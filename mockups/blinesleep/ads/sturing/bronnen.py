"""Bline advertentiesturing: gegevens ophalen uit Google Ads, Meta, Shopify, Clarity en Klaviyo.

Alleen lezen. Sleutels komen uit de omgeving (GOOGLE_ADS_*, META_*, BLINE_SHOPIFY_*, Bline_Clarity,
KLAVIYO_BlineSleep) en worden nooit gelogd of opgeslagen.
"""
import datetime as dt
import os
import re

import requests

E = os.environ
GADS_CID = '8605359447'
GADS_V = 'v22'
META_V = 'https://graph.facebook.com/v23.0/'
SHOP = 'zaiap0-jj.myshopify.com'
SHOP_V = '2026-10'
TIMEOUT = 90


# ---------- Google Ads ----------

def _gads_headers():
    t = requests.post('https://oauth2.googleapis.com/token', data={
        'client_id': E['GOOGLE_ADS_CLIENT_ID'], 'client_secret': E['GOOGLE_ADS_CLIENT_SECRET'],
        'refresh_token': E['GOOGLE_ADS_REFRESH_TOKEN'], 'grant_type': 'refresh_token'}, timeout=30).json()
    return {'Authorization': 'Bearer ' + t['access_token'],
            'developer-token': E['GOOGLE_ADS_DEVELOPER_TOKEN'],
            'login-customer-id': E['GOOGLE_ADS_LOGIN_CUSTOMER_ID'].replace('-', '')}


class GoogleAds:
    def __init__(self):
        self.h = _gads_headers()

    def search(self, q):
        out, tok = [], None
        while True:
            body = {'query': q}
            if tok:
                body['pageToken'] = tok
            r = requests.post(f'https://googleads.googleapis.com/{GADS_V}/customers/{GADS_CID}/googleAds:search',
                              headers=self.h, json=body, timeout=TIMEOUT).json()
            if 'error' in r:
                raise RuntimeError('Google Ads: ' + str(r['error'].get('message', r['error']))[:400])
            out += r.get('results', [])
            tok = r.get('nextPageToken')
            if not tok:
                return out

    def mutate(self, ops, validate=False):
        r = requests.post(f'https://googleads.googleapis.com/{GADS_V}/customers/{GADS_CID}/googleAds:mutate',
                          headers=self.h, json={'mutateOperations': ops, 'partialFailure': False,
                                                'validateOnly': validate}, timeout=TIMEOUT)
        return r.status_code, r.json()


def _m(x, k):
    return float(x.get('metrics', {}).get(k, 0) or 0)


