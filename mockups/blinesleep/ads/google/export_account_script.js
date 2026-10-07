/**
 * Google Ads-script: exporteert de opzet en resultaten van één account naar een nieuwe Google Sheet.
 * Gebruik: Google Ads > Tools > Bulkacties > Scripts > + > plak dit script > Autoriseren > Uitvoeren.
 * Alleen lezen: het script verandert niets in het account.
 * Na afloop staat de link naar de sheet onderaan bij "Logboeken".
 */
var VAN = '2017-01-01';

var QUERIES = [
  ['Campagnes',
    "SELECT campaign.id, campaign.name, campaign.status, campaign.advertising_channel_type, campaign.bidding_strategy_type, " +
    "campaign.start_date, campaign_budget.amount_micros, metrics.cost_micros, metrics.clicks, metrics.impressions, metrics.ctr, " +
    "metrics.average_cpc, metrics.conversions, metrics.conversions_value FROM campaign WHERE segments.date BETWEEN '{VAN}' AND '{TOT}'"],
  ['Biedstrategie',
    "SELECT campaign.name, campaign.bidding_strategy_type, campaign.maximize_conversion_value.target_roas, " +
    "campaign.target_roas.target_roas, campaign.maximize_conversions.target_cpa_micros FROM campaign"],
  ['Advertentiegroepen',
    "SELECT campaign.name, ad_group.name, ad_group.status, ad_group.type, metrics.cost_micros, metrics.clicks, metrics.impressions, " +
    "metrics.conversions, metrics.conversions_value FROM ad_group WHERE segments.date BETWEEN '{VAN}' AND '{TOT}'"],
  ['Zoekwoorden',
    "SELECT campaign.name, ad_group.name, ad_group_criterion.keyword.text, ad_group_criterion.keyword.match_type, " +
    "ad_group_criterion.status, metrics.cost_micros, metrics.clicks, metrics.impressions, metrics.conversions, metrics.conversions_value " +
    "FROM keyword_view WHERE segments.date BETWEEN '{VAN}' AND '{TOT}'"],
  ['Uitsluitingen campagne',
    "SELECT campaign.name, campaign_criterion.keyword.text, campaign_criterion.keyword.match_type FROM campaign_criterion " +
    "WHERE campaign_criterion.negative = TRUE AND campaign_criterion.type = KEYWORD"],
  ['Uitsluitingen lijsten',
    "SELECT shared_set.name, shared_criterion.keyword.text, shared_criterion.keyword.match_type FROM shared_criterion " +
    "WHERE shared_criterion.type = KEYWORD"],
  ['Advertenties',
    "SELECT campaign.name, ad_group.name, ad_group_ad.status, ad_group_ad.ad.type, ad_group_ad.ad.final_urls, " +
    "ad_group_ad.ad.responsive_search_ad.headlines, ad_group_ad.ad.responsive_search_ad.descriptions, " +
    "metrics.cost_micros, metrics.clicks, metrics.impressions, metrics.conversions FROM ad_group_ad " +
    "WHERE segments.date BETWEEN '{VAN}' AND '{TOT}'"],
  ['PMax-groepen',
    "SELECT campaign.name, asset_group.name, asset_group.status, asset_group.final_urls FROM asset_group"],
  ['PMax-onderdelen',
    "SELECT campaign.name, asset_group.name, asset_group_asset.field_type, asset_group_asset.status, asset.type, " +
    "asset.text_asset.text, asset.image_asset.full_size.url, asset.youtube_video_asset.youtube_video_id FROM asset_group_asset"],
  ['Zoektermen',
    "SELECT campaign.name, search_term_view.search_term, metrics.cost_micros, metrics.clicks, metrics.impressions, " +
    "metrics.conversions, metrics.conversions_value FROM search_term_view WHERE segments.date BETWEEN '{VAN}' AND '{TOT}'"],
  ['Producten',
    "SELECT campaign.name, segments.product_item_id, segments.product_title, metrics.cost_micros, metrics.clicks, " +
    "metrics.impressions, metrics.conversions, metrics.conversions_value FROM shopping_performance_view " +
    "WHERE segments.date BETWEEN '{VAN}' AND '{TOT}'"],
  ['Apparaten',
    "SELECT campaign.name, segments.device, metrics.cost_micros, metrics.clicks, metrics.impressions, metrics.conversions " +
    "FROM campaign WHERE segments.date BETWEEN '{VAN}' AND '{TOT}'"],
  ['Per maand',
    "SELECT segments.month, campaign.name, metrics.cost_micros, metrics.clicks, metrics.impressions, metrics.conversions, " +
    "metrics.conversions_value FROM campaign WHERE segments.date BETWEEN '{VAN}' AND '{TOT}'"],
  ['Conversieacties',
    "SELECT conversion_action.name, conversion_action.type, conversion_action.status, conversion_action.category, " +
    "conversion_action.primary_for_goal, conversion_action.counting_type FROM conversion_action"],
  ['Doelgroepen',
    "SELECT campaign.name, ad_group.name, ad_group_criterion.type, ad_group_criterion.display_name, ad_group_criterion.negative " +
    "FROM ad_group_criterion WHERE ad_group_criterion.type IN ('USER_LIST', 'USER_INTEREST', 'CUSTOM_AUDIENCE', 'AGE_RANGE', 'GENDER')"]
];

