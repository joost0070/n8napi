# Bline Klaviyo-flows (stand 6 oktober 2026)

Gemaakt via de Klaviyo-API op het gratis abonnement (max. 3 live flows). Alleen flows die naar een aankoop leiden. Alle drie staan **live**.

| Flow | Trigger | Mails | Korting |
|---|---|---|---|
| Bline \| Verlaten checkout | Checkout Started (Shopify) | 1 uur: "Je leeskussen staat nog klaar" (winkelwagen met foto per kleur en totaal) · 24 uur: veelgestelde vragen · 3 dagen: persoonlijke code | 10% in mail 3 (coupon `BLINE_CHECKOUT10`) |
| Bline \| Product bekeken en winkelwagen | Viewed Product (Shopify) | 2 uur: splitst op "in winkelwagen gelegd" (winkelwagenmail) of niet (productmail) · 2 dagen: kleurenmail | geen |
| Bline \| Welkom met 10% | Toegevoegd aan "Email List" | direct: welkom met code · 2 dagen: "stevig van binnen" · 5 dagen: code nog een keer | 10% in mail 1 en 3 (coupon `BLINE_WELKOM10`) |

Iedereen gaat uit een flow zodra die persoon bestelt. De productmail stopt ook zodra iemand afrekent, want dan neemt de checkoutflow het over. De welkomstflow is alleen voor mensen die nog nooit hebben besteld. Bij de productflow staat slim versturen aan: niet vaker dan één mail per 16 uur.

## Kortingscodes

- In Shopify: twee kortingen van 10% op alles, elk met 250 unieke codes.
  - "Klaviyo welkom 10% (unieke codes BLW-)"
  - "Klaviyo verlaten checkout 10% (unieke codes BLC-)"
  - Elke code is één keer te gebruiken, één keer per klant, en is niet te combineren met de automatische kortingen.
- In Klaviyo: dezelfde codes onder Content > Coupons. Elke ontvanger krijgt een eigen code.
- Bijna op? Voeg codes toe met dezelfde opbouw. Of maak in Klaviyo een Shopify-coupon die zelf codes aanmaakt, en vervang de couponnaam in de templates.

## Bestanden

- `mails.py`: de 9 HTML-templates in de Bline-stijl.
- `flows.py`: de flowdefinities.
- `kv.py`: API-hulpje dat de sleutel uit de omgeving leest.
- `voorbeelden/`: schermafdrukken op mobiel.

De kortingscodes zelf staan niet in de repo.

## Nog te doen in Klaviyo (Joost)

1. **Eigen verzenddomein** (Settings > Domains), bijvoorbeeld `send.blinesleep.nl`. blinesleep.nl heeft een DMARC-regel met `p=quarantine`, dus zonder eigen domein komen mails van mail@blinesleep.nl waarschijnlijk in de spam.
2. **Accountinstellingen:** tijdzone Europe/Amsterdam en valuta EUR. Nu staan die op US/Eastern en USD. Zet de website-URL op https://blinesleep.nl zodra het domein gekoppeld is: alle links in de mails gebruiken die URL.
3. **Aanmeldformulier** (1 live formulier inbegrepen): een pop-up met "10% op je eerste bestelling" die aanmeldingen in "Email List" zet. Controleer ook dat de Shopify-integratie nieuwsbriefaanmeldingen naar "Email List" synchroniseert.
4. **Shopify:** zet de eigen mail voor verlaten checkouts in Shopify uit (Marketing > Automatiseringen), anders krijgen klanten twee herinneringen.
