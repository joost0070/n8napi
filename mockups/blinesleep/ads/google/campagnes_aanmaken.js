/**
 * Bline: Google Ads-campagnes aanmaken, alles op PAUZE.
 * Account: Bline 860-535-9447. Er wordt niets uitgegeven tot je zelf een campagne aanzet.
 *
 * Gebruik: Google Ads > Tools > Bulkacties > Scripts > + > plak dit script > Autoriseren.
 * 1. Klik eerst op "Voorbeeld": er wordt dan niets aangemaakt, je ziet in "Logboeken" wat het script zou doen.
 * 2. Staat er onderaan "Klaar" zonder FOUT-regels, klik dan op "Uitvoeren".
 * Het script stopt vanzelf als de campagnes al bestaan, dus twee keer draaien maakt geen dubbele campagnes.
 *
 * Wat het aanmaakt:
 * - 00 Search | Merk | NL+BE       budget €1 per dag, handmatige CPC
 * - 01 Shopping | Leeskussen | NL+BE  budget €5 per dag, handmatige CPC per kleur (wit €0,40, andere kleuren €0,45),
 *                                      België 10% lager, hoezen en sets uitgesloten
 * - 02 Search | Generiek | NL+BE   budget €4 per dag, handmatige CPC per groep
 * Met zoekwoorden (prioriteit 1 aan, prioriteit 2 op pauze voor later), advertenties, uitsluitingslijsten,
 * sitelinks, highlights en fragmenten. Doel: alleen de aankoopactie van de Shopify-app telt (staat al zo).
 */
