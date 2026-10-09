"""Tests voor de beslisregels en de vangrails van de uitvoerder. Draaien: python3 -m pytest -q test_sturing.py"""
import datetime as dt

import pytest

import regels
import uitvoer

CFG = regels.lees_config([['Sleutel', 'Waarde']] + [[k, v] for k, v in {
    'automatisering_aan': 'JA', 'start_verliesteller': '2026-10-01', 'gem_orderwaarde': 81.58,
    'bijdrage_per_order': 26, 'breakeven_roas': 3.15, 'test_roas': 2.0, 'opschaal_roas': 4.0,
    'opschaal_min_orders_14d': 15, 'verlies_week': 75, 'verlies_totaal': 300, 'kanaal_zonder_aankoop': 125,
    'max_stap_omhoog': 0.2, 'max_stap_omlaag': 0.3, 'min_dagen_tussen_wijzigingen': 3,
    'plafond_dagbudget_totaal': 25, 'kans_pauze': 0.1, 'kans_opschalen': 0.8, 'zoekwoord_bod_omlaag': 52,
    'zoekwoord_pauze': 78, 'zoekwoord_pauze_klikken': 200, 'meta_aandacht_euro': 8, 'meta_min_ctr': 0.006,
    'meta_min_hookrate': 0.2, 'meta_klik_euro': 15, 'meta_max_cpc': 1.0, 'meta_aankoop_euro': 52,
    'meta_plafond_euro': 78}.items()])


def test_kansen_volgen_de_beslistabel():
    # dag 14, €280: 0-3 orders -> kans op ROAS > 2 hooguit 6%; 15 orders -> > 3,15 minstens 86%
    assert regels.kans_roas_boven(3, 280, 2.0, 81.58, 26) <= 0.06
    assert regels.kans_roas_boven(15, 280, 3.15, 81.58, 26) >= 0.855  # tabel rondt af op 86%
    # dag 7, €140: 0-1 orders -> hooguit 9%
    assert regels.kans_roas_boven(1, 140, 2.0, 81.58, 26) <= 0.09


def _dagen(start, n, **per_dag):
    d0 = dt.date.fromisoformat(start)
    return {(d0 + dt.timedelta(days=i)).isoformat(): dict(per_dag) for i in range(n)}


def _data(google_kosten_per_dag=10.0, orders=(), zoekwoorden=(), meta_ads=()):
    return {
        'google': {'campagnes': [{'id': '1', 'naam': '02 Generiek', 'status': 'ENABLED', 'budget': 10.0,
                                  'budget_rn': 'b/1', 'dagen': _dagen('2026-10-01', 14, kosten=google_kosten_per_dag,
                                                                      klik=10, vert=200, conv=0, waarde=0,
                                                                      verlies_budget=0.3)}],
                   'zoekwoorden': list(zoekwoorden), 'producten': [], 'zoektermen': [], 'afgekeurd': []},
        'meta': {'campagnes': [], 'adsets': [], 'ads': list(meta_ads)},
        'shopify': {'orders': list(orders), 'sessies': {}},
        'clarity': {}, 'klaviyo': {}}


def test_kanaal_zonder_aankoop_gaat_op_pauze():
    b = regels.Beslisser(CFG, _data(10.0), '2026-10-15')
    b.regels()
    assert any(v['actie'] == 'pauze' and v['object'] == '1' for v in b.voorstellen)


def test_geen_pauze_bij_weinig_uitgave():
    b = regels.Beslisser(CFG, _data(2.0), '2026-10-15')
    b.regels()
    assert not [v for v in b.voorstellen if v['actie'] == 'pauze']


def test_opschalen_alleen_met_genoeg_orders_en_binnen_plafond():
    orders = [{'order': f'#{i}', 'datum': '2026-10-%02d' % (2 + i % 12), 'omzet': 82.0, 'terug': 0,
               'kanaal': 'google', 'campagne': '1', 'content': None} for i in range(16)]
    b = regels.Beslisser(CFG, _data(10.0, orders), '2026-10-15')
    b.regels()
    budget = [v for v in b.voorstellen if v['actie'] == 'budget']
    assert budget and budget[0]['naar'] == 12.0


