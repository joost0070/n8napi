# Uitverkoopradar

Doel: automatisch signaleren wanneer een best verkopend artikel uit voorraad gaat
lopen, op een moment dat bijbestellen nog op tijd landt.

Dit vervangt niet de rest van de Voorraad Watch, maar zet één vraag voorop:
**op welke dag is deze maat op, en is dat vóór of na het moment dat nieuwe
voorraad binnen kan zijn?**

---

## Waarom "dagen voorraad" alleen niet genoeg is

De gebruikelijke rekensom is `voorraad / gemiddelde verkoop per dag`. Die gaat bij
schoenen op drie manieren mis:

1. **Het seizoen.** 100 paar winterlaarzen in week 40 gaan niet even snel als in
   week 48. Een vlak gemiddelde zegt "ruim voldoende" terwijl de piek nog moet
   komen, en in maart het omgekeerde.
2. **Uitverkochte weken.** Een maat die de helft van de maand leeg stond,
   verkocht de helft minder — niet omdat de vraag lager was, maar omdat er niets
   te verkopen viel. Dan lijkt de vraag laag en komt het signaal te laat.
3. **Kleine aantallen per maat.** Een maat met twee verkopen in vier weken geeft
   geen betrouwbaar eigen tempo.

## De methode

Per **model** (artikel + kleur), daarna verdeeld over de maten.

### 1. Recent tempo, gecorrigeerd voor leegstand

```
verkocht laatste 28 dagen, alle kanalen
------------------------------------------   x 7  =  tempo per week
dagen dat het model leverbaar was
```

"Leverbaar" komt uit ShopifyQL (`days_out_of_stock` per maat), gewogen naar hoe
belangrijk de maat is: als maat 39 leeg stond telt dat zwaarder dan maat 46.

### 2. Ontseizoenen

Het tempo van de afgelopen vier weken wordt gedeeld door het seizoensgewicht van
die vier weken. Dat geeft het **jaarniveau** van het model: hoeveel het zou
verkopen als het het hele jaar leverbaar was.

Omdat dit uit de *recente* weken komt, zit de groei of krimp van het merk er al
in. Een aparte momentumfactor is niet meer nodig.

### 3. Herseizoenen en afboeken

Week voor week vooruit: verwachte vraag = jaarniveau × seizoensgewicht van die
week × aandeel van de maat. Dat wordt van de voorraad afgehaald tot die op is.
**Die dag is de verwachte uitverkoopdatum.**

Het seizoensgewicht komt van het model zelf (kleurvariant), anders van de
modelfamilie, anders van merk × seizoen — twee volledige jaarcycli, elk apart
genormaliseerd.

### 4. Maatverdeling

Uit de eigen verkoophistorie van het model, waarbij de laatste 28 dagen drie
keer zo zwaar tellen, en de maatcurve van het merk als achtergrond voor maten met
weinig waarneming. Een nieuw model zonder historie krijgt zo toch een
realistische verdeling.

### 5. Signaal

| Status | Wanneer | Betekenis |
|---|---|---|
| **Leeg** | voorraad 0, er is vraag | er wordt nu omzet gemist |
| **Te laat** | leeg vóór de hersteltijd voorbij is | ook een bestelling van vandaag komt na het gat |
| **Bestel nu** | leeg binnen hersteltijd + 2 weken marge | nu bestellen landt precies op tijd |
| **Volgende week** | leeg binnen hersteltijd + 4 weken | in de gaten houden |
| OK | later | — |

Een model krijgt de status van zijn slechtste **kernmaat**: de maten die samen
80% van de vraag dragen. Een lege randmaat maakt het model niet rood.

### 6. Hersteltijd per merk — gemeten, niet aangenomen

Uit de weekhistorie in ShopifyQL: hoe lang stond een uitverkochte maat leeg
voordat hij terugkwam? De mediaan per merk is de **werkelijke hersteltijd**:
reactietijd plus levertijd samen. Dat is wat telt voor een signaal — niet wat de
leverancier belooft, maar hoe lang het bij jullie in de praktijk duurt.

Leegstand die langer dan twintig weken duurde telt apart: dat artikel is binnen
het seizoen nooit meer aangevuld.

Zodra een leverancier een echte levertijd opgeeft, gaat die voor.

---

## Collectie, seizoen en afprijzen

### Welke collectie loopt nu

| Collectie | In week 40 van 2026 | Signaal |
|---|---|---|
| **Lopend** | FW 2026 | volledig: bestellen als het op dreigt te raken |
| **Doorlopend** | NOOS, of een vlakke jaarcurve | volledig |
| **Net voorbij** | SS 2026 | geen besteladvies, wel restvoorraad bij seizoenseinde |
| **Vorig jaar** | FW 2025 | geen besteladvies |
| **Ouder** | alles daarvoor | geen besteladvies |
| Geen label | seizoensjaar ontbreekt | wel signaal, gemarkeerd |

Het NOOS-label is niet heilig: een artikel dat als NOOS staat maar 74% van zijn
jaar in dertien weken verkoopt wordt als seizoensartikel behandeld.

Daarnaast: een collectie waarvan 45% of meer al is afgeprijsd wordt opgeruimd.
Daar wordt niet in bijbesteld, ook niet als dit ene artikel nog volle prijs heeft.

### Wanneer piekt het seizoen, wanneer afprijzen

Per model uit zijn eigen curve:

- **Piek** — de week met de meeste vraag
- **Seizoensvenster** — van 8% tot 92% van de jaarvraag, gerekend vanaf het dal
- **Afprijzen vanaf** — de week waarin 70% van de seizoensvraag achter de rug is.
  Vanaf dan loopt de vraag terug en kost wachten meer dan een korting.
- **Restvoorraad bij het dal** — wat er bij het huidige tempo overblijft als het
  seizoen afloopt. Is dat meer dan nul, dan hoort afprijzen niet te wachten tot
  het vaste sale-moment.

## Kanalen

Er is **één voorraad**. Die wordt gespiegeld naar de eigen merkshop, de brede
shops (bartogi.nl / .de) en de marktplaatsen. Dus:

- **Vraag** wordt over alle kanalen opgeteld.
- **Voorraad** wordt één keer geteld, nooit per kanaal opgeteld.
- De radar toont per model de **verdeling van de vraag** over merkshop, brede
  shop en marktplaats.

Bij krapte zijn de kanalen niet gelijk. Een marktplaatsverkoop kost een fee en
komt vaker retour (27% tegen 2–11% in de eigen shops). Wanneer een kernmaat op
"te laat" staat, zijn de laatste paren daarom meer waard in de eigen shops. De
radar markeert dat; het afknijpen van de marktplaatsvoorraad zelf is een
instelling in ChannelEngine.

## Terugblik: hoe groot is het probleem

Voor de vijftig best verkopende modellen van het afgelopen jaar: welk deel van
het jaar waren ze volledig leverbaar, en hoeveel verkoop is er naar schatting
gemist in de dagen dat een kernmaat leeg stond. Dat laatste is een indicatie: het
rekent met het gemiddelde jaartempo, dus het overschat als de leegstand buiten
het seizoen viel en onderschat als het in de piek was.

## Bekende beperkingen

- Vraag is bruto: retouren worden niet afgetrokken. Voor een waarschuwing is dat
  de veilige kant, het signaal komt eerder.
- De seizoenscurve zelf is nog gebouwd op verkopen, dus ook gedrukt door
  leegstand in vorige jaren. Het jaarniveau is wel gecorrigeerd, de vorm nog
  niet.
- Prijzen en publicatiestatus komen uit de laatste volledige export; de voorraad
  en verkopen uit de radarrun zelf.
