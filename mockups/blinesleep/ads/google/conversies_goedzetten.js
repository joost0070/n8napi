/**
 * Bline: conversiedoelen in Google Ads in één keer goed zetten.
 * Gebruik: Google Ads (account Bline 860-535-9447) > Tools > Bulkacties > Scripts > + > plak dit script > Autoriseren.
 * Eerst op "Voorbeeld" klikken: dan wordt niets gewijzigd en zie je in "Logboeken" wat het script zou doen.
 * Klopt het, dan op "Uitvoeren" klikken.
 *
 * Wat het doet:
 * 1. Alleen "Aankopen" blijft een accountdoel waar Google op biedt. Alle andere doelen
 *    (winkelwagen, checkout, telefoontjes, contact, route, paginaweergave, enz.) gaan uit de accountdoelen.
 *    De acties blijven meten, ze sturen alleen niet meer.
 * 2. Staat de aankoopactie van de Shopify-app er ("Google Shopping App Purchase"), dan wordt die primair
 *    en gaat de GA4-import "Aankoop" naar secundair. Staat hij er nog niet, dan blijft GA4 voorlopig primair
 *    en meldt het script dat je het later nog een keer moet draaien.
 * 3. Alle andere acties in de categorie aankoop worden secundair, zodat er maar één primaire aankoop is.
 */
function main() {
  var cid = AdsApp.currentAccount().getCustomerId().replace(/-/g, '');
  Logger.log('Account: ' + AdsApp.currentAccount().getName() + ' (' + AdsApp.currentAccount().getCustomerId() + ')');

  // 1. Accountdoelen: alleen aankopen biedbaar
  var doelen = AdsApp.search('SELECT customer_conversion_goal.resource_name, customer_conversion_goal.category, customer_conversion_goal.origin, customer_conversion_goal.biddable FROM customer_conversion_goal');
  while (doelen.hasNext()) {
    var d = doelen.next().customerConversionGoal;
    var moet = d.category === 'PURCHASE';
    if (d.biddable !== moet) {
      wijzig({ customerConversionGoalOperation: { update: { resourceName: d.resourceName, biddable: moet }, updateMask: 'biddable' } },
        'Accountdoel ' + d.category + ' / ' + d.origin + ': ' + (moet ? 'aan' : 'uit'));
    } else {
      Logger.log('Accountdoel ' + d.category + ' / ' + d.origin + ': staat al goed (' + (moet ? 'aan' : 'uit') + ')');
    }
  }

  // 2. Aankoopacties: één primaire, bij voorkeur die van de Shopify-app
  var acties = [];
  var it = AdsApp.search("SELECT conversion_action.resource_name, conversion_action.name, conversion_action.type, conversion_action.category, conversion_action.primary_for_goal, conversion_action.status FROM conversion_action WHERE conversion_action.status = 'ENABLED'");
  while (it.hasNext()) acties.push(it.next().conversionAction);

  var aankopen = acties.filter(function (a) { return a.category === 'PURCHASE'; });
  var shopify = aankopen.filter(function (a) { return /google shopping app purchase/i.test(a.name); })[0];
  Logger.log('Aankoopacties gevonden: ' + aankopen.map(function (a) { return a.name + ' [' + a.type + ', ' + (a.primaryForGoal ? 'primair' : 'secundair') + ']'; }).join(' | '));

  if (!shopify) {
    Logger.log('LET OP: de aankoopactie van de Shopify-app ("Google Shopping App Purchase") bestaat nog niet. ' +
      'De GA4-aankoop blijft voorlopig primair. Draai dit script morgen nog een keer.');
  } else {
    aankopen.forEach(function (a) {
      var moet = a.resourceName === shopify.resourceName;
      if (a.primaryForGoal !== moet) {
        wijzig({ conversionActionOperation: { update: { resourceName: a.resourceName, primaryForGoal: moet }, updateMask: 'primary_for_goal' } },
          'Actie "' + a.name + '": ' + (moet ? 'primair' : 'secundair'));
      }
    });
  }

  // 3. Overzicht van wat er nog primair is buiten aankopen (ter controle; telt niet mee zolang het doel uit staat)
  acties.filter(function (a) { return a.category !== 'PURCHASE' && a.primaryForGoal; }).forEach(function (a) {
    Logger.log('Ter info, primair maar zonder accountdoel: "' + a.name + '" (' + a.category + ')');
  });
  Logger.log('Klaar.');
}

function wijzig(operatie, omschrijving) {
  var r = AdsApp.mutate(operatie);
  if (r.isSuccessful()) Logger.log('OK   ' + omschrijving);
  else Logger.log('FOUT ' + omschrijving + ': ' + r.getErrorMessages().join('; '));
}
