# Bline shop opbouw logboek

Werkwijze volgens `prompts/bline-shop-opbouwen-masterprompt.md` (versie 1.1). Geheimen en de winkeldomeinnaam staan niet in dit logboek.

## 4 oktober 2026, sessie 1

### Stap 0: omgevingsvariabelen

| Variabele | Aanwezig |
|---|---|
| BLINE_SHOPIFY_STORE | ja |
| BLINE_SHOPIFY_CLIENT_ID | ja |
| BLINE_SHOPIFY_CLIENT_SECRET | ja |

Alleen de namen gecontroleerd, geen waarden getoond. De SHOPIFY_*- en BOL_*-variabelen zijn niet gebruikt.

### Werkpakket A: sleutel ophalen

**Resultaat: mislukt. Werk gestopt volgens hoofdstuk 5 van de masterprompt.**

- Aanvraag: `POST https://<BLINE_SHOPIFY_STORE>/admin/oauth/access_token` met `grant_type=client_credentials`, client id en secret (form-encoded).
- Antwoord: **HTTP 404**, Shopify-pagina "Store unavailable". Er is dus geen sleutel opgehaald en geen enkele API-call gedaan.

Nader onderzocht (zonder sleutel, alleen openbare adressen):

| Controle | Uitkomst |
|---|---|
| Vorm van BLINE_SHOPIFY_STORE | 24 tekens, eindigt op `.myshopify.com`, geen `https://`, geen slash, geen spaties. De vorm klopt. |
| Winkelpagina `/` | 404 "Store unavailable" |
| `/password` | 404 "Store unavailable" |
| `/admin` | doorverwijzing naar inlogpagina |
| Proxy van de sessie | werkt normaal |
| Vergelijking met een verzonnen, niet-bestaande `.myshopify.com`-naam | precies hetzelfde gedrag (404 "Store unavailable", `/admin` naar inlog) |

Conclusie: Shopify kent de winkel onder deze `.myshopify.com`-naam niet als actieve winkel. Een winkel die nog in de proefperiode zit of achter een wachtwoord staat, toont normaal de wachtwoordpagina, geen "Store unavailable". De fout ligt dus niet bij de app-rechten (dat zou een 400 of 401 geven), maar bij de winkelnaam of de status van de winkel.

Meest waarschijnlijke oorzaken, in volgorde:

1. **Verkeerde winkelnaam in de variabele.** De vaste `.myshopify.com`-naam wijkt vaak af van de winkelnaam die je zelf kiest (Shopify maakt soms een naam als `abc123-x1.myshopify.com`). Te vinden in Shopify admin onder Instellingen > Domeinen, of in de adresbalk van de admin (`admin.shopify.com/store/<naam>`; de variabele is dan `<naam>.myshopify.com`).
2. **Winkel gesloten, gepauzeerd of proefperiode verlopen zonder abonnement.** Te zien in Instellingen > Abonnement.
3. **Winkel nog niet aangemaakt** in dezelfde organisatie als de Dev Dashboard-app.

### Wat ontbreekt (stand nulmeting)

De nulmeting (thema's, producten, pagina's, menu's, markten, verzendprofielen, beleid, betaalinstellingen, rechten) kon niet worden gedaan. Alles uit werkpakket A staat nog open, net als B tot en met L.

### Niet gedaan, bewust

- Niets aangemaakt, niets gepubliceerd, geen prijzen gezet.
- Geen mails verstuurd, geen beelden laten maken.
- Geen regel in het Systeemregister gezet (dat hoort bij de afronding van de opbouw).

### Wacht op Joost

1. Controleer de `.myshopify.com`-naam van de Bline-winkel en zet die in `BLINE_SHOPIFY_STORE` (zonder `https://`).
2. Controleer of de winkel actief is (abonnement of proefperiode loopt).
3. Controleer of de Dev Dashboard-app in dezelfde organisatie zit, is vrijgegeven en op deze winkel is geïnstalleerd.
4. Start daarna opnieuw met "Bline shop opbouwen".

### Aanvulling: env nagekeken na melding "het is blinesleep.nl"

- `BLINE_SHOPIFY_STORE` staat op `blinesleep.myshopify.com`. Shopify kent die winkelnaam niet (404 "Store unavailable").
- `blinesleep.nl` en `www.blinesleep.nl` draaien nu op een eigen webserver (LiteSpeed, antwoord 401 "Authorization Required"), niet op Shopify. Het domein is dus nog niet aan een Shopify-winkel gekoppeld en verraadt de `.myshopify.com`-naam niet.
- Voor de sleutel is altijd de vaste `.myshopify.com`-naam nodig; het eigen domein werkt niet voor de API.
- Een paar voor de hand liggende namen geprobeerd (bline-sleep, blinesleep-nl, blinesleepnl, bline, bline-nl en enkele varianten): geen daarvan is een actieve winkel van Bline.
- Nodig van Joost: de naam uit de adresbalk van de Shopify-admin (`admin.shopify.com/store/<naam>`). De variabele wordt dan `<naam>.myshopify.com`.