def google(van, tot):
    """Campagnes per dag, plus zoekwoorden, producten en zoektermen opgeteld over van..tot."""
    g = GoogleAds()
    periode = f"segments.date BETWEEN '{van}' AND '{tot}'"
    camp = {}
    for x in g.search(
            "SELECT campaign.id, campaign.name, campaign.status, campaign.advertising_channel_type, "
            "campaign_budget.amount_micros, campaign_budget.resource_name FROM campaign "
            "WHERE campaign.status != 'REMOVED'"):
        c = x['campaign']
        camp[c['id']] = {'id': c['id'], 'naam': c['name'], 'status': c['status'],
                         'type': c.get('advertisingChannelType'),
                         'budget': int(x['campaignBudget'].get('amountMicros', 0)) / 1e6,
                         'budget_rn': x['campaignBudget']['resourceName'], 'dagen': {}}
    for x in g.search(
            "SELECT campaign.id, segments.date, metrics.cost_micros, metrics.impressions, metrics.clicks, "
            "metrics.conversions, metrics.conversions_value, metrics.search_budget_lost_impression_share, "
            f"metrics.search_impression_share FROM campaign WHERE {periode}"):
        c = camp.get(x['campaign']['id'])
        if not c:
            continue
        c['dagen'][x['segments']['date']] = {
            'kosten': _m(x, 'costMicros') / 1e6, 'vert': _m(x, 'impressions'), 'klik': _m(x, 'clicks'),
            'conv': _m(x, 'conversions'), 'waarde': _m(x, 'conversionsValue'),
            'verlies_budget': _m(x, 'searchBudgetLostImpressionShare'),
            'aandeel': _m(x, 'searchImpressionShare')}
    zw = []
    for x in g.search(
            "SELECT campaign.id, ad_group.id, ad_group_criterion.resource_name, ad_group_criterion.keyword.text, "
            "ad_group_criterion.keyword.match_type, ad_group_criterion.status, ad_group_criterion.cpc_bid_micros, "
            "ad_group_criterion.effective_cpc_bid_micros, metrics.cost_micros, metrics.clicks, metrics.conversions, "
            f"metrics.conversions_value FROM keyword_view WHERE {periode} AND ad_group_criterion.status = 'ENABLED'"):
        k = x['adGroupCriterion']
        zw.append({'campagne': x['campaign']['id'], 'rn': k['resourceName'],
                   'tekst': k['keyword']['text'], 'match': k['keyword']['matchType'],
                   'bod': int(k.get('effectiveCpcBidMicros') or k.get('cpcBidMicros') or 0) / 1e6,
                   'kosten': _m(x, 'costMicros') / 1e6, 'klik': _m(x, 'clicks'), 'conv': _m(x, 'conversions'),
                   'waarde': _m(x, 'conversionsValue')})
    prod = {}
    for x in g.search(
            "SELECT campaign.id, segments.product_item_id, segments.product_title, metrics.cost_micros, "
            f"metrics.clicks, metrics.conversions, metrics.conversions_value FROM shopping_performance_view WHERE {periode}"):
        pid = x['segments'].get('productItemId', '')
        p = prod.setdefault(pid, {'campagne': x['campaign']['id'], 'item': pid,
                                  'titel': x['segments'].get('productTitle', ''),
                                  'kosten': 0.0, 'klik': 0.0, 'conv': 0.0, 'waarde': 0.0})
        p['kosten'] += _m(x, 'costMicros') / 1e6
        p['klik'] += _m(x, 'clicks')
        p['conv'] += _m(x, 'conversions')
        p['waarde'] += _m(x, 'conversionsValue')
    # productgroepen (listing group UNIT op item-ID) met hun bod, om producten te kunnen aanpassen
    for x in g.search(
            "SELECT campaign.id, ad_group_criterion.resource_name, ad_group_criterion.cpc_bid_micros, "
            "ad_group_criterion.listing_group.case_value.product_item_id.value, ad_group_criterion.status, "
            "ad_group_criterion.negative FROM ad_group_criterion WHERE ad_group_criterion.type = 'LISTING_GROUP' "
            "AND ad_group_criterion.listing_group.type = 'UNIT' AND ad_group_criterion.status != 'REMOVED'"):
        k = x['adGroupCriterion']
        item = (k.get('listingGroup', {}).get('caseValue', {}).get('productItemId', {}) or {}).get('value')
        if not item or k.get('negative'):
            continue
        p = prod.setdefault(item.lower(), {'campagne': x['campaign']['id'], 'item': item.lower(), 'titel': '',
                                           'kosten': 0.0, 'klik': 0.0, 'conv': 0.0, 'waarde': 0.0})
        p['rn'] = k['resourceName']
        p['bod'] = int(k.get('cpcBidMicros', 0)) / 1e6
        p['status'] = k.get('status')
    termen = []
    for x in g.search(
            "SELECT campaign.id, search_term_view.search_term, search_term_view.status, metrics.cost_micros, "
            f"metrics.clicks, metrics.impressions, metrics.conversions FROM search_term_view WHERE {periode}"):
        termen.append({'campagne': x['campaign']['id'], 'term': x['searchTermView']['searchTerm'],
                       'status': x['searchTermView'].get('status'), 'kosten': _m(x, 'costMicros') / 1e6,
                       'klik': _m(x, 'clicks'), 'vert': _m(x, 'impressions'), 'conv': _m(x, 'conversions')})
    afgekeurd = []
    for x in g.search(
            "SELECT campaign.name, ad_group_ad.ad.id, ad_group_ad.policy_summary.approval_status "
            "FROM ad_group_ad WHERE ad_group_ad.status = 'ENABLED' AND campaign.status = 'ENABLED'"):
        st = x['adGroupAd'].get('policySummary', {}).get('approvalStatus')
        if st not in ('APPROVED', 'APPROVED_LIMITED', None):
            afgekeurd.append({'campagne': x['campaign']['name'], 'ad': x['adGroupAd']['ad']['id'], 'status': st})
    return {'campagnes': list(camp.values()), 'zoekwoorden': zw, 'producten': list(prod.values()),
            'zoektermen': termen, 'afgekeurd': afgekeurd}


# ---------- Meta ----------

def _meta_get(pad, **q):
    q['access_token'] = E['META_ACCESS_TOKEN']
    out, url = [], META_V + pad
    while url:
        r = requests.get(url, params=q, timeout=TIMEOUT)
        j = r.json()
        if 'error' in j:
            raise RuntimeError('Meta: ' + str(j['error'].get('message'))[:400])
        out += j.get('data', [])
        url, q = j.get('paging', {}).get('next'), {}
    return out


def _actie(lijst, soort):
    for a in lijst or []:
        if a.get('action_type') == soort:
            return float(a.get('value', 0) or 0)
    return 0.0