def test_zoekwoord_bod_omlaag_en_pauze():
    zw = [{'campagne': '1', 'rn': 'k/1', 'tekst': 'leeskussen', 'match': 'EXACT', 'bod': 0.7, 'kosten': 60,
           'klik': 80, 'conv': 0, 'waarde': 0},
          {'campagne': '1', 'rn': 'k/2', 'tekst': 'kussen', 'match': 'PHRASE', 'bod': 0.5, 'kosten': 80,
           'klik': 90, 'conv': 0, 'waarde': 0}]
    b = regels.Beslisser(CFG, _data(2.0, zoekwoorden=zw), '2026-10-15')
    b.regels()
    acties = {(v['object'], v['actie'], v['naar']) for v in b.voorstellen}
    assert ('k/1', 'bod', 0.49) in acties
    assert ('k/2', 'pauze', 'pauze') in acties


def test_meta_advertentie_zonder_aankoop_na_plafond():
    ad = {'id': 'a1', 'naam': 'bl_test', 'adset': 's1', 'campagne': 'c1', 'campagnenaam': 'c', 'status': 'ACTIVE',
          'video': False, 'dagen': _dagen('2026-10-01', 10, kosten=8.0, vert=1000, klik=12, video3s=0,
                                          winkelwagen=1, conv=0, waarde=0)}
    b = regels.Beslisser(CFG, _data(0.0, meta_ads=[ad]), '2026-10-15')
    b.regels()
    assert any(v['object'] == 'a1' and v['actie'] == 'pauze' for v in b.voorstellen)


def test_open_voorstel_wordt_niet_dubbel_voorgesteld():
    b = regels.Beslisser(CFG, _data(10.0), '2026-10-15', open_voorstellen=[{'object': '1', 'actie': 'pauze'}])
    b.regels()
    assert not [v for v in b.voorstellen if v['object'] == '1' and v['actie'] == 'pauze']


class NepGoogle:
    cid = '8605359447'

    def __init__(self, budget=10.0, totaal=10.0):
        self.budget, self.totaal, self.verstuurd = budget, totaal, []

    def campagne(self, cid):
        return {'campaign': {'status': 'ENABLED'},
                'campaignBudget': {'amountMicros': str(int(self.budget * 1e6)), 'resourceName': 'b/1'}}

    def totaal_budget(self):
        return self.totaal

    def run(self, ops, echt):
        self.verstuurd.append(ops)
        return 'ok'


class NepMeta:
    def totaal_budget(self):
        return 8.0


def _v(**kw):
    v = {'id': 'V1', 'datum': '2026-10-15', 'kanaal': 'Google', 'niveau': 'campagne', 'object': '1',
         'actie': 'budget', 'van': 10.0, 'naar': 12.0, 'wat': 'x'}
    v.update(kw)
    return v


def test_uitvoerder_houdt_zich_aan_de_stapgrens():
    g = NepGoogle()
    with pytest.raises(uitvoer.Weigering):
        uitvoer.controleer_en_voer_uit(_v(naar=13.0), CFG, [], '2026-10-15', g, NepMeta(), True)
    with pytest.raises(uitvoer.Weigering):
        uitvoer.controleer_en_voer_uit(_v(naar=6.0), CFG, [], '2026-10-15', g, NepMeta(), True)
    assert uitvoer.controleer_en_voer_uit(_v(naar=12.0), CFG, [], '2026-10-15', g, NepMeta(), True)[1] == 12.0


def test_uitvoerder_houdt_zich_aan_het_plafond():
    g = NepGoogle(budget=10.0, totaal=16.0)  # 16 Google + 8 Meta = 24; +2 wordt 26 > 25
    with pytest.raises(uitvoer.Weigering):
        uitvoer.controleer_en_voer_uit(_v(naar=12.0), CFG, [], '2026-10-15', g, NepMeta(), True)


