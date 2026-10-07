# Bline meetplan (stand 7 oktober 2026)

Doel: elke verkoop één keer, met het juiste bedrag, in Shopify, Meta en Google, en alleen bij bezoekers die toestemming geven. Pas als dat aantoonbaar werkt, gaat er advertentiebudget uit.

## Wat er vorige keer misging (en hoe we het nu voorkomen)

| Fout | Gevolg | Nu |
|---|---|---|
| Geen werkende aankoopmeting (zustermerk: €831 uitgegeven, 0 conversies gemeten) | Google en Meta bieden blind, je kunt niet zien wat verkoopt | Eerst een testbestelling die aantoonbaar binnenkomt in Meta én Google, daarna pas budget |
| Meerdere conversieacties als "primair" (bijv. paginaweergave, winkelwagen én aankoop) | Het systeem optimaliseert op de verkeerde actie en rapporteert te veel "conversies" | Alleen **Aankoop** is primair; de rest secundair (alleen ter info) |
| Dubbel tellen (zelfde aankoop via de app én via GA4-import of losse code) | Twee keer zoveel conversies, verkeerde ROAS | Eén bron per platform: de officiële Shopify-apps. Geen losse code in het thema, geen Tag Manager, geen GA4-import als conversie in Google Ads |
| Oude pixel/dataset van de vorige winkel nog gekoppeld | Gegevens van twee winkels door elkaar | Nieuwe winkel gebruikt **Pixel 1 (488144327490376)**; de oude dataset "Shopify: 4d21faa2" en de oude catalogus niet gebruiken, opruimen als alles werkt |

## Hoe het is ingericht

| Onderdeel | Hoe | Stand |
|---|---|---|
| Thema | geen losse trackingcode (gecontroleerd 07-10: geen fbq, gtag, GTM of andere pixels in het thema) | goed |
| Toestemming | Shopify-cookiebanner aan, automatisch beheerd; NL en BE: toestemming verplicht. Pixels via Shopify-apps volgen die toestemming vanzelf | goed (07-10 via API gecontroleerd) |
| Meta | app "Facebook & Instagram" in Shopify, Pixel 1 (488144327490376), gegevens delen "Uitgebreid" (pixel + Conversions API, Shopify ontdubbelt zelf) | gekoppeld; ontvangst van gebeurtenissen nog controleren (zie test) |
| Google | app "Google & YouTube" in Shopify: Merchant Center, aankoopconversie, Enhanced Conversions, toestemmingsmodus (consent mode v2) via Shopify | **nog te doen (Joost)** |
| Google Analytics 4 | optioneel via dezelfde Google-app, alleen voor analyse; niet als conversie importeren in Google Ads | later |
| Klaviyo | Shopify-integratie (bestellingen, checkouts) + Klaviyo-script op de site | goed; in Klaviyo de instelling voor toestemming controleren (zie Joost-acties) |
| Eigen gebeurtenissen | `bline_kleur_gekozen`, `bline_hoes_aangevinkt`, `bline_in_winkelwagen`, `bline_pop_aangemeld` (Shopify-klantgebeurtenissen, voor eigen analyse) | goed |

## Gebeurtenissen die moeten binnenkomen

| Gebeurtenis | Meta | Google Ads | Primair? |
|---|---|---|---|
| Pagina bekeken | PageView | (pagina weergeven) | nee |
| Product bekeken | ViewContent (met content_ids, waarde) | view_item | nee |
| In winkelwagen | AddToCart (waarde) | add_to_cart | nee |
| Checkout gestart | InitiateCheckout | begin_checkout | nee |
| **Aankoop** | **Purchase (waarde incl. btw, EUR, order-ID)** | **purchase (waarde, transactie-ID, Enhanced Conversions)** | **ja, als enige** |

Waarde: totaalbedrag van de bestelling in euro. Meta en Google gebruiken het order-ID om dubbele meldingen samen te voegen.

## UTM-afspraken

- Meta: `utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`
- Google: automatische tagging aan (gclid), geen handmatige UTM nodig.
- Klaviyo: `utm_source=klaviyo&utm_medium=email&utm_campaign={message_name}` (staat al in de flows).
- Campagnenamen: `bl_<kanaal>_<doel>_<land>`, bijvoorbeeld `bl_meta_sales_nlbe`, `bl_google_search_generiek_nl`.

## Testprocedure (voordat er één euro uitgaat)

1. **Meta:** Gebeurtenissenbeheer > Pixel 1 > **Gebeurtenissen testen** > website `blinesleep.nl` (of de myshopify-link) openen via die knop. Bekijk een product, leg het in de winkelwagen, start de checkout. Elke stap moet in de lijst verschijnen, met "Browser" én "Server".
2. **Testbestelling:** een kortingscode van 100% voor één gebruik (maak ik op verzoek aan), daarmee een echte bestelling plaatsen. Daarna de bestelling annuleren.
3. **Controleren:**
   - Meta: Purchase met de juiste waarde, browser en server, en een score voor gebeurteniskoppeling ("Event Match Quality") van 6 of hoger.
   - Google Ads: Doelen > Conversies > de aankoopactie staat binnen 24 uur op "Conversies worden geregistreerd".
   - Shopify: Instellingen > Klantgebeurtenissen > beide apps "Verbonden".
4. **Met toestemming testen:** in een incognitovenster vanuit NL de cookiebanner zien, op "Accepteren" klikken en de test herhalen. Na "Weigeren" mogen er geen marketinggebeurtenissen meer verschijnen. Shopify stuurt dan via de toestemmingsmodus alleen nog naamloze signalen naar Google.
5. Pas als 1 tot en met 4 kloppen: campagnes mogen aan.

Zodra de Meta- en Google-sleutels in een sessie beschikbaar zijn, controleer ik de ontvangst ook via de API: het aantal gebeurtenissen per type bij de pixel en de status van de conversieacties in Google Ads.

## Acties Joost

1. **Shopify > Apps > "Google & YouTube" installeren.**
   - Koppel het Google-account dat toegang heeft tot Google Ads 860-535-9447.
   - Maak een **nieuw** Merchant Center-account aan voor Bline.
   - Koppel Google Ads **860-535-9447**.
   - Zet **conversiemeting** aan, met **Enhanced Conversions** aan.
2. **Google Ads > Doelen > Conversies:** alleen de aankoopactie van de Shopify-app op **Primair**. Alles wat de app verder aanmaakt (paginaweergave, winkelwagen, checkout) zet je op **Secundair**. Twijfel je, stuur een screenshot.
3. **Klaviyo:** controleer bij Integraties > Shopify > Instellingen dat het Klaviyo-script de Shopify-toestemming respecteert (de optie heet ongeveer "Respect Shopify customer privacy" of "Consent"), en zet die aan.
4. Testbestelling volgens de testprocedure, samen met mij.
