"""Verzendeconomie en retourpakketten bij Bartogi NL, uit de Shopify-orderregels.

De MT-rapportage rekent € 6,00 verzendkosten per order. Dat is alleen heenweg:
19.608 / 6,00 = 3.268 orders, precies het aantal orders. De retourzending zit
er dus niet in.
"""
import pandas as pd
pd.set_option("display.width", 210)

VERZENDKOSTEN = 6.00
RETOURKOSTEN = 6.00   # zelfde tarief voor de retourzending; aanname

for sleutel, naam in (("bartogi_nl", "Bartogi NL"), ("bartogi_de", "Bartogi DE")):
    d = pd.read_pickle(f"bar_regels_{sleutel}.pkl")
    orders = d.groupby("order").agg(
        datum=("datum", "first"), bruto=("bruto", "sum"), netto=("netto", "sum"),
        verzendopbrengst=("verzendopbrengst", "first"),
        inkoop=("kostprijs", lambda s: 0),  # apart hieronder
        stuks=("aantal", "sum"), stuks_nu=("aantal_nu", "sum"),
        bron=("eerste_bron", "first"), klantorders=("orders_van_klant", "first")).reset_index()
    kost = d.assign(k=d.kostprijs * d.aantal).groupby("order").k.sum()
    kost_nu = d.assign(k=d.kostprijs * d.aantal_nu).groupby("order").k.sum()
    netto_nu = d.assign(n=d.netto * d.aantal_nu / d.aantal.replace(0, 1)).groupby("order").n.sum()
    orders["inkoop"] = orders.order.map(kost)
    orders["inkoop_nu"] = orders.order.map(kost_nu)
    orders["netto_nu"] = orders.order.map(netto_nu)
    orders["volledig_retour"] = orders.stuks_nu == 0
    orders["deels_retour"] = (orders.stuks_nu > 0) & (orders.stuks_nu < orders.stuks)
    orders["retourpakket"] = orders.stuks_nu < orders.stuks

    n = len(orders)
    print(f"\n{'='*100}\n=== {naam}: {n:,} orders ===".replace(",", "."))
    print(f"  gemiddelde orderwaarde (bruto)  € {orders.bruto.mean():.2f}")
    print(f"  orders met een retour           {orders.retourpakket.sum():,} "
          f"({orders.retourpakket.mean()*100:.1f}%)".replace(",", "."))
    print(f"  waarvan volledig geretourneerd  {orders.volledig_retour.sum():,} "
          f"({orders.volledig_retour.mean()*100:.1f}%)".replace(",", "."))
    verborgen = orders.retourpakket.sum() * RETOURKOSTEN
    print(f"  retourzendingen a € {RETOURKOSTEN:.2f}      € {verborgen:,.0f}  "
          f"= {verborgen/orders.bruto.sum()*100:.2f}% van de bruto omzet"
          .replace(",", "."))
    print(f"  -> die post zit NIET in de MT-rapportage")

    print(f"\n  -- orderwaarde en dekkingsbijdrage per schijf --")
    orders["schijf"] = pd.cut(orders.bruto, [0, 25, 40, 50, 60, 75, 100, 150, 1e6],
                    labels=["< 25", "25-40", "40-50", "50-60", "60-75", "75-100",
                            "100-150", "150+"])
    g = orders.groupby("schijf", observed=True).agg(
        orders=("order", "count"), omzet=("bruto", "sum"),
        netto_nu=("netto_nu", "sum"), inkoop_nu=("inkoop_nu", "sum"),
        verzendopbr=("verzendopbrengst", "sum"),
        retourpakketten=("retourpakket", "sum")).reset_index()
    g["aandeel orders%"] = g.orders / n * 100
    g["productmarge na retour"] = g.netto_nu - g.inkoop_nu
    g["verzendlast"] = g.orders * VERZENDKOSTEN + g.retourpakketten * RETOURKOSTEN - g.verzendopbr
    g["na verzending"] = g["productmarge na retour"] - g.verzendlast
    g["per order"] = g["na verzending"] / g.orders
    print(g[["schijf", "orders", "aandeel orders%", "omzet",
             "productmarge na retour", "verzendlast", "na verzending", "per order"]]
          .rename(columns={"schijf": "orderwaarde"}).to_string(
        index=False, float_format=lambda v: f"{v:,.0f}"))
    if sleutel == "bartogi_nl":
        orders.to_pickle("bar_orders_nl.pkl")