var DATA = {
 "groups": [
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Merk",
   "cpc": "0.30"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Hoes",
   "cpc": "0.30"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen",
   "cpc": "0.50"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bed",
   "cpc": "0.50"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bank en zetel",
   "cpc": "0.45"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "cpc": "0.45"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bank en zetel",
   "cpc": "0.35"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "cpc": "0.40"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rechtop zitten in bed",
   "cpc": "0.40"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Lezen en tv in bed",
   "cpc": "0.35"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kenmerken",
   "cpc": "0.40"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kleuren",
   "cpc": "0.40"
  }
 ],
 "kw": [
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Merk",
   "t": "bline leeskussen",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Merk",
   "t": "bline leeskussen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Merk",
   "t": "bline",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Merk",
   "t": "blinesleep",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Merk",
   "t": "blinesleep",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Merk",
   "t": "bline sleep",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Merk",
   "t": "bline sleep",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Merk",
   "t": "bline kussen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Hoes",
   "t": "bline leeskussen hoes",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Hoes",
   "t": "bline leeskussen hoes",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Hoes",
   "t": "bline hoes",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen",
   "t": "leeskussen",
   "m": "EXACT",
   "cpc": "0.55",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen",
   "t": "leeskussens",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen",
   "t": "leeskussen kopen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bed",
   "t": "leeskussen bed",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bed",
   "t": "leeskussen bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bed",
   "t": "leeskussen voor in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bed",
   "t": "leeskussen in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bank en zetel",
   "t": "leeskussen bank",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bank en zetel",
   "t": "leeskussen voor bank",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bank en zetel",
   "t": "leeskussen voor op de bank",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bank en zetel",
   "t": "leeskussen voor in bed en bank",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bank en zetel",
   "t": "leeskussen zetel",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "rugkussen bed",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "rugkussen bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "rugkussen voor in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "rugkussen in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "rugkussen bed lezen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "rugkussen leeskussen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "rugsteun bed",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "rugsteun voor in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "rugsteun in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "rugsteun kussen bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "rugsteun kussen voor in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "rugsteun bed lezen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rechtop zitten in bed",
   "t": "kussen om rechtop te zitten in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rechtop zitten in bed",
   "t": "kussen om in bed te zitten",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rechtop zitten in bed",
   "t": "kussen rechtop zitten bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rechtop zitten in bed",
   "t": "kussen om rechtop in bed te zitten",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kenmerken",
   "t": "leeskussen traagschuim",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "ENABLED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Merk",
   "t": "bline leeskussen review",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Merk",
   "t": "bline ervaringen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Hoes",
   "t": "slopen voor bline leeskussen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen",
   "t": "lees kussen",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen",
   "t": "leeskussen volwassenen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen",
   "t": "leeskussen voor volwassenen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen",
   "t": "groot leeskussen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bed",
   "t": "leeskussen voor op bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bed",
   "t": "leeskussen voor bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bed",
   "t": "bed leeskussen",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bed",
   "t": "groot leeskussen bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bed",
   "t": "leeskussen bed rugkussen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bank en zetel",
   "t": "leeskussen bed bank",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bank en zetel",
   "t": "leeskussen voor zetel",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "rugkussen op bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "rugkussen voor bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "bed rugkussen",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "groot rugkussen bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "stevig rugkussen bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "rugkussen bed bank",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "rugkussen voor in bed en bank",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "driehoekig rugkussen bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "t": "rugkussen driehoek",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bank en zetel",
   "t": "rugkussen bank",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bank en zetel",
   "t": "rugkussen voor op de bank",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bank en zetel",
   "t": "rugkussen zetel",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bank en zetel",
   "t": "rugkussen voor in de zetel",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "rugsteun op bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "bed rugsteun",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "ruggesteun in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "ruggesteun bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "rug steun voor in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "rugleuning bed kussen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "rugleuning voor in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "t": "rugsteun bed kopen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rechtop zitten in bed",
   "t": "kussen voor rechtop zitten in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rechtop zitten in bed",
   "t": "zitkussen bed",
   "m": "EXACT",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rechtop zitten in bed",
   "t": "zitkussen voor in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Lezen en tv in bed",
   "t": "kussen om te lezen in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Lezen en tv in bed",
   "t": "kussen om te lezen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Lezen en tv in bed",
   "t": "kussen voor lezen in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Lezen en tv in bed",
   "t": "lezen in bed kussen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Lezen en tv in bed",
   "t": "kussen om boek te lezen in bed",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Lezen en tv in bed",
   "t": "tv kijken in bed kussen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kenmerken",
   "t": "leeskussen memory foam",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kenmerken",
   "t": "rugkussen traagschuim",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kenmerken",
   "t": "leeskussen stevig",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kenmerken",
   "t": "leeskussen katoen",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kenmerken",
   "t": "leeskussen met vak",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kenmerken",
   "t": "leeskussen met opbergvak",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kenmerken",
   "t": "leeskussen afneembare hoes",
   "m": "PHRASE",
   "cpc": "",
   "u": "",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kleuren",
   "t": "leeskussen wit",
   "m": "PHRASE",
   "cpc": "",
   "u": "https://blinesleep.nl/products/leeskussen-wit",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kleuren",
   "t": "leeskussen beige",
   "m": "PHRASE",
   "cpc": "",
   "u": "https://blinesleep.nl/products/leeskussen-beige",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kleuren",
   "t": "leeskussen blauw",
   "m": "PHRASE",
   "cpc": "",
   "u": "https://blinesleep.nl/products/leeskussen-blauw",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kleuren",
   "t": "leeskussen grijs",
   "m": "PHRASE",
   "cpc": "",
   "u": "https://blinesleep.nl/products/leeskussen-grijs",
   "s": "PAUSED"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kleuren",
   "t": "leeskussen zwart",
   "m": "PHRASE",
   "cpc": "",
   "u": "https://blinesleep.nl/products/leeskussen-zwart",
   "s": "PAUSED"
  }
 ],
 "ads": [
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Merk",
   "u": "https://blinesleep.nl/",
   "p1": "leeskussen",
   "p2": "bline",
   "h": [
    {
     "text": "Bline leeskussen",
     "pinnedField": "HEADLINE_1"
    },
    {
     "text": "Officiële webshop van Bline",
     "pinnedField": "HEADLINE_1"
    },
    {
     "text": "Eén kussen dat blijft staan"
    },
    {
     "text": "Koel katoen, geen fluweel"
    },
    {
     "text": "Hoes eraf, in de was"
    },
    {
     "text": "Kleuren die bij je bed passen"
    },
    {
     "text": "Armen vrij, geen armleuningen"
    },
    {
     "text": "3,8 kg stevig traagschuim"
    },
    {
     "text": "Met vak voor je telefoon"
    },
    {
     "text": "Gratis verzending NL en BE"
    },
    {
     "text": "30 dagen proberen"
    },
    {
     "text": "In 1-2 werkdagen in huis"
    },
    {
     "text": "4,5 uit 5 op bol.com"
    },
    {
     "text": "Een Nederlands merk uit Borne"
    },
    {
     "text": "Betaal met iDEAL of Bancontact"
    }
   ],
   "d": [
    {
     "text": "Het leeskussen van Bline: stevig traagschuim, vak voor je telefoon en een wasbare hoes."
    },
    {
     "text": "Koel katoen 400 TC, geen fluweel. Hoes eraf met de rits en op 30 °C in de was."
    },
    {
     "text": "Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis."
    },
    {
     "text": "Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice."
    }
   ]
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "g": "Hoes",
   "u": "https://blinesleep.nl/products/hoes-beige",
   "p1": "hoes",
   "p2": "bline",
   "h": [
    {
     "text": "Hoes voor je Bline leeskussen"
    },
    {
     "text": "Bline leeskussen hoes"
    },
    {
     "text": "Losse hoes vanaf €29,99"
    },
    {
     "text": "Extra hoes voor de wasdag"
    },
    {
     "text": "Eén in de was, één in gebruik"
    },
    {
     "text": "Katoen 400 TC met rits"
    },
    {
     "text": "Koel katoen, geen fluweel"
    },
    {
     "text": "Wasbaar op 30 °C"
    },
    {
     "text": "Hoes in 5 kleuren"
    },
    {
     "text": "Wissel van kleur"
    },
    {
     "text": "Past op elk Bline leeskussen"
    },
    {
     "text": "Hoes eraf, in de was"
    },
    {
     "text": "Gratis verzending NL en BE"
    },
    {
     "text": "30 dagen proberen"
    },
    {
     "text": "In 1-2 werkdagen in huis"
    }
   ],
   "d": [
    {
     "text": "Losse hoes voor het Bline leeskussen. Katoen 400 TC met rits, wasbaar op 30 °C."
    },
    {
     "text": "In wit, beige, blauw, grijs en zwart. Handig als de andere hoes in de was zit."
    },
    {
     "text": "Wit €29,99, andere kleuren €34,99. Gratis verzending in Nederland en België."
    },
    {
     "text": "Binnen 1-2 werkdagen in huis en 30 dagen proberen. Koel katoen in plaats van fluweel."
    }
   ]
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen",
   "u": "https://blinesleep.nl/products/leeskussen-beige",
   "p1": "leeskussen",
   "p2": "5-kleuren",
   "h": [
    {
     "text": "Leeskussen voor bed en bank"
    },
    {
     "text": "Leeskussen kopen"
    },
    {
     "text": "Vanaf €69,99"
    },
    {
     "text": "Bline leeskussen"
    },
    {
     "text": "Eén kussen dat blijft staan"
    },
    {
     "text": "Koel katoen, geen fluweel"
    },
    {
     "text": "Hoes eraf, in de was"
    },
    {
     "text": "Kleuren die bij je bed passen"
    },
    {
     "text": "Armen vrij, geen armleuningen"
    },
    {
     "text": "3,8 kg stevig traagschuim"
    },
    {
     "text": "Met vak voor je telefoon"
    },
    {
     "text": "Gratis verzending NL en BE"
    },
    {
     "text": "30 dagen proberen"
    },
    {
     "text": "In 1-2 werkdagen in huis"
    },
    {
     "text": "4,5 uit 5 op bol.com"
    }
   ],
   "d": [
    {
     "text": "Eén leeskussen dat blijft staan als je leunt. 3,8 kg traagschuim, vak voor je telefoon."
    },
    {
     "text": "Koel katoen 400 TC, geen fluweel. Hoes eraf met de rits en op 30 °C in de was."
    },
    {
     "text": "Geen armleuningen, dus je armen blijven vrij. Vijf rustige kleuren die bij je bed passen."
    },
    {
     "text": "Gratis verzending in NL en BE, in 1-2 werkdagen in huis. 30 dagen proberen."
    }
   ]
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bed",
   "u": "https://blinesleep.nl/products/leeskussen-beige",
   "p1": "leeskussen",
   "p2": "bed",
   "h": [
    {
     "text": "Leeskussen voor in bed"
    },
    {
     "text": "Rechtop lezen in bed"
    },
    {
     "text": "Geen stapel kussens meer"
    },
    {
     "text": "Bline leeskussen"
    },
    {
     "text": "Eén kussen dat blijft staan"
    },
    {
     "text": "Koel katoen, geen fluweel"
    },
    {
     "text": "Hoes eraf, in de was"
    },
    {
     "text": "Kleuren die bij je bed passen"
    },
    {
     "text": "Armen vrij, geen armleuningen"
    },
    {
     "text": "3,8 kg stevig traagschuim"
    },
    {
     "text": "Met vak voor je telefoon"
    },
    {
     "text": "Gratis verzending NL en BE"
    },
    {
     "text": "30 dagen proberen"
    },
    {
     "text": "In 1-2 werkdagen in huis"
    },
    {
     "text": "4,5 uit 5 op bol.com"
    }
   ],
   "d": [
    {
     "text": "Zit rechtop in bed met een boek of een serie. Stevig traagschuim dat niet wegzakt."
    },
    {
     "text": "Koel katoen 400 TC, geen fluweel. Hoes eraf met de rits en op 30 °C in de was."
    },
    {
     "text": "Geen armleuningen, dus je armen blijven vrij. Vijf rustige kleuren die bij je bed passen."
    },
    {
     "text": "Gratis verzending in NL en BE, in 1-2 werkdagen in huis. 30 dagen proberen."
    }
   ]
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Leeskussen bank en zetel",
   "u": "https://blinesleep.nl/products/leeskussen-beige",
   "p1": "leeskussen",
   "p2": "bank",
   "h": [
    {
     "text": "Leeskussen voor de bank"
    },
    {
     "text": "Leeskussen voor bed en zetel"
    },
    {
     "text": "Voor bank, zetel en bed"
    },
    {
     "text": "Bline leeskussen"
    },
    {
     "text": "Eén kussen dat blijft staan"
    },
    {
     "text": "Koel katoen, geen fluweel"
    },
    {
     "text": "Hoes eraf, in de was"
    },
    {
     "text": "Kleuren die bij je bed passen"
    },
    {
     "text": "Armen vrij, geen armleuningen"
    },
    {
     "text": "3,8 kg stevig traagschuim"
    },
    {
     "text": "Met vak voor je telefoon"
    },
    {
     "text": "Gratis verzending NL en BE"
    },
    {
     "text": "30 dagen proberen"
    },
    {
     "text": "In 1-2 werkdagen in huis"
    },
    {
     "text": "4,5 uit 5 op bol.com"
    }
   ],
   "d": [
    {
     "text": "Leeskussen voor bank, zetel en bed. Stevig traagschuim met vak voor je telefoon."
    },
    {
     "text": "Koel katoen 400 TC, geen fluweel. Hoes eraf met de rits en op 30 °C in de was."
    },
    {
     "text": "Geen armleuningen, dus je armen blijven vrij. Vijf rustige kleuren die bij je bed passen."
    },
    {
     "text": "Gratis verzending in NL en BE, in 1-2 werkdagen in huis. 30 dagen proberen."
    }
   ]
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bed",
   "u": "https://blinesleep.nl/products/leeskussen-beige",
   "p1": "rugkussen",
   "p2": "bed",
   "h": [
    {
     "text": "Rugkussen voor in bed"
    },
    {
     "text": "Stevig rugkussen voor bed"
    },
    {
     "text": "Rugkussen van traagschuim"
    },
    {
     "text": "Bline leeskussen"
    },
    {
     "text": "Eén kussen dat blijft staan"
    },
    {
     "text": "Koel katoen, geen fluweel"
    },
    {
     "text": "Hoes eraf, in de was"
    },
    {
     "text": "Kleuren die bij je bed passen"
    },
    {
     "text": "Armen vrij, geen armleuningen"
    },
    {
     "text": "3,8 kg stevig traagschuim"
    },
    {
     "text": "Met vak voor je telefoon"
    },
    {
     "text": "Gratis verzending NL en BE"
    },
    {
     "text": "30 dagen proberen"
    },
    {
     "text": "In 1-2 werkdagen in huis"
    },
    {
     "text": "4,5 uit 5 op bol.com"
    }
   ],
   "d": [
    {
     "text": "Rugkussen voor in bed van 3,8 kg traagschuim. Blijft staan als je ertegen leunt."
    },
    {
     "text": "Koel katoen 400 TC, geen fluweel. Hoes eraf met de rits en op 30 °C in de was."
    },
    {
     "text": "Geen armleuningen, dus je armen blijven vrij. Vijf rustige kleuren die bij je bed passen."
    },
    {
     "text": "Gratis verzending in NL en BE, in 1-2 werkdagen in huis. 30 dagen proberen."
    }
   ]
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugkussen bank en zetel",
   "u": "https://blinesleep.nl/products/leeskussen-beige",
   "p1": "rugkussen",
   "p2": "bank",
   "h": [
    {
     "text": "Rugkussen voor de bank"
    },
    {
     "text": "Rugkussen voor bank en zetel"
    },
    {
     "text": "Los rugkussen, 65 x 50 x 45"
    },
    {
     "text": "Bline leeskussen"
    },
    {
     "text": "Eén kussen dat blijft staan"
    },
    {
     "text": "Koel katoen, geen fluweel"
    },
    {
     "text": "Hoes eraf, in de was"
    },
    {
     "text": "Kleuren die bij je bed passen"
    },
    {
     "text": "Armen vrij, geen armleuningen"
    },
    {
     "text": "3,8 kg stevig traagschuim"
    },
    {
     "text": "Met vak voor je telefoon"
    },
    {
     "text": "Gratis verzending NL en BE"
    },
    {
     "text": "30 dagen proberen"
    },
    {
     "text": "In 1-2 werkdagen in huis"
    },
    {
     "text": "4,5 uit 5 op bol.com"
    }
   ],
   "d": [
    {
     "text": "Los rugkussen voor bank, zetel of bed. Met vak voor je telefoon en een wasbare hoes."
    },
    {
     "text": "Koel katoen 400 TC, geen fluweel. Hoes eraf met de rits en op 30 °C in de was."
    },
    {
     "text": "Geen armleuningen, dus je armen blijven vrij. Vijf rustige kleuren die bij je bed passen."
    },
    {
     "text": "Gratis verzending in NL en BE, in 1-2 werkdagen in huis. 30 dagen proberen."
    }
   ]
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rugsteun bed",
   "u": "https://blinesleep.nl/products/leeskussen-beige",
   "p1": "rugsteun",
   "p2": "bed",
   "h": [
    {
     "text": "Rugsteun voor in bed"
    },
    {
     "text": "Kussen als rugsteun in bed"
    },
    {
     "text": "Geen frame, geen stekker"
    },
    {
     "text": "Bline leeskussen"
    },
    {
     "text": "Eén kussen dat blijft staan"
    },
    {
     "text": "Koel katoen, geen fluweel"
    },
    {
     "text": "Hoes eraf, in de was"
    },
    {
     "text": "Kleuren die bij je bed passen"
    },
    {
     "text": "Armen vrij, geen armleuningen"
    },
    {
     "text": "3,8 kg stevig traagschuim"
    },
    {
     "text": "Met vak voor je telefoon"
    },
    {
     "text": "Gratis verzending NL en BE"
    },
    {
     "text": "30 dagen proberen"
    },
    {
     "text": "In 1-2 werkdagen in huis"
    },
    {
     "text": "4,5 uit 5 op bol.com"
    }
   ],
   "d": [
    {
     "text": "Kussen als rugsteun in bed, van stevig traagschuim. Geen frame en geen stekker nodig."
    },
    {
     "text": "Koel katoen 400 TC, geen fluweel. Hoes eraf met de rits en op 30 °C in de was."
    },
    {
     "text": "Geen armleuningen, dus je armen blijven vrij. Vijf rustige kleuren die bij je bed passen."
    },
    {
     "text": "Gratis verzending in NL en BE, in 1-2 werkdagen in huis. 30 dagen proberen."
    }
   ]
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Rechtop zitten in bed",
   "u": "https://blinesleep.nl/products/leeskussen-beige",
   "p1": "rechtop-zitten",
   "p2": "bed",
   "h": [
    {
     "text": "Rechtop zitten in bed"
    },
    {
     "text": "Kussen om rechtop te zitten"
    },
    {
     "text": "Zit rechtop met een boek"
    },
    {
     "text": "Bline leeskussen"
    },
    {
     "text": "Eén kussen dat blijft staan"
    },
    {
     "text": "Koel katoen, geen fluweel"
    },
    {
     "text": "Hoes eraf, in de was"
    },
    {
     "text": "Kleuren die bij je bed passen"
    },
    {
     "text": "Armen vrij, geen armleuningen"
    },
    {
     "text": "3,8 kg stevig traagschuim"
    },
    {
     "text": "Met vak voor je telefoon"
    },
    {
     "text": "Gratis verzending NL en BE"
    },
    {
     "text": "30 dagen proberen"
    },
    {
     "text": "In 1-2 werkdagen in huis"
    },
    {
     "text": "4,5 uit 5 op bol.com"
    }
   ],
   "d": [
    {
     "text": "Kussen om rechtop te zitten in bed of op de bank. Houdt zijn vorm als je leunt."
    },
    {
     "text": "Koel katoen 400 TC, geen fluweel. Hoes eraf met de rits en op 30 °C in de was."
    },
    {
     "text": "Geen armleuningen, dus je armen blijven vrij. Vijf rustige kleuren die bij je bed passen."
    },
    {
     "text": "Gratis verzending in NL en BE, in 1-2 werkdagen in huis. 30 dagen proberen."
    }
   ]
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Lezen en tv in bed",
   "u": "https://blinesleep.nl/products/leeskussen-beige",
   "p1": "lezen",
   "p2": "bed",
   "h": [
    {
     "text": "Lezen of tv kijken in bed"
    },
    {
     "text": "Kussen om te lezen in bed"
    },
    {
     "text": "Voor boek, serie en laptop"
    },
    {
     "text": "Bline leeskussen"
    },
    {
     "text": "Eén kussen dat blijft staan"
    },
    {
     "text": "Koel katoen, geen fluweel"
    },
    {
     "text": "Hoes eraf, in de was"
    },
    {
     "text": "Kleuren die bij je bed passen"
    },
    {
     "text": "Armen vrij, geen armleuningen"
    },
    {
     "text": "3,8 kg stevig traagschuim"
    },
    {
     "text": "Met vak voor je telefoon"
    },
    {
     "text": "Gratis verzending NL en BE"
    },
    {
     "text": "30 dagen proberen"
    },
    {
     "text": "In 1-2 werkdagen in huis"
    },
    {
     "text": "4,5 uit 5 op bol.com"
    }
   ],
   "d": [
    {
     "text": "Voor lezen, series of even werken in bed. Met vak voor telefoon, bril of e-reader."
    },
    {
     "text": "Koel katoen 400 TC, geen fluweel. Hoes eraf met de rits en op 30 °C in de was."
    },
    {
     "text": "Geen armleuningen, dus je armen blijven vrij. Vijf rustige kleuren die bij je bed passen."
    },
    {
     "text": "Gratis verzending in NL en BE, in 1-2 werkdagen in huis. 30 dagen proberen."
    }
   ]
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kenmerken",
   "u": "https://blinesleep.nl/products/leeskussen-beige",
   "p1": "leeskussen",
   "p2": "traagschuim",
   "h": [
    {
     "text": "Leeskussen van traagschuim"
    },
    {
     "text": "Hoes van katoen 400 TC"
    },
    {
     "text": "Zijvak voor je telefoon"
    },
    {
     "text": "Bline leeskussen"
    },
    {
     "text": "Eén kussen dat blijft staan"
    },
    {
     "text": "Koel katoen, geen fluweel"
    },
    {
     "text": "Hoes eraf, in de was"
    },
    {
     "text": "Kleuren die bij je bed passen"
    },
    {
     "text": "Armen vrij, geen armleuningen"
    },
    {
     "text": "3,8 kg stevig traagschuim"
    },
    {
     "text": "Vanaf €69,99"
    },
    {
     "text": "Gratis verzending NL en BE"
    },
    {
     "text": "30 dagen proberen"
    },
    {
     "text": "In 1-2 werkdagen in huis"
    },
    {
     "text": "4,5 uit 5 op bol.com"
    }
   ],
   "d": [
    {
     "text": "3,8 kg traagschuim in een katoenen hoes van 400 TC. Hoes met rits, wasbaar op 30 °C."
    },
    {
     "text": "Leeskussen van 65 x 50 x 45 cm met zijvak voor je telefoon. Koel katoen, geen fluweel."
    },
    {
     "text": "Geen armleuningen, dus je armen blijven vrij. Vijf rustige kleuren die bij je bed passen."
    },
    {
     "text": "Gratis verzending in NL en BE, in 1-2 werkdagen in huis. 30 dagen proberen."
    }
   ]
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "g": "Kleuren",
   "u": "https://blinesleep.nl/products/leeskussen-beige",
   "p1": "leeskussen",
   "p2": "kleuren",
   "h": [
    {
     "text": "Leeskussen in 5 kleuren"
    },
    {
     "text": "Kies je kleur"
    },
    {
     "text": "Ook losse hoezen per kleur"
    },
    {
     "text": "Bline leeskussen"
    },
    {
     "text": "Eén kussen dat blijft staan"
    },
    {
     "text": "Koel katoen, geen fluweel"
    },
    {
     "text": "Hoes eraf, in de was"
    },
    {
     "text": "Kleuren die bij je bed passen"
    },
    {
     "text": "Armen vrij, geen armleuningen"
    },
    {
     "text": "3,8 kg stevig traagschuim"
    },
    {
     "text": "Met vak voor je telefoon"
    },
    {
     "text": "Gratis verzending NL en BE"
    },
    {
     "text": "30 dagen proberen"
    },
    {
     "text": "In 1-2 werkdagen in huis"
    },
    {
     "text": "4,5 uit 5 op bol.com"
    }
   ],
   "d": [
    {
     "text": "In wit, beige, blauw, grijs en zwart. Een bijpassende losse hoes in elke kleur."
    },
    {
     "text": "Koel katoen 400 TC, geen fluweel. Hoes eraf met de rits en op 30 °C in de was."
    },
    {
     "text": "Eén leeskussen dat blijft staan als je leunt. Geen armleuningen, dus je armen zijn vrij."
    },
    {
     "text": "Gratis verzending in NL en BE, in 1-2 werkdagen in huis. 30 dagen proberen."
    }
   ]
  }
 ],
 "neg": {
  "Bline | Algemeen": [
   {
    "t": "gratis",
    "m": "PHRASE"
   },
   {
    "t": "tweedehands",
    "m": "PHRASE"
   },
   {
    "t": "2e hands",
    "m": "PHRASE"
   },
   {
    "t": "tweede hands",
    "m": "PHRASE"
   },
   {
    "t": "2dehands",
    "m": "PHRASE"
   },
   {
    "t": "gebruikt",
    "m": "PHRASE"
   },
   {
    "t": "marktplaats",
    "m": "PHRASE"
   },
   {
    "t": "vinted",
    "m": "PHRASE"
   },
   {
    "t": "kringloop",
    "m": "PHRASE"
   },
   {
    "t": "zelf maken",
    "m": "PHRASE"
   },
   {
    "t": "maken",
    "m": "PHRASE"
   },
   {
    "t": "diy",
    "m": "PHRASE"
   },
   {
    "t": "patroon",
    "m": "PHRASE"
   },
   {
    "t": "naaipatroon",
    "m": "PHRASE"
   },
   {
    "t": "haken",
    "m": "PHRASE"
   },
   {
    "t": "gehaakt",
    "m": "PHRASE"
   },
   {
    "t": "breien",
    "m": "PHRASE"
   },
   {
    "t": "naaien",
    "m": "PHRASE"
   },
   {
    "t": "tutorial",
    "m": "PHRASE"
   },
   {
    "t": "tuto",
    "m": "PHRASE"
   },
   {
    "t": "handleiding",
    "m": "PHRASE"
   },
   {
    "t": "ikea",
    "m": "PHRASE"
   },
   {
    "t": "action",
    "m": "PHRASE"
   },
   {
    "t": "lidl",
    "m": "PHRASE"
   },
   {
    "t": "aldi",
    "m": "PHRASE"
   },
   {
    "t": "kwantum",
    "m": "PHRASE"
   },
   {
    "t": "hema",
    "m": "PHRASE"
   },
   {
    "t": "leenbakker",
    "m": "PHRASE"
   },
   {
    "t": "jysk",
    "m": "PHRASE"
   },
   {
    "t": "blokker",
    "m": "PHRASE"
   },
   {
    "t": "xenos",
    "m": "PHRASE"
   },
   {
    "t": "temu",
    "m": "PHRASE"
   },
   {
    "t": "aliexpress",
    "m": "PHRASE"
   },
   {
    "t": "shein",
    "m": "PHRASE"
   },
   {
    "t": "wish",
    "m": "PHRASE"
   },
   {
    "t": "kruidvat",
    "m": "PHRASE"
   },
   {
    "t": "zeeman",
    "m": "PHRASE"
   },
   {
    "t": "primark",
    "m": "PHRASE"
   },
   {
    "t": "karwei",
    "m": "PHRASE"
   },
   {
    "t": "hornbach",
    "m": "PHRASE"
   },
   {
    "t": "praxis",
    "m": "PHRASE"
   },
   {
    "t": "gamma",
    "m": "PHRASE"
   },
   {
    "t": "decathlon",
    "m": "PHRASE"
   },
   {
    "t": "wibra",
    "m": "PHRASE"
   },
   {
    "t": "beter bed",
    "m": "PHRASE"
   },
   {
    "t": "sleepworld",
    "m": "PHRASE"
   },
   {
    "t": "swiss sense",
    "m": "PHRASE"
   },
   {
    "t": "auping",
    "m": "PHRASE"
   },
   {
    "t": "bol com",
    "m": "PHRASE"
   },
   {
    "t": "bol.com",
    "m": "PHRASE"
   },
   {
    "t": "bolcom",
    "m": "PHRASE"
   },
   {
    "t": "amazon",
    "m": "PHRASE"
   },
   {
    "t": "baby",
    "m": "PHRASE"
   },
   {
    "t": "babies",
    "m": "PHRASE"
   },
   {
    "t": "kind",
    "m": "PHRASE"
   },
   {
    "t": "kinderen",
    "m": "PHRASE"
   },
   {
    "t": "kinder",
    "m": "PHRASE"
   },
   {
    "t": "kinderkamer",
    "m": "PHRASE"
   },
   {
    "t": "peuter",
    "m": "PHRASE"
   },
   {
    "t": "jongen",
    "m": "PHRASE"
   },
   {
    "t": "meisje",
    "m": "PHRASE"
   },
   {
    "t": "tiener",
    "m": "PHRASE"
   },
   {
    "t": "hond",
    "m": "PHRASE"
   },
   {
    "t": "honden",
    "m": "PHRASE"
   },
   {
    "t": "kat",
    "m": "PHRASE"
   },
   {
    "t": "katten",
    "m": "PHRASE"
   },
   {
    "t": "poes",
    "m": "PHRASE"
   },
   {
    "t": "huisdier",
    "m": "PHRASE"
   },
   {
    "t": "medisch",
    "m": "PHRASE"
   },
   {
    "t": "ziekenhuis",
    "m": "PHRASE"
   },
   {
    "t": "rugpijn",
    "m": "PHRASE"
   },
   {
    "t": "nekpijn",
    "m": "PHRASE"
   },
   {
    "t": "hernia",
    "m": "PHRASE"
   },
   {
    "t": "reflux",
    "m": "PHRASE"
   },
   {
    "t": "maagzuur",
    "m": "PHRASE"
   },
   {
    "t": "apneu",
    "m": "PHRASE"
   },
   {
    "t": "snurken",
    "m": "PHRASE"
   },
   {
    "t": "scoliose",
    "m": "PHRASE"
   },
   {
    "t": "decubitus",
    "m": "PHRASE"
   },
   {
    "t": "orthopedisch",
    "m": "PHRASE"
   },
   {
    "t": "fysio",
    "m": "PHRASE"
   },
   {
    "t": "fysiotherapie",
    "m": "PHRASE"
   },
   {
    "t": "operatie",
    "m": "PHRASE"
   },
   {
    "t": "revalidatie",
    "m": "PHRASE"
   },
   {
    "t": "thuiszorg",
    "m": "PHRASE"
   },
   {
    "t": "thuiszorgwinkel",
    "m": "PHRASE"
   },
   {
    "t": "zorgwinkel",
    "m": "PHRASE"
   },
   {
    "t": "medipoint",
    "m": "PHRASE"
   },
   {
    "t": "vegro",
    "m": "PHRASE"
   },
   {
    "t": "huren",
    "m": "PHRASE"
   },
   {
    "t": "lenen",
    "m": "PHRASE"
   },
   {
    "t": "uitleen",
    "m": "PHRASE"
   },
   {
    "t": "stuitje",
    "m": "PHRASE"
   },
   {
    "t": "coccyx",
    "m": "PHRASE"
   },
   {
    "t": "heup",
    "m": "PHRASE"
   },
   {
    "t": "knie",
    "m": "PHRASE"
   },
   {
    "t": "been",
    "m": "PHRASE"
   },
   {
    "t": "benen",
    "m": "PHRASE"
   },
   {
    "t": "voeten",
    "m": "PHRASE"
   },
   {
    "t": "onderrug",
    "m": "PHRASE"
   },
   {
    "t": "lendensteun",
    "m": "PHRASE"
   },
   {
    "t": "zwanger",
    "m": "PHRASE"
   },
   {
    "t": "zwangerschap",
    "m": "PHRASE"
   },
   {
    "t": "zwangerschapskussen",
    "m": "PHRASE"
   },
   {
    "t": "bevalling",
    "m": "PHRASE"
   },
   {
    "t": "kraamweek",
    "m": "PHRASE"
   },
   {
    "t": "kraamzorg",
    "m": "PHRASE"
   },
   {
    "t": "kraampakket",
    "m": "PHRASE"
   },
   {
    "t": "borstvoeding",
    "m": "PHRASE"
   },
   {
    "t": "voedingskussen",
    "m": "PHRASE"
   },
   {
    "t": "keizersnede",
    "m": "PHRASE"
   },
   {
    "t": "auto",
    "m": "PHRASE"
   },
   {
    "t": "autostoel",
    "m": "PHRASE"
   },
   {
    "t": "bureaustoel",
    "m": "PHRASE"
   },
   {
    "t": "kantoorstoel",
    "m": "PHRASE"
   },
   {
    "t": "gamestoel",
    "m": "PHRASE"
   },
   {
    "t": "gamingstoel",
    "m": "PHRASE"
   },
   {
    "t": "rolstoel",
    "m": "PHRASE"
   },
   {
    "t": "rollator",
    "m": "PHRASE"
   },
   {
    "t": "scootmobiel",
    "m": "PHRASE"
   },
   {
    "t": "fiets",
    "m": "PHRASE"
   },
   {
    "t": "motor",
    "m": "PHRASE"
   },
   {
    "t": "scooter",
    "m": "PHRASE"
   },
   {
    "t": "boot",
    "m": "PHRASE"
   },
   {
    "t": "camper",
    "m": "PHRASE"
   },
   {
    "t": "caravan",
    "m": "PHRASE"
   },
   {
    "t": "tuin",
    "m": "PHRASE"
   },
   {
    "t": "tuinbank",
    "m": "PHRASE"
   },
   {
    "t": "tuinstoel",
    "m": "PHRASE"
   },
   {
    "t": "buiten",
    "m": "PHRASE"
   },
   {
    "t": "loungeset",
    "m": "PHRASE"
   },
   {
    "t": "pallet",
    "m": "PHRASE"
   },
   {
    "t": "palletkussen",
    "m": "PHRASE"
   },
   {
    "t": "strand",
    "m": "PHRASE"
   },
   {
    "t": "zwembad",
    "m": "PHRASE"
   },
   {
    "t": "bad",
    "m": "PHRASE"
   },
   {
    "t": "ligbad",
    "m": "PHRASE"
   },
   {
    "t": "vliegtuig",
    "m": "PHRASE"
   },
   {
    "t": "reiskussen",
    "m": "PHRASE"
   },
   {
    "t": "nekkussen",
    "m": "PHRASE"
   },
   {
    "t": "hoofdkussen",
    "m": "PHRASE"
   },
   {
    "t": "dekbed",
    "m": "PHRASE"
   },
   {
    "t": "matras",
    "m": "PHRASE"
   },
   {
    "t": "kussensloop",
    "m": "PHRASE"
   },
   {
    "t": "kussenslopen",
    "m": "PHRASE"
   },
   {
    "t": "elektrisch",
    "m": "PHRASE"
   },
   {
    "t": "elektrische",
    "m": "PHRASE"
   },
   {
    "t": "verstelbaar",
    "m": "PHRASE"
   },
   {
    "t": "verstelbare",
    "m": "PHRASE"
   },
   {
    "t": "massage",
    "m": "PHRASE"
   },
   {
    "t": "warmte",
    "m": "PHRASE"
   },
   {
    "t": "infrarood",
    "m": "PHRASE"
   },
   {
    "t": "opblaasbaar",
    "m": "PHRASE"
   },
   {
    "t": "opblaasbare",
    "m": "PHRASE"
   },
   {
    "t": "wigkussen been",
    "m": "PHRASE"
   },
   {
    "t": "beenkussen",
    "m": "PHRASE"
   },
   {
    "t": "puzzel",
    "m": "PHRASE"
   },
   {
    "t": "puzzelmat",
    "m": "PHRASE"
   },
   {
    "t": "puzzelmap",
    "m": "PHRASE"
   },
   {
    "t": "puzzeltafel",
    "m": "PHRASE"
   },
   {
    "t": "puzzelbord",
    "m": "PHRASE"
   },
   {
    "t": "puzzelplank",
    "m": "PHRASE"
   },
   {
    "t": "puzzelplaat",
    "m": "PHRASE"
   },
   {
    "t": "vacature",
    "m": "PHRASE"
   },
   {
    "t": "vacatures",
    "m": "PHRASE"
   },
   {
    "t": "baan",
    "m": "PHRASE"
   },
   {
    "t": "banen",
    "m": "PHRASE"
   },
   {
    "t": "stage",
    "m": "PHRASE"
   },
   {
    "t": "salaris",
    "m": "PHRASE"
   },
   {
    "t": "wat is",
    "m": "PHRASE"
   },
   {
    "t": "betekenis",
    "m": "PHRASE"
   },
   {
    "t": "engels",
    "m": "PHRASE"
   },
   {
    "t": "in het engels",
    "m": "PHRASE"
   },
   {
    "t": "vertaling",
    "m": "PHRASE"
   },
   {
    "t": "duits",
    "m": "PHRASE"
   },
   {
    "t": "definitie",
    "m": "PHRASE"
   },
   {
    "t": "bank",
    "m": "EXACT"
   },
   {
    "t": "banken",
    "m": "EXACT"
   },
   {
    "t": "kussen",
    "m": "EXACT"
   },
   {
    "t": "kussens",
    "m": "EXACT"
   },
   {
    "t": "rugkussen",
    "m": "EXACT"
   },
   {
    "t": "rugsteun",
    "m": "EXACT"
   },
   {
    "t": "wigkussen",
    "m": "EXACT"
   },
   {
    "t": "lezen in bed",
    "m": "EXACT"
   }
  ],
  "Bline | Merk": [
   {
    "t": "bline",
    "m": "PHRASE"
   },
   {
    "t": "blinesleep",
    "m": "PHRASE"
   },
   {
    "t": "bline sleep",
    "m": "PHRASE"
   },
   {
    "t": "blin",
    "m": "EXACT"
   },
   {
    "t": "blins",
    "m": "EXACT"
   }
  ],
  "Bline | Concurrenten": [
   {
    "t": "ella",
    "m": "PHRASE"
   },
   {
    "t": "ella sleeps",
    "m": "PHRASE"
   },
   {
    "t": "ellasleeps",
    "m": "PHRASE"
   },
   {
    "t": "q living",
    "m": "PHRASE"
   },
   {
    "t": "q-living",
    "m": "PHRASE"
   },
   {
    "t": "qliving",
    "m": "PHRASE"
   },
   {
    "t": "ten cate",
    "m": "PHRASE"
   },
   {
    "t": "tencate",
    "m": "PHRASE"
   },
   {
    "t": "cozysense",
    "m": "PHRASE"
   },
   {
    "t": "ducky dons",
    "m": "PHRASE"
   },
   {
    "t": "happybed",
    "m": "PHRASE"
   },
   {
    "t": "happy bed",
    "m": "PHRASE"
   },
   {
    "t": "homca",
    "m": "PHRASE"
   },
   {
    "t": "best life",
    "m": "PHRASE"
   },
   {
    "t": "eloneo",
    "m": "PHRASE"
   },
   {
    "t": "sleepy lounge",
    "m": "PHRASE"
   },
   {
    "t": "zensation",
    "m": "PHRASE"
   },
   {
    "t": "havargo",
    "m": "PHRASE"
   },
   {
    "t": "vitapur",
    "m": "PHRASE"
   },
   {
    "t": "milliard",
    "m": "PHRASE"
   },
   {
    "t": "costway",
    "m": "PHRASE"
   },
   {
    "t": "isleep",
    "m": "PHRASE"
   },
   {
    "t": "sleeplife",
    "m": "PHRASE"
   },
   {
    "t": "zelesta",
    "m": "PHRASE"
   },
   {
    "t": "livarno",
    "m": "PHRASE"
   },
   {
    "t": "icon",
    "m": "PHRASE"
   },
   {
    "t": "symposium",
    "m": "PHRASE"
   },
   {
    "t": "weids wonen",
    "m": "PHRASE"
   },
   {
    "t": "polydaun",
    "m": "PHRASE"
   },
   {
    "t": "sleeptight",
    "m": "PHRASE"
   },
   {
    "t": "droomtextiel",
    "m": "PHRASE"
   },
   {
    "t": "lyxus",
    "m": "PHRASE"
   },
   {
    "t": "soft silky",
    "m": "PHRASE"
   },
   {
    "t": "defa",
    "m": "PHRASE"
   },
   {
    "t": "novamed",
    "m": "PHRASE"
   },
   {
    "t": "sissel",
    "m": "PHRASE"
   },
   {
    "t": "tempur",
    "m": "PHRASE"
   },
   {
    "t": "dorsaback",
    "m": "PHRASE"
   },
   {
    "t": "lucovitaal",
    "m": "PHRASE"
   },
   {
    "t": "wellpur",
    "m": "PHRASE"
   },
   {
    "t": "nira",
    "m": "PHRASE"
   },
   {
    "t": "froli",
    "m": "PHRASE"
   },
   {
    "t": "inventum",
    "m": "PHRASE"
   },
   {
    "t": "the bookseat",
    "m": "PHRASE"
   },
   {
    "t": "ergokussens",
    "m": "PHRASE"
   }
  ],
  "Bline | Productmismatch Search": [
   {
    "t": "armleuning",
    "m": "PHRASE"
   },
   {
    "t": "armleuningen",
    "m": "PHRASE"
   },
   {
    "t": "armsteun",
    "m": "PHRASE"
   },
   {
    "t": "nekrol",
    "m": "PHRASE"
   },
   {
    "t": "neksteun",
    "m": "PHRASE"
   },
   {
    "t": "hoofdsteun",
    "m": "PHRASE"
   },
   {
    "t": "schoot",
    "m": "PHRASE"
   },
   {
    "t": "op schoot",
    "m": "PHRASE"
   },
   {
    "t": "vloer",
    "m": "PHRASE"
   },
   {
    "t": "grond",
    "m": "PHRASE"
   },
   {
    "t": "rond",
    "m": "PHRASE"
   },
   {
    "t": "2 personen",
    "m": "PHRASE"
   },
   {
    "t": "90 cm",
    "m": "PHRASE"
   },
   {
    "t": "140",
    "m": "PHRASE"
   },
   {
    "t": "140 cm",
    "m": "PHRASE"
   },
   {
    "t": "160",
    "m": "PHRASE"
   },
   {
    "t": "160 cm",
    "m": "PHRASE"
   },
   {
    "t": "180",
    "m": "PHRASE"
   },
   {
    "t": "180 cm",
    "m": "PHRASE"
   },
   {
    "t": "200",
    "m": "PHRASE"
   },
   {
    "t": "goedkoop",
    "m": "PHRASE"
   },
   {
    "t": "goedkope",
    "m": "PHRASE"
   },
   {
    "t": "aanbieding",
    "m": "PHRASE"
   },
   {
    "t": "korting",
    "m": "PHRASE"
   },
   {
    "t": "sale",
    "m": "PHRASE"
   },
   {
    "t": "uitverkoop",
    "m": "PHRASE"
   },
   {
    "t": "black friday",
    "m": "PHRASE"
   },
   {
    "t": "teddy",
    "m": "PHRASE"
   },
   {
    "t": "pompom",
    "m": "PHRASE"
   },
   {
    "t": "pom pom",
    "m": "PHRASE"
   },
   {
    "t": "fluffy",
    "m": "PHRASE"
   },
   {
    "t": "minecraft",
    "m": "PHRASE"
   },
   {
    "t": "stitch",
    "m": "PHRASE"
   },
   {
    "t": "sierkussen",
    "m": "PHRASE"
   },
   {
    "t": "sierkussens",
    "m": "PHRASE"
   },
   {
    "t": "zitzak",
    "m": "PHRASE"
   },
   {
    "t": "slapen",
    "m": "PHRASE"
   },
   {
    "t": "zijslaper",
    "m": "PHRASE"
   },
   {
    "t": "lendekussen",
    "m": "PHRASE"
   }
  ]
 },
 "koppel": [
  [
   "Bline | Algemeen",
   "00 Search | Merk | NL+BE"
  ],
  [
   "Bline | Algemeen",
   "02 Search | Generiek | NL+BE"
  ],
  [
   "Bline | Merk",
   "02 Search | Generiek | NL+BE"
  ],
  [
   "Bline | Concurrenten",
   "02 Search | Generiek | NL+BE"
  ],
  [
   "Bline | Productmismatch Search",
   "02 Search | Generiek | NL+BE"
  ]
 ],
 "sl": [
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Vijf kleuren",
   "d1": "Wit, beige, blauw, grijs, zwart",
   "d2": "Kies de kleur die bij je bed past",
   "u": "https://blinesleep.nl/#kleuren"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Losse hoezen",
   "d1": "Tweede hoes voor de wasdag",
   "d2": "Katoen 400 TC, met rits",
   "u": "https://blinesleep.nl/products/hoes-beige"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Maten en details",
   "d1": "65 x 50 x 45 cm, 3,8 kg",
   "d2": "Zo past hij op je bed",
   "u": "https://blinesleep.nl/pages/maatgids"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Veelgestelde vragen",
   "d1": "Maat, wassen, levertijd",
   "d2": "Alles op één pagina",
   "u": "https://blinesleep.nl/pages/veelgestelde-vragen"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Verzending",
   "d1": "Gratis naar NL en BE",
   "d2": "In 1-2 werkdagen in huis",
   "u": "https://blinesleep.nl/pages/verzending"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "30 dagen proberen",
   "d1": "Rustig thuis uitproberen",
   "d2": "Zo werkt retourneren",
   "u": "https://blinesleep.nl/pages/retourneren"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Over Bline",
   "d1": "Een Nederlands merk uit Borne",
   "d2": "Wie we zijn en wat we maken",
   "u": "https://blinesleep.nl/pages/over-bline"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Contact",
   "d1": "Vragen over maat of kleur?",
   "d2": "We helpen je graag",
   "u": "https://blinesleep.nl/pages/contact"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Vijf kleuren",
   "d1": "Wit, beige, blauw, grijs, zwart",
   "d2": "Kies de kleur die bij je bed past",
   "u": "https://blinesleep.nl/#kleuren"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Losse hoezen",
   "d1": "Tweede hoes voor de wasdag",
   "d2": "Katoen 400 TC, met rits",
   "u": "https://blinesleep.nl/products/hoes-beige"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Maten en details",
   "d1": "65 x 50 x 45 cm, 3,8 kg",
   "d2": "Zo past hij op je bed",
   "u": "https://blinesleep.nl/pages/maatgids"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Veelgestelde vragen",
   "d1": "Maat, wassen, levertijd",
   "d2": "Alles op één pagina",
   "u": "https://blinesleep.nl/pages/veelgestelde-vragen"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Verzending",
   "d1": "Gratis naar NL en BE",
   "d2": "In 1-2 werkdagen in huis",
   "u": "https://blinesleep.nl/pages/verzending"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "30 dagen proberen",
   "d1": "Rustig thuis uitproberen",
   "d2": "Zo werkt retourneren",
   "u": "https://blinesleep.nl/pages/retourneren"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Over Bline",
   "d1": "Een Nederlands merk uit Borne",
   "d2": "Wie we zijn en wat we maken",
   "u": "https://blinesleep.nl/pages/over-bline"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Contact",
   "d1": "Vragen over maat of kleur?",
   "d2": "We helpen je graag",
   "u": "https://blinesleep.nl/pages/contact"
  }
 ],
 "co": [
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Gratis verzending NL/BE"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "30 dagen proberen"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "In 1-2 werkdagen in huis"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Koel katoen, geen fluweel"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Hoes eraf, in de was"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Hoes wasbaar op 30 °C"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "3,8 kg traagschuim"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Vak voor je telefoon"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Katoen 400 TC met rits"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Geen armleuningen"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Losse hoezen per kleur"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Betaal met iDEAL"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Bancontact voor België"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Nederlands merk"
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "t": "Echte klantenservice"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Gratis verzending NL/BE"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "30 dagen proberen"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "In 1-2 werkdagen in huis"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Koel katoen, geen fluweel"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Hoes eraf, in de was"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Hoes wasbaar op 30 °C"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "3,8 kg traagschuim"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Vak voor je telefoon"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Katoen 400 TC met rits"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Geen armleuningen"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Losse hoezen per kleur"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Betaal met iDEAL"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Bancontact voor België"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Nederlands merk"
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "t": "Echte klantenservice"
  }
 ],
 "sn": [
  {
   "c": "00 Search | Merk | NL+BE",
   "h": "Styles",
   "v": [
    "Wit",
    "Beige",
    "Blauw",
    "Grijs",
    "Zwart"
   ]
  },
  {
   "c": "00 Search | Merk | NL+BE",
   "h": "Types",
   "v": [
    "Leeskussen",
    "Rugkussen voor bed",
    "Losse hoes"
   ]
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "h": "Styles",
   "v": [
    "Wit",
    "Beige",
    "Blauw",
    "Grijs",
    "Zwart"
   ]
  },
  {
   "c": "02 Search | Generiek | NL+BE",
   "h": "Types",
   "v": [
    "Leeskussen",
    "Rugkussen voor bed",
    "Losse hoes"
   ]
  }
 ],
 "shopping": {
  "merchantId": "5871227119",
  "items": [
   [
    "shopify_zz_10913990181203_55210456514899",
    "beige",
    0.45
   ],
   [
    "shopify_zz_10913990869331_55210458448211",
    "blauw",
    0.45
   ],
   [
    "shopify_zz_10913991131475_55210458710355",
    "grijs",
    0.45
   ],
   [
    "shopify_zz_10913991393619_55210459332947",
    "zwart",
    0.45
   ],
   [
    "shopify_zz_10913990639955_55210457170259",
    "wit",
    0.4
   ]
  ]
 }
};

var BUDGET = { '00 Search | Merk | NL+BE': 1, '02 Search | Generiek | NL+BE': 4, '01 Shopping | Leeskussen | NL+BE': 5 };
var NL = 'geoTargetConstants/2528', BE = 'geoTargetConstants/2056', NEDERLANDS = 'languageConstants/1010';

function main() {
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