def test_uitvoerder_weigert_te_snel_opnieuw_en_verouderd():
    g = NepGoogle()
    log = [{'tijd': '2026-10-14 18:00', 'id': 'V0', 'object': '1', 'status': 'uitgevoerd'}]
    with pytest.raises(uitvoer.Weigering):
        uitvoer.controleer_en_voer_uit(_v(), CFG, log, '2026-10-15', g, NepMeta(), True)
    with pytest.raises(uitvoer.Weigering):
        uitvoer.controleer_en_voer_uit(_v(datum='2026-10-10'), CFG, [], '2026-10-15', g, NepMeta(), True)
    with pytest.raises(uitvoer.Weigering):
        uitvoer.controleer_en_voer_uit(_v(van=8.0, naar=9.0), CFG, [], '2026-10-15', g, NepMeta(), True)
    with pytest.raises(uitvoer.Weigering):
        uitvoer.controleer_en_voer_uit(_v(actie='biedstrategie'), CFG, [], '2026-10-15', g, NepMeta(), True)


def test_doelbod_volgt_conversie():
    b = regels.Beslisser(CFG, _data(0.0), '2026-10-15')
    # zonder data: prior 2% x 26 x 0,9 = 0,47
    assert abs(b.doelbod(0, 0) - 0.468) < 0.01
    # 100 klikken, 4 aankopen: (4 + 1) / 150 = 3,3% -> 0,78
    assert abs(b.doelbod(100, 4) - 0.78) < 0.01


def test_bod_naar_doel_binnen_stapgrens():
    zw = [{'campagne': '1', 'rn': 'k/3', 'tekst': 'leeskussen bed', 'match': 'EXACT', 'bod': 0.5, 'kosten': 30,
           'klik': 60, 'conv': 4, 'waarde': 320}]
    b = regels.Beslisser(CFG, _data(2.0, zoekwoorden=zw), '2026-10-15')
    b.regels()
    v = [v for v in b.voorstellen if v['object'] == 'k/3']
    assert v and v[0]['actie'] == 'bod' and v[0]['naar'] == 0.6  # doel ~1,03, maar hooguit +20%


def test_mandaat_voert_alleen_biedingen_uit(tmp_path):
    import json
    kop = ['ID', 'Datum', 'Kanaal', 'Niveau', 'Wat', 'Object-ID', 'Actie', 'Van', 'Naar', 'Reden', 'Kans', 'Akkoord',
           'Uitgevoerd', 'Resultaat']
    cfg = [['Sleutel', 'Waarde'], ['automatisering_aan', 'NEE'], ['mandaat_biedingen', 'JA']] + \
        [[k, v] for k, v in CFG.items() if k not in ('automatisering_aan',)]
    vandaag = dt.date.today().isoformat()
    sheet = {'Config': cfg, 'Logboek': [['Tijd']], 'Voorstellen': [kop,
             ['V1', vandaag, 'Google', 'campagne', 'x', '1', 'budget', 10, 12, '', '', 'MANDAAT', '', ''],
             ['V2', vandaag, 'Google', 'campagne', 'x', '1', 'budget', 10, 12, '', '', 'JA', '', '']]}
    p = tmp_path / 's.json'
    p.write_text(json.dumps(sheet))
    import subprocess, sys, os
    uit = tmp_path / 'u.json'
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), 'uitvoer.py'), str(p), str(uit)], check=True)
    assert json.loads(uit.read_text())['logboek'] == []  # budget nooit via het biedmandaat, en noodstop staat op NEE


def test_uitvoerder_houdt_bod_binnen_grenzen():
    class G(NepGoogle):
        def criterium(self, rn):
            return {'cpcBidMicros': '1000000', 'status': 'ENABLED'}
    cfg = dict(CFG, bod_max=1.0)
    with pytest.raises(uitvoer.Weigering):
        uitvoer.controleer_en_voer_uit(_v(niveau='zoekwoord', object='k/1', actie='bod', van=1.0, naar=1.15),
                                       cfg, [], '2026-10-15', G(), NepMeta(), True)
