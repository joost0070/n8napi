"""Bline advertentiesturing: dagelijkse run (ophalen, KPI's, beslisregels).

Gebruik:
    python3 dag.py sheet.json uit.json [--vandaag 2026-10-09]

sheet.json bevat de ruwe waarden van de tabbladen Config, Voorstellen en Logboek, precies zoals de
Sheets-API ze teruggeeft: {"Config": [[...], ...], "Voorstellen": [...], "Logboek": [...]}.
uit.json krijgt de rijen voor Dagcijfers, Voorstellen en Verslag. Dit script wijzigt zelf niets in
de advertentieaccounts.
"""
import argparse
import datetime as dt
import json
import sys

import bronnen
import regels

VOORSTEL_KOP = ['ID', 'Datum', 'Kanaal', 'Niveau', 'Wat', 'Object-ID', 'Actie', 'Van', 'Naar', 'Reden', 'Kans',
                'Akkoord', 'Uitgevoerd', 'Resultaat']
LOG_KOP = ['Tijd', 'Voorstel-ID', 'Kanaal', 'Wat', 'Object-ID', 'Actie', 'Oud', 'Nieuw', 'Akkoord', 'Status',
           'API-antwoord']


def als_dicts(rijen, kop):
    uit = []
    for i, r in enumerate(rijen[1:], start=2):
        r = list(r) + [''] * (len(kop) - len(r))
        d = dict(zip(kop, r))
        d['_rij'] = i
        uit.append(d)
    return uit


def voorstellen_uit_sheet(rijen):
    return [{'id': v['ID'], 'object': v['Object-ID'], 'actie': v['Actie'], 'akkoord': str(v['Akkoord']).upper(),
             'uitgevoerd': v['Uitgevoerd'], 'datum': v['Datum'], 'rij': v['_rij'], 'kanaal': v['Kanaal'],
             'niveau': v['Niveau'], 'wat': v['Wat'], 'van': v['Van'], 'naar': v['Naar']}
            for v in als_dicts(rijen, VOORSTEL_KOP) if v['ID']]


def logboek_uit_sheet(rijen):
    return [{'tijd': str(l['Tijd']), 'id': l['Voorstel-ID'], 'object': l['Object-ID'], 'status': l['Status']}
            for l in als_dicts(rijen, LOG_KOP) if l['Tijd']]


def veilig(naam, f, fouten):
    try:
        return f()
    except Exception as e:  # een bron die faalt mag de rest niet stoppen
        fouten.append(f'{naam}: {str(e)[:200]}')
        return None


def nl(x):
    return f'{x:g}'.replace('.', ',')


