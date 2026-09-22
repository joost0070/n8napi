"""De brug: waarom haalt Bartogi NL 7,05% en Bartogi DE 21,76%?

Alles uitgedrukt in procentpunten van de eigen bruto omzet, zodat de posten
optellen tot de brutowinstmarge en het verschil te ontleden is.
Bron: MT-rapportage 'Week + YTD', regel 33 en 34.
"""
import pandas as pd

NL = dict(bruto=187792.86, korting=10108.55, retour=31250.48, verzendopbrengst=5403.24,
          netto=151837.07, inkoop=78231.30, payment=1464.50, verzend=19608.00,
          advertentie=39286.05, winst=13246.69, orders=3280)
DE = dict(bruto=152950.62, korting=6262.83, retour=24586.81, verzendopbrengst=4373.89,
          netto=126474.87, inkoop=59070.93, payment=4737.00, verzend=15957.50,
          advertentie=13424.43, winst=33284.49, orders=2455)

POSTEN = [("kortingen", "korting", -1), ("retouren", "retour", -1),
          ("verzendopbrengsten", "verzendopbrengst", +1), ("inkoopkosten", "inkoop", -1),
          ("payment costs", "payment", -1), ("verzendkosten", "verzend", -1),
          ("advertentiekosten", "advertentie", -1)]

print("=== opbouw van de brutowinstmarge, in % van de eigen bruto omzet ===\n")
print(f"{'post':<22}{'Bartogi NL':>14}{'Bartogi DE':>14}{'verschil':>12}")
print(f"{'bruto omzet':<22}{'100,00%':>14}{'100,00%':>14}{'':>12}")
brug = []
for naam, sleutel, teken in POSTEN:
    a, b = NL[sleutel] / NL["bruto"] * 100, DE[sleutel] / DE["bruto"] * 100
    bij = teken * (a - b)
    brug.append((naam, bij))
    print(f"{naam:<22}{teken*a:>13.2f}%{teken*b:>13.2f}%{bij:>11.2f}pp")
print(f"{'-'*62}")
print(f"{'brutowinstmarge':<22}{NL['winst']/NL['bruto']*100:>13.2f}%"
      f"{DE['winst']/DE['bruto']*100:>13.2f}%"
      f"{(NL['winst']/NL['bruto']-DE['winst']/DE['bruto'])*100:>11.2f}pp")

print("\n=== waar zit het gat van 14,7 procentpunt? ===")
gat = sum(b for _, b in brug)
for naam, bij in sorted(brug, key=lambda t: t[1]):
    if abs(bij) >= 0.01:
        print(f"  {naam:<22}{bij:>8.2f}pp   {abs(bij)/abs(gat)*100:>5.0f}% van het gat"
              + ("   (NL beter)" if bij > 0 else ""))

print("\n\n=== wat is er nodig voor 20%? ===")
doel = 0.20 * NL["bruto"]
print(f"  brutowinst nu       € {NL['winst']:>9,.0f}   ({NL['winst']/NL['bruto']*100:.2f}%)"
      .replace(",", "."))
print(f"  brutowinst bij 20%  € {doel:>9,.0f}")
print(f"  tekort              € {doel-NL['winst']:>9,.0f}\n".replace(",", "."))

for naam, sleutel, doelpct, uitleg in [
    ("advertentie naar DE-niveau", "advertentie", DE["advertentie"]/DE["bruto"], "8,78%"),
    ("advertentie naar 12%", "advertentie", 0.12, "12%"),
    ("advertentie naar 15%", "advertentie", 0.15, "15%"),
    ("inkoop naar DE-niveau", "inkoop", DE["inkoop"]/DE["bruto"], "38,62%"),
    ("kortingen naar DE-niveau", "korting", DE["korting"]/DE["bruto"], "4,09%"),
    ("retouren naar DE-niveau", "retour", DE["retour"]/DE["bruto"], "16,07%"),
]:
    besparing = NL[sleutel] - doelpct * NL["bruto"]
    nieuw = (NL["winst"] + besparing) / NL["bruto"] * 100
    print(f"  {naam:<30} ({uitleg:>7}): € {besparing:>8,.0f} erbij  ->  marge {nieuw:>5.2f}%"
          .replace(",", "."))

print("\n\n=== verzendeconomie Bartogi NL ===")
per_order_kosten = NL["verzend"] / NL["orders"]
per_order_opbrengst = NL["verzendopbrengst"] / NL["orders"]
print(f"  {NL['orders']:,} orders".replace(",", "."))
print(f"  verzendkosten     € {NL['verzend']:>8,.0f}  = € {per_order_kosten:.2f} per order"
      .replace(",", "."))
print(f"  verzendopbrengst  € {NL['verzendopbrengst']:>8,.0f}  = € {per_order_opbrengst:.2f} per order"
      .replace(",", "."))
print(f"  verlies           € {NL['verzend']-NL['verzendopbrengst']:>8,.0f}  = "
      f"€ {per_order_kosten-per_order_opbrengst:.2f} per order  "
      f"({(NL['verzend']-NL['verzendopbrengst'])/NL['bruto']*100:.2f}% van de bruto omzet)"
      .replace(",", "."))
print(f"  gemiddelde orderwaarde € {NL['bruto']/NL['orders']:.2f}")