function main() {
  var tot = Utilities.formatDate(new Date(), AdsApp.currentAccount().getTimeZone(), 'yyyy-MM-dd');
  var naam = AdsApp.currentAccount().getName() + ' export ' + tot;
  var sheet = SpreadsheetApp.create(naam);
  var eerste = sheet.getSheets()[0];
  var samenvatting = [['Tabblad', 'Rijen', 'Opmerking']];

  QUERIES.forEach(function (q) {
    var titel = q[0];
    var gaql = q[1].replace('{VAN}', VAN).replace('{TOT}', tot);
    try {
      var rijen = [];
      var kolommen = {};
      var it = AdsApp.search(gaql);
      while (it.hasNext() && rijen.length < 50000) {
        var plat = {};
        plat_maken(it.next(), '', plat);
        Object.keys(plat).forEach(function (k) { kolommen[k] = true; });
        rijen.push(plat);
      }
      var kop = Object.keys(kolommen);
      var tab = sheet.insertSheet(titel);
      if (rijen.length) {
        var waarden = [kop].concat(rijen.map(function (r) { return kop.map(function (k) { return r[k] === undefined ? '' : r[k]; }); }));
        tab.getRange(1, 1, waarden.length, kop.length).setValues(waarden);
        tab.setFrozenRows(1);
      } else {
        tab.getRange(1, 1).setValue('Geen gegevens');
      }
      samenvatting.push([titel, rijen.length, '']);
    } catch (e) {
      // een onderdeel dat dit account niet heeft (bijv. geen Shopping) slaan we over
      samenvatting.push([titel, 0, 'overgeslagen: ' + String(e).slice(0, 200)]);
    }
  });

  eerste.setName('Samenvatting');
  eerste.getRange(1, 1, samenvatting.length, 3).setValues(samenvatting);
  Logger.log('Klaar. Open de sheet: ' + sheet.getUrl());
}

// zet een geneste rij om naar kolommen; bedragen in micros worden euro's, lijsten worden tekst
function plat_maken(obj, voor, uit) {
  Object.keys(obj).forEach(function (k) {
    var v = obj[k];
    var sleutel = voor ? voor + '.' + k : k;
    if (v === null || v === undefined) return;
    if (Array.isArray(v)) {
      uit[sleutel] = v.map(function (x) { return (x && typeof x === 'object') ? (x.text || JSON.stringify(x)) : x; }).join(' | ');
    } else if (typeof v === 'object') {
      plat_maken(v, sleutel, uit);
    } else if (/Micros$/.test(k)) {
      uit[sleutel.replace(/Micros$/, '')] = Number(v) / 1e6;
    } else {
      uit[sleutel] = v;
    }
  });
}
