# Trechterproject Hooijer webshops — gereedschap

Opnieuw opgebouwd op 22 september 2026. De oorspronkelijke `scratchpad/hooijer/`
uit eerdere sessies stond op een andere machine en is hier niet beschikbaar.

## Bestanden

| Bestand | Wat het doet |
|---|---|
| `shop.py` | toegang tot de Shopify Admin API per shop; `shop.gql(sleutel, query)` |
| `sql.py` | ShopifyQL-vragen; `sql.vraag(sleutel, query)` geeft een DataFrame |
| `controle_toegang.py` | levenstest over alle 17 shops |
| `nulmeting.py` | trechter + omzet per shop over een op te geven periode |
| `maandreeks.py` | sessies per maand per shop, om meetgaten te vinden |
| `rangschikking.py` | rangschikking op verwachte impact, op twee vensters |
| `bronnen_check.py` | trechter per verkeersbron voor losse shops en perioden |
| `spooksessies.py` | kwantificeert de piek okt-jan die nauwelijks converteerde |
| `venster_test.py` | leidt af welk twaalfmaandsvenster bij een nulmeting hoort |

Tokens komen uitsluitend uit omgevingsvariabelen en staan nergens in code of
uitvoer.

## Aanroepen

```bash
python3 nulmeting.py "SINCE -12m UNTIL today"
python3 nulmeting.py "SINCE 2026-06-01 UNTIL 2026-08-31"
```

Vereist `pandas`. ShopifyQL kent een eigen kostenplafond van 1000 punten per
minuut per shop; `sql.vraag` wacht vanzelf als het vol zit.

## Wat hier nog niet is

De datasets uit hoofdstuk 3 van het startpakket (`shop_regels.pkl`,
`kost_per_ean.pkl`, `merkweek.pkl`, `weekcijfers.pkl`, `alle_kanalen.pkl`,
`returnista*.pkl`, `ce_*.pkl`, `seizoen_per_ean.pkl`) ontbreken. Getest en
bevestigd is dat kostprijs per variant (`inventoryItem.unitCost`) en orders met
klantgeschiedenis en eerste-bezoekbron via de Admin API opnieuw op te halen
zijn. Targets per merk zijn dat niet: die komen uit een eigen bron.
