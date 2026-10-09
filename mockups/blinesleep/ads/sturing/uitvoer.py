"""Bline advertentiesturing: uitvoerder.

Voert alleen voorstellen uit met Akkoord = JA, die nog niet zijn uitgevoerd en niet in het logboek staan.
De harde grenzen staan hier in de code, niet alleen in de instructies:
  - Config "automatisering_aan" moet JA zijn (noodstop), anders gebeurt er niets;
  - budget hooguit +max_stap_omhoog of -max_stap_omlaag ten opzichte van het huidige budget in het account;
  - het totale dagbudget blijft onder plafond_dagbudget_totaal;
  - per object hooguit één wijziging per min_dagen_tussen_wijzigingen;
  - "Van" moet nog kloppen met de huidige stand (anders is het voorstel verouderd);
  - een voorstel ouder dan 3 dagen vervalt;
  - alleen de acties budget, bod, pauze, aan en uitsluiten.

Gebruik:
    python3 uitvoer.py sheet.json uit.json          # droog: controleert alleen
    python3 uitvoer.py sheet.json uit.json --echt   # voert uit
uit.json krijgt de logboekregels en de updates voor de kolommen Uitgevoerd en Resultaat in Voorstellen.
"""
import argparse
import datetime as dt
import json

import requests

import bronnen
import regels
from dag import logboek_uit_sheet, voorstellen_uit_sheet

ACTIES = {'budget', 'bod', 'pauze', 'aan', 'uitsluiten'}
MAX_LEEFTIJD = 3


class Weigering(Exception):
    pass


def _getal(v):
    return float(str(v).replace('€', '').replace(',', '.').strip())


class Google:
    def __init__(self):
        self.g = bronnen.GoogleAds()
        self.cid = bronnen.GADS_CID

    def campagne(self, cid):
        r = self.g.search('SELECT campaign.status, campaign_budget.amount_micros, campaign_budget.resource_name '
                          f'FROM campaign WHERE campaign.id = {int(cid)}')
        if not r:
            raise Weigering('campagne niet gevonden')
        return r[0]

    def totaal_budget(self):
        r = self.g.search("SELECT campaign_budget.amount_micros FROM campaign WHERE campaign.status = 'ENABLED'")
        return sum(int(x['campaignBudget']['amountMicros']) for x in r) / 1e6

    def criterium(self, rn):
        r = self.g.search('SELECT ad_group_criterion.status, ad_group_criterion.cpc_bid_micros '
                          f"FROM ad_group_criterion WHERE ad_group_criterion.resource_name = '{rn}'")
        if not r:
            raise Weigering('zoekwoord of product niet gevonden')
        return r[0]['adGroupCriterion']

    def run(self, ops, echt):
        status, antwoord = self.g.mutate(ops, validate=not echt)
        if status != 200:
            raise Weigering('Google: ' + json.dumps(antwoord)[:300])
        return 'Google OK' + ('' if echt else ' (validatie)')


class Meta:
    def __init__(self):
        self.t = bronnen.E['META_ACCESS_TOKEN']

    def lees(self, oid):
        r = requests.get(bronnen.META_V + oid, params={'access_token': self.t,
                                                       'fields': 'name,effective_status,status,daily_budget'},
                         timeout=60).json()
        if 'error' in r:
            raise Weigering('Meta: ' + r['error'].get('message', '')[:200])
        return r

    def totaal_budget(self):
        acc = bronnen.E['META_AD_ACCOUNT_ID']
        acc = acc if acc.startswith('act_') else 'act_' + acc
        som = 0.0
        for soort in ('adsets', 'campaigns'):
            r = requests.get(bronnen.META_V + f'{acc}/{soort}', params={
                'access_token': self.t, 'fields': 'effective_status,daily_budget', 'limit': 200}, timeout=60).json()
            som += sum(int(x.get('daily_budget') or 0) / 100 for x in r.get('data', [])
                       if x.get('effective_status') == 'ACTIVE')
        return som

    def zet(self, oid, velden, echt):
        if not echt:
            return 'Meta (droog, niet verstuurd)'
        d = dict(velden)
        d['access_token'] = self.t
        r = requests.post(bronnen.META_V + oid, data=d, timeout=60).json()
        if 'error' in r:
            raise Weigering('Meta: ' + r['error'].get('message', '')[:200])
        return 'Meta OK'