def meta(van, tot):
    acc = E['META_AD_ACCOUNT_ID']
    acc = acc if acc.startswith('act_') else 'act_' + acc
    adsets = [{'id': s['id'], 'naam': s['name'], 'status': s.get('effective_status'),
               'campagne': s.get('campaign_id'),
               'budget': int(s.get('daily_budget') or 0) / 100}
              for s in _meta_get(acc + '/adsets', fields='id,name,effective_status,campaign_id,daily_budget', limit=200)]
    camps = [{'id': c['id'], 'naam': c['name'], 'status': c.get('effective_status'),
              'budget': int(c.get('daily_budget') or 0) / 100}
             for c in _meta_get(acc + '/campaigns', fields='id,name,effective_status,daily_budget', limit=200)]
    rijen = _meta_get(acc + '/insights', level='ad', time_increment=1,
                      time_range='{"since":"%s","until":"%s"}' % (van, tot),
                      action_attribution_windows='["7d_click","1d_view"]',
                      fields='date_start,campaign_id,campaign_name,adset_id,ad_id,ad_name,spend,impressions,clicks,'
                             'inline_link_clicks,actions,action_values', limit=500)
    ads = {}
    for r in rijen:
        a = ads.setdefault(r['ad_id'], {'id': r['ad_id'], 'naam': r.get('ad_name'), 'adset': r.get('adset_id'),
                                        'campagne': r.get('campaign_id'), 'campagnenaam': r.get('campaign_name'),
                                        'dagen': {}})
        a['dagen'][r['date_start']] = {
            'kosten': float(r.get('spend', 0) or 0), 'vert': float(r.get('impressions', 0) or 0),
            'klik': float(r.get('inline_link_clicks', 0) or 0),
            'video3s': _actie(r.get('actions'), 'video_view'),
            'winkelwagen': _actie(r.get('actions'), 'offsite_conversion.fb_pixel_add_to_cart'),
            'conv': _actie(r.get('actions'), 'offsite_conversion.fb_pixel_purchase'),
            'waarde': _actie(r.get('action_values'), 'offsite_conversion.fb_pixel_purchase')}
    status = {a['id']: a for a in _meta_get(acc + '/ads', fields='id,name,effective_status,adset_id,creative{object_type,video_id}', limit=500)}
    for i, a in ads.items():
        s = status.get(i, {})
        a['status'] = s.get('effective_status')
        a['video'] = bool((s.get('creative') or {}).get('video_id'))
    return {'campagnes': camps, 'adsets': adsets, 'ads': list(ads.values())}


# ---------- Shopify ----------

_shop_tok = None


def _shop_gql(q, v=None):
    global _shop_tok
    if not _shop_tok:
        _shop_tok = requests.post(f'https://{SHOP}/admin/oauth/access_token', data={
            'client_id': E['BLINE_SHOPIFY_CLIENT_ID'], 'client_secret': E['BLINE_SHOPIFY_CLIENT_SECRET'],
            'grant_type': 'client_credentials'}, timeout=30).json()['access_token']
    r = requests.post(f'https://{SHOP}/admin/api/{SHOP_V}/graphql.json', json={'query': q, 'variables': v or {}},
                      headers={'X-Shopify-Access-Token': _shop_tok}, timeout=TIMEOUT).json()
    if r.get('errors'):
        raise RuntimeError('Shopify: ' + str(r['errors'])[:400])
    return r['data']


META_BRONNEN = {'fb', 'ig', 'facebook', 'instagram', 'meta', 'msg', 'an', 'threads'}


def kanaal(bezoek):
    """Betaald kanaal van een bezoek: 'google', 'meta' of 'overig'."""
    if not bezoek:
        return 'overig', None
    utm = bezoek.get('utmParameters') or {}
    bron = (utm.get('source') or '').lower()
    medium = (utm.get('medium') or '').lower()
    pagina = bezoek.get('landingPage') or ''
    if re.search(r'[?&](gclid|gbraid|wbraid)=', pagina) or (bron == 'google' and medium == 'cpc'):
        return 'google', utm.get('campaign')
    if medium == 'paid_social' or (bron in META_BRONNEN and medium in ('paid', 'cpc', 'paid_social')):
        return 'meta', utm.get('campaign')
    return 'overig', None


