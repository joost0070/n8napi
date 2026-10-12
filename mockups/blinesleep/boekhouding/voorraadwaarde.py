"""Voorraadwaarde per de 1e van de maand, gesplitst in NL (fysiek bij de fulfilment) en CN (betaald, nog bij de leverancier).

Gebruik:
    python3 voorraadwaarde.py [--peildatum 2026-10-01] [--schrijf]

Zonder --peildatum: de 1e van de huidige maand. Aantallen komen uit tab "📆 Voorraad Dagregister" (stand aan het
begin van de dag, dus de rij van de 1e = stand per einde van de vorige maand). Prijzen, partijen en inkooporders staan
bovenaan tab "🧾 Voorraadwaarde" in de Shop4You-werkmap; daar wijzig je ze, niet hier. Met --schrijf komt de uitkomst
als regel WAARDE onderaan dat tabblad (een bestaande regel voor dezelfde peildatum wordt overschreven).

Waardering: inkoopwaarde excl. btw, FIFO. Wat er van een product ligt, komt uit de nieuwste partijen; een partij zonder
aantal is de rest. CN = stuks op een inkooporder (PO) min de partijen die van die order al binnen zijn.
"""
import argparse
import datetime as dt
import os
import sys
import urllib.parse

sys.path.insert(0, os.path.expanduser('~/.config/bline'))
import px  # noqa: E402  (proxy-helper, sleutels blijven buiten de repo)

WERKMAP = '1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw'
TAB = '🧾 Voorraadwaarde'
REGISTER = '📆 Voorraad Dagregister'


def getal(x):
    x = str(x).strip()
    return float(x.replace('.', '').replace(',', '.')) if ',' in x else float(x or 0)


def eur(x):
    return f'{x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def lees_instellingen(rijen):
    po, partijen, prijs, negeer = [], {}, {}, set()
    for r in rijen:
        r = list(r) + [''] * 7
        soort, oms, eans, stuks, pps, datum = r[0], r[1], r[2], r[3], r[4], r[5]
        if soort == 'PO':
            po.append({'sleutel': oms, 'ean': eans, 'stuks': getal(stuks), 'prijs': getal(pps), 'datum': datum})
        elif soort == 'PARTIJ':
            partijen.setdefault(eans, []).append({'oms': oms, 'stuks': getal(stuks) if str(stuks).strip() else None,
                                                  'prijs': getal(pps), 'datum': datum})
        elif soort == 'PRIJS':
            for e in eans.split(','):
                prijs[e.strip()] = getal(pps)
        elif soort == 'NEGEER':
            negeer.update(e.strip() for e in eans.split(','))
    for lijst in partijen.values():
        lijst.sort(key=lambda p: p['datum'], reverse=True)  # nieuwste eerst: FIFO laat de nieuwste liggen
    return po, partijen, prijs, negeer


def stand(register, peildatum):
    data = sorted({r[0] for r in register[1:] if r and r[0] <= peildatum})
    if not data:
        sys.exit(f'Geen voorraadstand op of voor {peildatum}.')
    dag = data[-1]
    return dag, {r[1]: (r[2], getal(r[3])) for r in register[1:] if r and r[0] == dag}


def waardeer(aantal, partijen):
    over, waarde = aantal, 0.0
    for p in partijen:
        n = over if p['stuks'] is None else min(over, p['stuks'])
        waarde += n * p['prijs']
        over -= n
        if over <= 0:
            break
    return waarde, over  # over > 0: meer voorraad dan bekende partijen


def bereken(peildatum):
    instel = px.sheet_get(WERKMAP, f'{TAB}!A1:G9').get('values', [])
    po, partijen, prijs, negeer = lees_instellingen(instel[3:])
    # alleen wat op de peildatum al betaald of binnen was
    po = [o for o in po if o['datum'] <= peildatum]
    partijen = {e: [p for p in lijst if p['datum'] <= peildatum] for e, lijst in partijen.items()}
    dag, voorraad = stand(px.sheet_get(WERKMAP, f'{REGISTER}!A1:E5000')['values'], peildatum)
    opm, kussen_st, kussen_w, hoes_st, hoes_w, overig_w = [], 0, 0.0, 0, 0.0, 0.0
    for ean, (naam, n) in sorted(voorraad.items()):
        if ean in negeer or n <= 0:
            continue
        if ean in partijen:
            w, tekort = waardeer(n, partijen[ean])
            if tekort > 0:
                opm.append(f'{naam}: {tekort:.0f} stuks zonder bekende partij')
            kussen_st, kussen_w = kussen_st + n, kussen_w + w
        elif ean in prijs:
            w = n * prijs[ean]
            if naam.lower().startswith('hoes'):
                hoes_st, hoes_w = hoes_st + n, hoes_w + w
            else:
                overig_w += w
                opm.append(f'{naam} {n:.0f} x {eur(prijs[ean])}')
        else:
            opm.append(f'{naam} ({ean}) {n:.0f} stuks zonder prijs, niet meegeteld')
    cn_st, cn_w = 0, 0.0
    for o in po:
        binnen = sum(p['stuks'] or 0 for p in partijen.get(o['ean'], []) if p['oms'].startswith(o['sleutel']))
        rest = max(0.0, o['stuks'] - binnen)
        cn_st, cn_w = cn_st + rest, cn_w + rest * o['prijs']
    nl = kussen_w + hoes_w + overig_w
    if dag != peildatum:
        opm.insert(0, f'stand van {dag} gebruikt')
    return [peildatum, kussen_st, round(kussen_w, 2), hoes_st, round(hoes_w, 2), round(overig_w, 2), round(nl, 2),
            cn_st, round(cn_w, 2), round(nl + cn_w, 2), '; '.join(opm)]


def schrijf(regel):
    kolom_a = px.sheet_get(WERKMAP, f'{TAB}!A1:B300').get('values', [])
    rij = next((i for i, r in enumerate(kolom_a, 1) if len(r) > 1 and r[0] == 'WAARDE' and r[1] == regel[0]), None)
    rij = rij or len(kolom_a) + 1
    bereik = f'{TAB}!A{rij}:L{rij}'
    url = 'https://sheets.googleapis.com/v4/spreadsheets/%s/values/%s?valueInputOption=RAW' % (
        WERKMAP, urllib.parse.quote(bereik))
    sc, r = px.sheet('PUT', url, {'range': bereik, 'values': [['WAARDE'] + regel]})
    if sc != 200:
        sys.exit(f'Schrijven mislukt: {sc} {str(r)[:200]}')
    return rij


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--peildatum', default=dt.date.today().replace(day=1).isoformat())
    ap.add_argument('--schrijf', action='store_true')
    a = ap.parse_args()
    r = bereken(a.peildatum)
    print(f'Voorraadwaarde per {r[0]} (inkoopwaarde excl. btw):')
    print(f'  NL  € {eur(r[6])}  (kussens {r[1]:.0f} = € {eur(r[2])}, hoezen {r[3]:.0f} = € {eur(r[4])}, overig € {eur(r[5])})')
    print(f'  CN  € {eur(r[8])}  ({r[7]:.0f} kussens betaald, nog bij de leverancier)')
    print(f'  Totaal € {eur(r[9])}')
    if r[10]:
        print(f'  Opmerking: {r[10]}')
    if a.schrijf:
        print(f'Geschreven in rij {schrijf(r)} van {TAB}.')


if __name__ == '__main__':
    main()
