/**
 * Bline: Google Ads-campagnes aanmaken in Bline 860-535-9447, alles op PAUZE.
 * Eerst "Voorbeeld" (maakt niets aan), dan "Uitvoeren". Stopt vanzelf als de campagnes al bestaan.
 * Merk €1, Shopping €5, Generiek €4 per dag. De data (zoekwoorden, advertenties, uitsluitingen) komt uit
 * mockups/blinesleep/ads/google/campagnes_data.json in de repo.
 */
var DATA_URL = 'https://raw.githubusercontent.com/joost0070/n8napi/claude/lucid-hopper-Mn8M6/mockups/blinesleep/ads/google/campagnes_data.json';
var DATA;

var BUDGET = { '00 Search | Merk | NL+BE': 1, '02 Search | Generiek | NL+BE': 4, '01 Shopping | Leeskussen | NL+BE': 5 };
var NL = 'geoTargetConstants/2528', BE = 'geoTargetConstants/2056', NEDERLANDS = 'languageConstants/1010';

function main() {
  DATA = JSON.parse(UrlFetchApp.fetch(DATA_URL).getContentText());
  Logger.log('Data geladen: ' + DATA.kw.length + ' zoekwoorden, ' + DATA.ads.length + ' advertenties.');
  var cid = AdsApp.currentAccount().getCustomerId().replace(/-/g, '');
  Logger.log('Account: ' + AdsApp.currentAccount().getName() + ' (' + AdsApp.currentAccount().getCustomerId() + ')');
  if (cid !== '8605359447') { Logger.log('FOUT: dit is niet het account Bline 860-535-9447. Gestopt.'); return; }

  var namen = Object.keys(BUDGET);
  var bestaand = AdsApp.search("SELECT campaign.name FROM campaign WHERE campaign.status != 'REMOVED' AND campaign.name IN ('" + namen.join("','") + "')");
  if (bestaand.hasNext()) { Logger.log('Gestopt: de campagnes bestaan al (' + bestaand.next().campaign.name + ').'); return; }

  var t = 0;
  function tmp() { t -= 1; return t; }
  function rn(type, id) { return 'customers/' + cid + '/' + type + '/' + id; }
  function micros(eur) { return String(Math.round(parseFloat(String(eur).replace(',', '.')) * 1e6)); }
  var ops = [], uitleg = [];
  function op(o, tekst) { ops.push(o); uitleg.push(tekst); }

  var camp = {}, grp = {};
  // Zoekcampagnes
  ['00 Search | Merk | NL+BE', '02 Search | Generiek | NL+BE'].forEach(function (naam) {
    var b = rn('campaignBudgets', tmp()), c = rn('campaigns', tmp());
    camp[naam] = c;
    op({ campaignBudgetOperation: { create: { resourceName: b, name: 'Bline | ' + naam, amountMicros: micros(BUDGET[naam]), deliveryMethod: 'STANDARD', explicitlyShared: false } } }, 'Budget ' + naam);
    op({ campaignOperation: { create: {
      resourceName: c, name: naam, status: 'PAUSED', advertisingChannelType: 'SEARCH', campaignBudget: b,
      manualCpc: { enhancedCpcEnabled: false },
      networkSettings: { targetGoogleSearch: true, targetSearchNetwork: false, targetContentNetwork: false, targetPartnerSearchNetwork: false },
      geoTargetTypeSetting: { positiveGeoTargetType: 'PRESENCE', negativeGeoTargetType: 'PRESENCE' },
      containsEuPoliticalAdvertising: 'DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING'
    } } }, 'Campagne ' + naam);
    [NL, BE].forEach(function (g) { op({ campaignCriterionOperation: { create: { campaign: c, location: { geoTargetConstant: g } } } }, 'Locatie ' + g + ' ' + naam); });
    op({ campaignCriterionOperation: { create: { campaign: c, language: { languageConstant: NEDERLANDS } } } }, 'Taal Nederlands ' + naam);
  });

  DATA.groups.forEach(function (g) {
    var r = rn('adGroups', tmp()); grp[g.c + '|' + g.g] = r;
    op({ adGroupOperation: { create: { resourceName: r, campaign: camp[g.c], name: g.g, status: 'ENABLED', type: 'SEARCH_STANDARD', cpcBidMicros: micros(g.cpc) } } }, 'Advertentiegroep ' + g.c + ' > ' + g.g);
  });

  DATA.kw.forEach(function (k) {
    var crit = { adGroup: grp[k.c + '|' + k.g], status: k.s, keyword: { text: k.t, matchType: k.m } };
    if (k.cpc) crit.cpcBidMicros = micros(k.cpc);
    if (k.u) crit.finalUrls = [k.u];
    op({ adGroupCriterionOperation: { create: crit } }, 'Zoekwoord [' + k.m + '] ' + k.t + (k.s === 'PAUSED' ? ' (pauze)' : ''));
  });

  DATA.ads.forEach(function (a) {
    var rsa = { headlines: a.h, descriptions: a.d };
    if (a.p1) rsa.path1 = a.p1;
    if (a.p2) rsa.path2 = a.p2;
    op({ adGroupAdOperation: { create: { adGroup: grp[a.c + '|' + a.g], status: 'ENABLED', ad: { finalUrls: [a.u], responsiveSearchAd: rsa } } } }, 'Advertentie ' + a.c + ' > ' + a.g);
  });

  var sets = {};
  Object.keys(DATA.neg).forEach(function (naam) {
    var s = rn('sharedSets', tmp()); sets[naam] = s;
    op({ sharedSetOperation: { create: { resourceName: s, name: naam, type: 'NEGATIVE_KEYWORDS' } } }, 'Uitsluitingslijst ' + naam);
    DATA.neg[naam].forEach(function (k) {
      op({ sharedCriterionOperation: { create: { sharedSet: s, keyword: { text: k.t, matchType: k.m } } } }, 'Uitsluiting ' + naam + ': ' + k.t);
    });
  });
  DATA.koppel.forEach(function (k) {
    if (camp[k[1]] && sets[k[0]]) op({ campaignSharedSetOperation: { create: { campaign: camp[k[1]], sharedSet: sets[k[0]] } } }, 'Lijst ' + k[0] + ' aan ' + k[1]);
  });

  DATA.sl.forEach(function (s) {
    var a = rn('assets', tmp());
    op({ assetOperation: { create: { resourceName: a, finalUrls: [s.u], sitelinkAsset: { linkText: s.t, description1: s.d1, description2: s.d2 } } } }, 'Sitelink ' + s.t);
    op({ campaignAssetOperation: { create: { campaign: camp[s.c], asset: a, fieldType: 'SITELINK' } } }, 'Sitelink aan ' + s.c);
  });
  DATA.co.forEach(function (c) {
    var a = rn('assets', tmp());
    op({ assetOperation: { create: { resourceName: a, calloutAsset: { calloutText: c.t } } } }, 'Highlight ' + c.t);
    op({ campaignAssetOperation: { create: { campaign: camp[c.c], asset: a, fieldType: 'CALLOUT' } } }, 'Highlight aan ' + c.c);
  });
  DATA.sn.forEach(function (s) {
    var a = rn('assets', tmp());
    op({ assetOperation: { create: { resourceName: a, structuredSnippetAsset: { header: s.h, values: s.v } } } }, 'Fragment ' + s.h);
    op({ campaignAssetOperation: { create: { campaign: camp[s.c], asset: a, fieldType: 'STRUCTURED_SNIPPET' } } }, 'Fragment aan ' + s.c);
  });

  // Shopping
  var sNaam = '01 Shopping | Leeskussen | NL+BE';
  var sb = rn('campaignBudgets', tmp()), sc = rn('campaigns', tmp()), sg = rn('adGroups', tmp());
  var sgId = sg.split('/').pop();
  op({ campaignBudgetOperation: { create: { resourceName: sb, name: 'Bline | ' + sNaam, amountMicros: micros(BUDGET[sNaam]), deliveryMethod: 'STANDARD', explicitlyShared: false } } }, 'Budget ' + sNaam);
  op({ campaignOperation: { create: {
    resourceName: sc, name: sNaam, status: 'PAUSED', advertisingChannelType: 'SHOPPING', campaignBudget: sb,
    manualCpc: { enhancedCpcEnabled: false },
    shoppingSetting: { merchantId: DATA.shopping.merchantId, campaignPriority: 0, enableLocal: false },
    networkSettings: { targetGoogleSearch: true, targetSearchNetwork: false, targetContentNetwork: false },
    geoTargetTypeSetting: { positiveGeoTargetType: 'PRESENCE', negativeGeoTargetType: 'PRESENCE' },
    containsEuPoliticalAdvertising: 'DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING'
  } } }, 'Campagne ' + sNaam);
  op({ campaignCriterionOperation: { create: { campaign: sc, location: { geoTargetConstant: NL } } } }, 'Locatie NL Shopping');
  op({ campaignCriterionOperation: { create: { campaign: sc, location: { geoTargetConstant: BE }, bidModifier: 0.9 } } }, 'Locatie BE Shopping (-10%)');
  op({ adGroupOperation: { create: { resourceName: sg, campaign: sc, name: 'Leeskussens', status: 'ENABLED', type: 'SHOPPING_PRODUCT_ADS', cpcBidMicros: micros(0.45) } } }, 'Advertentiegroep Leeskussens');
  op({ adGroupAdOperation: { create: { adGroup: sg, status: 'ENABLED', ad: { shoppingProductAd: {} } } } }, 'Shopping-advertentie');
  var root = rn('adGroupCriteria', sgId + '~' + tmp());
  op({ adGroupCriterionOperation: { create: { resourceName: root, adGroup: sg, status: 'ENABLED', listingGroup: { type: 'SUBDIVISION' } } } }, 'Productgroep: alle producten (op item-ID)');
  DATA.shopping.items.forEach(function (it) {
    op({ adGroupCriterionOperation: { create: { adGroup: sg, status: 'ENABLED', cpcBidMicros: micros(it[2]),
      listingGroup: { type: 'UNIT', parentAdGroupCriterion: root, caseValue: { productItemId: { value: it[0] } } } } } }, 'Product ' + it[1] + ' bod €' + it[2]);
  });
  op({ adGroupCriterionOperation: { create: { adGroup: sg, status: 'ENABLED', negative: true,
    listingGroup: { type: 'UNIT', parentAdGroupCriterion: root, caseValue: { productItemId: {} } } } } }, 'Overige producten (hoezen, sets) uitgesloten');

  Logger.log(ops.length + ' wijzigingen klaar om te versturen.');
  var res = AdsApp.mutateAll(ops, { partialFailure: true });
  var ok = 0, fout = 0;
  for (var i = 0; i < res.length; i++) {
    if (res[i].isSuccessful()) ok++;
    else { fout++; Logger.log('FOUT ' + uitleg[i] + ': ' + res[i].getErrorMessages().join('; ')); }
  }
  Logger.log('Klaar: ' + ok + ' gelukt, ' + fout + ' fout. Alle campagnes staan op PAUZE.');
}