def shopify(van, tot):
    orders, cursor = [], None
    zoek = f'created_at:>={van} created_at:<={tot}T23:59:59 test:false'
    while True:
        d = _shop_gql('''query($q:String!,$c:String){ orders(first:100, after:$c, query:$q) {
          pageInfo { hasNextPage endCursor }
          nodes { name createdAt test cancelledAt
            totalPriceSet { shopMoney { amount } } totalRefundedSet { shopMoney { amount } }
            customerJourneySummary { lastVisit { source landingPage utmParameters { source medium campaign content term } } }
          } } }''', {'q': zoek, 'c': cursor})['orders']
        for o in d['nodes']:
            if o['test'] or o['cancelledAt']:
                continue
            lv = (o.get('customerJourneySummary') or {}).get('lastVisit')
            k, camp = kanaal(lv)
            utm = (lv or {}).get('utmParameters') or {}
            orders.append({'order': o['name'], 'datum': _lokale_datum(o['createdAt']),
                           'omzet': float(o['totalPriceSet']['shopMoney']['amount']),
                           'terug': float(o['totalRefundedSet']['shopMoney']['amount']),
                           'kanaal': k, 'campagne': camp, 'content': utm.get('content')})
        if not d['pageInfo']['hasNextPage']:
            break
        cursor = d['pageInfo']['endCursor']
    sessies = {}
    q = (f'FROM sessions SHOW sessions, conversion_rate GROUP BY day SINCE {van} UNTIL {tot}')
    t = _shop_gql('query($q:String!){ shopifyqlQuery(query:$q) { tableData { rows } parseErrors } }', {'q': q})
    for r in ((t['shopifyqlQuery'].get('tableData') or {}).get('rows') or []):
        sessies[r['day']] = {'sessies': int(float(r['sessions'] or 0)), 'conversie': float(r['conversion_rate'] or 0)}
    return {'orders': orders, 'sessies': sessies}


def _lokale_datum(iso):
    t = dt.datetime.fromisoformat(iso.replace('Z', '+00:00'))
    try:
        from zoneinfo import ZoneInfo
        return t.astimezone(ZoneInfo('Europe/Amsterdam')).date().isoformat()
    except Exception:
        return (t + dt.timedelta(hours=2)).date().isoformat()


# ---------- Clarity en Klaviyo (aanvullend; fouten stoppen de run niet) ----------

def clarity():
    """Gisteren-tot-nu in Clarity: maximaal 10 aanvragen per dag, dus 1 keer per run."""
    r = requests.get('https://www.clarity.ms/export-data/api/v1/project-live-insights', params={'numOfDays': 1},
                     headers={'Authorization': 'Bearer ' + E['Bline_Clarity']}, timeout=60)
    r.raise_for_status()
    uit = {}
    for m in r.json():
        info = (m.get('information') or [{}])[0]
        if m['metricName'] == 'Traffic':
            uit['sessies'] = info.get('totalSessionCount')
            uit['bots'] = info.get('totalBotSessionCount')
        elif m['metricName'] == 'ScrollDepth':
            uit['scrolldiepte'] = info.get('averageScrollDepth')
        elif 'sessionsWithMetricPercentage' in info:
            uit[m['metricName']] = info.get('sessionsWithMetricPercentage')
    return uit


KLAVIYO_METRICS = {'Viewed Product': 'productweergaven', 'Added to Cart': 'winkelwagens',
                   'Checkout Started': 'checkouts', 'Subscribed to Email Marketing': 'aanmeldingen'}


def klaviyo(van, tot):
    """Trechter per dag uit Klaviyo: productweergaven, winkelwagens, checkouts en aanmeldingen."""
    h = {'Authorization': 'Klaviyo-API-Key ' + E['KLAVIYO_BlineSleep'], 'revision': '2024-10-15',
         'accept': 'application/vnd.api+json', 'content-type': 'application/vnd.api+json'}
    ms = requests.get('https://a.klaviyo.com/api/metrics/', headers=h, timeout=60).json().get('data', [])
    uit = {}
    for naam, sleutel in KLAVIYO_METRICS.items():
        mid = next((m['id'] for m in ms if m['attributes']['name'] == naam), None)
        if not mid:
            continue
        body = {'data': {'type': 'metric-aggregate', 'attributes': {
            'metric_id': mid, 'measurements': ['count'], 'interval': 'day', 'timezone': 'Europe/Amsterdam',
            'filter': [f'greater-or-equal(datetime,{van}T00:00:00)',
                       f'less-than(datetime,{_volgende(tot)}T00:00:00)']}}}
        r = requests.post('https://a.klaviyo.com/api/metric-aggregates/', headers=h, json=body, timeout=60).json()
        a = r.get('data', {}).get('attributes', {})
        tellen = (a.get('data') or [{}])[0].get('measurements', {}).get('count', [])
        for d, n in zip(a.get('dates', []), tellen):
            uit.setdefault(d[:10], {})[sleutel] = int(n)
    return uit


def _volgende(d):
    return (dt.date.fromisoformat(d) + dt.timedelta(days=1)).isoformat()
