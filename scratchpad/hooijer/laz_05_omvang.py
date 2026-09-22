"""Hoe groot is het EN-verzendprobleem werkelijk?

Let op: de huidige AOV van EN (€ 59,75) is vertekend. De drempel van € 150 laat
vooral grote mandjes door. Wie het verzendtarief weghaalt, krijgt ook kleinere
orders erbij, dus rekenen we met de AOV van de zusterwinkels.
"""
import pandas as pd

MARGE = 0.66          # geijkte catalogusmarge Lazamani
basis = pd.read_pickle("nulmeting_v2.pkl")
en = basis[basis.sleutel == "lazamani_en"].iloc[0]
nl = basis[basis.sleutel == "lazamani_nl"].iloc[0]
de = basis[basis.sleutel == "lazamani_de"].iloc[0]
zuster_aov = (nl.net_sales + de.net_sales) / (nl.orders + de.orders)

print(f"Lazamani EN nu: {en.sessions:,.0f} sessies, {en['wagen%']:.2f}% wagen, "
      f"{en['afreken%']:.1f}% afrekenen, {en['order%']:.1f}% order".replace(",", "."))
print(f"  AOV EN € {en.AOV:.2f} — maar 92% betaalt verzendkosten en 8% haalt € 150")
print(f"  AOV van NL en DE samen: € {zuster_aov:.2f}\n")

verzendopbrengst = 310 * 5.9   # gemeten gemiddelde verzendkosten per order
for doel, naam in ((de["order%"], "niveau van Lazamani DE"),
                   (nl["order%"], "niveau van Lazamani NL")):
    afrekenaars = en.sessions * en["wagen%"] / 100 * en["afreken%"] / 100
    extra = afrekenaars * (doel - en["order%"]) / 100
    for aov, label in ((zuster_aov, "tegen zuster-AOV"), (en.AOV, "tegen huidige AOV")):
        omzet = extra * aov - verzendopbrengst
        print(f"  naar {naam} ({doel:.1f}%), {label} € {aov:.2f}:")
        print(f"     {extra:,.0f} extra orders, € {omzet:,.0f} netto-omzet per half jaar, "
              f"brutowinst € {omzet*MARGE:,.0f}  (€ {omzet*MARGE*2:,.0f} per jaar)"
              .replace(",", "."))
    print()

print("Ter vergelijking, wat in de eerdere controletabel stond: € 37.489 per jaar.")
print("Dat cijfer gebruikte de vertekende AOV van € 59,75 en telde ook stap 1 mee.")