def eur(x):
    return '' if x is None else f'€{x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sheet')
    ap.add_argument('uit')
    ap.add_argument('--vandaag', default=dt.date.today().isoformat())
    a = ap.parse_args()
    sheet = json.load(open(a.sheet))
    cfg = regels.lees_config(sheet['Config'])
    gisteren = (dt.date.fromisoformat(a.vandaag) - dt.timedelta(days=1)).isoformat()
    start = str(cfg.get('start_verliesteller') or cfg.get('start_fase0'))
    van = min(start, (dt.date.fromisoformat(gisteren) - dt.timedelta(days=27)).isoformat())

    fouten = []
    data = {
        'google': veilig('Google Ads', lambda: bronnen.google(van, gisteren), fouten),
        'meta': veilig('Meta', lambda: bronnen.meta(van, gisteren), fouten),
        'shopify': veilig('Shopify', lambda: bronnen.shopify(van, gisteren), fouten),
        'clarity': veilig('Clarity', bronnen.clarity, fouten),
        'klaviyo': veilig('Klaviyo', lambda: bronnen.klaviyo(gisteren, gisteren), fouten),
    }
    if not data['google'] or not data['shopify']:
        json.dump({'fout': fouten}, open(a.uit, 'w'), ensure_ascii=False, indent=1)
        print('Gestopt: kernbron ontbreekt.', fouten)
        sys.exit(1)
    data['meta'] = data['meta'] or {'campagnes': [], 'adsets': [], 'ads': []}

    bestaand = voorstellen_uit_sheet(sheet.get('Voorstellen', [[]]))
    open_ = [v for v in bestaand if not v['uitgevoerd'] and v['akkoord'] != 'NEE']
    b = regels.Beslisser(cfg, data, a.vandaag, logboek_uit_sheet(sheet.get('Logboek', [[]])), open_)
    kpi = b.regels()

    # Dagcijfers voor gisteren
    dag = []
    orders_g = b._orders(van=gisteren)
    for c in data['google']['campagnes']:
        d = c['dagen'].get(gisteren)
        if not d and c['status'] != 'ENABLED':
            continue
        d = d or {}
        o = b._orders('google', c['id'], van=gisteren)
        k, kl, vt = d.get('kosten', 0), d.get('klik', 0), d.get('vert', 0)
        omzet = sum(x['omzet'] for x in o)
        dag.append([gisteren, 'Google', c['naam'], round(k, 2), vt, kl, round(kl / vt, 4) if vt else '',
                    round(k / kl, 2) if kl else '', d.get('conv', 0), round(d.get('waarde', 0), 2), len(o),
                    round(omzet, 2), round(omzet / k, 2) if k else '', '', '',
                    f"budget €{c['budget']:.0f}; verloren door budget {d.get('verlies_budget', 0):.0%}"])
    per_camp = {}
    for ad in data['meta']['ads']:
        d = ad['dagen'].get(gisteren)
        if not d:
            continue
        p = per_camp.setdefault(ad['campagnenaam'], {'kosten': 0, 'vert': 0, 'klik': 0, 'conv': 0, 'waarde': 0,
                                                     'winkelwagen': 0})
        for veld in p:
            p[veld] += d.get(veld, 0)
    for naam, p in per_camp.items():
        o = [x for x in b._orders('meta', van=gisteren)]
        omzet = sum(x['omzet'] for x in o)
        dag.append([gisteren, 'Meta', naam, round(p['kosten'], 2), p['vert'], p['klik'],
                    round(p['klik'] / p['vert'], 4) if p['vert'] else '',
                    round(p['kosten'] / p['klik'], 2) if p['klik'] else '', p['conv'], round(p['waarde'], 2), len(o),
                    round(omzet, 2), round(omzet / p['kosten'], 2) if p['kosten'] else '', '', '',
                    f"winkelwagens {p['winkelwagen']:.0f}"])
    s = data['shopify']['sessies'].get(gisteren, {})
    kl = (data.get('klaviyo') or {}).get(gisteren, {})
    cl = data.get('clarity') or {}
    g = kpi['gisteren']
    dag.append([gisteren, 'Totaal', 'alle kanalen (MER)', g['kosten'], '', '', '', '', '', '', g['orders'], g['omzet'],
                g['mer'] or '', s.get('sessies', ''), round(s.get('conversie', 0) * 100, 2) if s else '',
                f"betaald {g['betaald']}; checkouts {kl.get('checkouts', '')}; Clarity-sessies {cl.get('sessies', '')}, "
                f"scrolldiepte {cl.get('scrolldiepte', '')}%"])

    # Voorstellen met nieuw ID
    nr = 1 + sum(1 for v in bestaand if str(v['id']).startswith('V' + a.vandaag.replace('-', '')))
    rijen_v = []
    for v in b.voorstellen:
        vid = f"V{a.vandaag.replace('-', '')}-{nr:02d}"
        nr += 1
        rijen_v.append([vid, a.vandaag, v['kanaal'], v['niveau'], v['wat'], v['object'], v['actie'], v['van'],
                        v['naar'], v['reden'], v['kans'], '', '', ''])

    t = kpi['totaal']
    w = kpi['7 dagen']
    stand = (f"Sinds {start}: {eur(t['kosten'])} uitgegeven, {t['orders']} orders, omzet {eur(t['omzet'])}, "
             f"bijdrage na advertenties {eur(t['bijdrage_na_ads'])}.")
    if t['kosten'] >= 10:
        stand += (f" Kans dat de echte ROAS boven {nl(cfg['test_roas'])} ligt: {t['kans_test']:.0%}, boven "
                  f"{nl(cfg['breakeven_roas'])} (break-even): {t['kans_breakeven']:.0%}.")
    else:
        stand += ' Nog te weinig uitgave voor een kansberekening.'
    m = regels.mijlpaal(cfg, a.vandaag, t['orders'], t['kosten'])
    if m:
        stand += ' ' + m
    stand += f' {len(rijen_v)} nieuwe voorstellen.' if rijen_v else ' Geen nieuwe voorstellen.'
    if b.notities:
        stand += ' ' + ' '.join(b.notities)
    vlaggen = b.vlaggen + [f'Bron niet bereikbaar: {f}' for f in fouten]
    verslag = [a.vandaag,
               f"{gisteren}: {eur(g['kosten'])} kosten, {g['orders']} orders, omzet {eur(g['omzet'])}, MER {g['mer'] or '-'}; "
               f"sessies {s.get('sessies', '-')}",
               f"{eur(w['kosten'])} kosten, {w['orders']} orders, omzet {eur(w['omzet'])}, MER {w['mer'] or '-'}, "
               f"CPA {eur(w['cpa']) or '-'}",
               stand, ' | '.join(vlaggen) or 'geen']
    uit = {'dagcijfers': dag, 'voorstellen': rijen_v, 'verslag': verslag, 'kpi': kpi, 'aov': b.aov,
           'zoektermen_te_beoordelen': getattr(b, 'te_beoordelen', []), 'fouten': fouten}
    json.dump(uit, open(a.uit, 'w'), ensure_ascii=False, indent=1)
    print(json.dumps({'verslag': verslag, 'voorstellen': len(rijen_v), 'zoektermen': len(uit['zoektermen_te_beoordelen']),
                      'fouten': fouten}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