def controleer_en_voer_uit(v, cfg, logboek, vandaag, google, meta, echt):
    actie = v['actie']
    if actie not in ACTIES:
        raise Weigering(f'actie "{actie}" is niet toegestaan')
    leeftijd = (dt.date.fromisoformat(vandaag) - dt.date.fromisoformat(str(v['datum']))).days
    if leeftijd > MAX_LEEFTIJD:
        raise Weigering(f'voorstel is {leeftijd} dagen oud: vervallen, wordt zo nodig opnieuw voorgesteld')
    if actie in ('budget', 'bod'):
        laatste = [r['tijd'][:10] for r in logboek if r['object'] == v['object'] and r['status'] == 'uitgevoerd']
        if laatste:
            dagen = (dt.date.fromisoformat(vandaag) - dt.date.fromisoformat(max(laatste))).days
            if dagen < cfg.get('min_dagen_tussen_wijzigingen', 3):
                raise Weigering(f'laatste wijziging {dagen} dagen geleden')
    omhoog, omlaag = cfg['max_stap_omhoog'], cfg['max_stap_omlaag']

    def stap(oud, nieuw):
        if nieuw > oud * (1 + omhoog) + 0.005 or nieuw < oud * (1 - omlaag) - 0.005:
            raise Weigering(f'{oud:.2f} naar {nieuw:.2f} is meer dan +{omhoog:.0%}/-{omlaag:.0%}')

    def van_klopt(huidig):
        if v['van'] not in ('', None) and abs(_getal(v['van']) - huidig) > 0.01:
            raise Weigering(f'stand is veranderd (nu {huidig:.2f}, voorstel ging uit van {v["van"]})')

    if v['kanaal'] == 'Google':
        if v['niveau'] == 'campagne':
            c = google.campagne(v['object'])
            rn_c = f'customers/{google.cid}/campaigns/{v["object"]}'
            if actie == 'budget':
                oud = int(c['campaignBudget']['amountMicros']) / 1e6
                nieuw = _getal(v['naar'])
                van_klopt(oud)
                stap(oud, nieuw)
                totaal = google.totaal_budget() + meta.totaal_budget() - oud + nieuw
                if totaal > cfg['plafond_dagbudget_totaal'] + 0.005:
                    raise Weigering(f'totaal dagbudget zou €{totaal:.2f} worden, plafond €{cfg["plafond_dagbudget_totaal"]:.0f}')
                op = {'campaignBudgetOperation': {'update': {'resourceName': c['campaignBudget']['resourceName'],
                                                             'amountMicros': str(round(nieuw * 1e6))},
                                                  'updateMask': 'amountMicros'}}
                return oud, nieuw, google.run([op], echt)
            if actie in ('pauze', 'aan'):
                nieuw = 'PAUSED' if actie == 'pauze' else 'ENABLED'
                op = {'campaignOperation': {'update': {'resourceName': rn_c, 'status': nieuw}, 'updateMask': 'status'}}
                return c['campaign']['status'], nieuw, google.run([op], echt)
            if actie == 'uitsluiten':
                tekst = str(v['naar']).strip()
                match = 'EXACT'
                for pre, m in (('exact:', 'EXACT'), ('phrase:', 'PHRASE'), ('woordgroep:', 'PHRASE')):
                    if tekst.lower().startswith(pre):
                        match, tekst = m, tekst[len(pre):].strip()
                if not tekst or len(tekst) > 80:
                    raise Weigering('lege of te lange uitsluiting')
                op = {'campaignCriterionOperation': {'create': {'campaign': rn_c, 'negative': True,
                                                                'keyword': {'text': tekst, 'matchType': match}}}}
                return '', f'{match.lower()}: {tekst}', google.run([op], echt)
        if v['niveau'] in ('zoekwoord', 'product'):
            k = google.criterium(v['object'])
            if actie == 'bod':
                oud = int(k.get('cpcBidMicros', 0)) / 1e6
                nieuw = _getal(v['naar'])
                if not oud:
                    raise Weigering('geen eigen bod op dit niveau')
                van_klopt(oud)
                stap(oud, nieuw)
                if not cfg.get('bod_min', 0.15) - 0.005 <= nieuw <= cfg.get('bod_max', 1.0) + 0.005:
                    raise Weigering(f'bod {nieuw:.2f} buiten de grenzen {cfg.get("bod_min", 0.15):.2f} tot {cfg.get("bod_max", 1.0):.2f}')
                op = {'adGroupCriterionOperation': {'update': {'resourceName': v['object'],
                                                               'cpcBidMicros': str(round(nieuw * 1e6))},
                                                    'updateMask': 'cpcBidMicros'}}
                return oud, nieuw, google.run([op], echt)
            if actie in ('pauze', 'aan'):
                if v['niveau'] == 'product':
                    raise Weigering('product pauzeren gaat via een uitsluiting in de productgroep: handmatig')
                nieuw = 'PAUSED' if actie == 'pauze' else 'ENABLED'
                op = {'adGroupCriterionOperation': {'update': {'resourceName': v['object'], 'status': nieuw},
                                                    'updateMask': 'status'}}
                return k.get('status'), nieuw, google.run([op], echt)
        raise Weigering(f'Google {v["niveau"]}/{actie} wordt niet ondersteund')

    if v['kanaal'] == 'Meta':
        o = meta.lees(v['object'])
        if actie == 'budget':
            if not o.get('daily_budget'):
                raise Weigering('dit object heeft geen eigen dagbudget')
            oud = int(o['daily_budget']) / 100
            nieuw = _getal(v['naar'])
            van_klopt(oud)
            stap(oud, nieuw)
            totaal = google.totaal_budget() + meta.totaal_budget() - (oud if o.get('effective_status') == 'ACTIVE' else 0) + nieuw
            if totaal > cfg['plafond_dagbudget_totaal'] + 0.005:
                raise Weigering(f'totaal dagbudget zou €{totaal:.2f} worden, plafond €{cfg["plafond_dagbudget_totaal"]:.0f}')
            return oud, nieuw, meta.zet(v['object'], {'daily_budget': str(round(nieuw * 100))}, echt)
        if actie in ('pauze', 'aan'):
            nieuw = 'PAUSED' if actie == 'pauze' else 'ACTIVE'
            return o.get('status'), nieuw, meta.zet(v['object'], {'status': nieuw}, echt)
        raise Weigering(f'Meta {actie} wordt niet ondersteund')
    raise Weigering(f'onbekend kanaal {v["kanaal"]}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sheet')
    ap.add_argument('uit')
    ap.add_argument('--echt', action='store_true')
    ap.add_argument('--vandaag', default=dt.date.today().isoformat())
    a = ap.parse_args()
    sheet = json.load(open(a.sheet))
    cfg = regels.lees_config(sheet['Config'])
    logboek = logboek_uit_sheet(sheet.get('Logboek', [[]]))
    gedaan = {r['id'] for r in logboek if r['status'] == 'uitgevoerd'}
    alles_aan = str(cfg.get('automatisering_aan', 'NEE')).upper() == 'JA'
    mandaat = str(cfg.get('mandaat_biedingen', 'NEE')).upper() == 'JA'
    open_ = [v for v in voorstellen_uit_sheet(sheet.get('Voorstellen', [[]]))
             if not v['uitgevoerd'] and v['id'] not in gedaan]
    # Akkoord JA: alles (alleen als de noodstop op JA staat). Akkoord MANDAAT: alleen biedingen, met het
    # biedmandaat van Joost (09-10), ook als de noodstop op NEE staat. NEE of leeg: niets.
    te_doen = [v for v in open_ if (v['akkoord'] == 'JA' and alles_aan)
               or (v['akkoord'] in ('JA', 'MANDAAT') and mandaat and v['actie'] == 'bod')]
    uit = {'logboek': [], 'voorstellen_updates': [], 'bericht': ''}
    if not te_doen:
        wachtend = sum(1 for v in open_ if v['akkoord'] in ('JA', 'MANDAAT'))
        uit['bericht'] = (f'Niets uit te voeren (noodstop {"JA" if alles_aan else "NEE"}, biedmandaat '
                          f'{"JA" if mandaat else "NEE"}; {wachtend} goedgekeurd en wachtend).')
        json.dump(uit, open(a.uit, 'w'), ensure_ascii=False, indent=1)
        print(uit['bericht'])
        return
    google, meta = Google(), Meta()
    nu = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
    for v in te_doen:
        try:
            oud, nieuw, antwoord = controleer_en_voer_uit(v, cfg, logboek, a.vandaag, google, meta, a.echt)
            status = 'uitgevoerd' if a.echt else 'gecontroleerd'
        except Weigering as e:
            oud, nieuw, antwoord, status = v['van'], v['naar'], str(e), 'geweigerd'
        except Exception as e:  # onverwacht: niet opnieuw proberen zonder blik van een mens
            oud, nieuw, antwoord, status = v['van'], v['naar'], f'fout: {str(e)[:200]}', 'fout'
        rij = [nu, v['id'], v['kanaal'], v['wat'], v['object'], v['actie'], oud, nieuw, v['akkoord'], status, antwoord]
        uit['logboek'].append(rij)
        if a.echt or status == 'geweigerd':
            uit['voorstellen_updates'].append({'rij': v['rij'], 'waarden': [nu if status == 'uitgevoerd' else '',
                                                                           f'{status}: {antwoord}']})
        if status == 'uitgevoerd':
            logboek.append({'tijd': nu, 'id': v['id'], 'object': v['object'], 'status': 'uitgevoerd'})
    uit['bericht'] = f'{len(te_doen)} goedgekeurde voorstellen verwerkt ({"echt" if a.echt else "droog"}).'
    json.dump(uit, open(a.uit, 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(uit, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
