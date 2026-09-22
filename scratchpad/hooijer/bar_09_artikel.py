"""Bartogi NL en DE: winst-en-verliesrekening per artikel.

Toerekening, in lijn met hoe de MT-rapportage de posten uitdrukt:
  advertentie en payment : naar rato van de bruto omzet (vast % van de omzet)
  verzendkosten          : per verkocht stuk (het is een pakketkost, geen omzetkost)
  verzendopbrengsten     : per verkocht stuk
  retouren               : per artikel gemeten uit de orderregels
Bedragen exclusief btw. Shopify-orderregels staan inclusief btw en worden
gedeeld door 1,21 (NL) respectievelijk 1,19 (DE).

Bodemprijs = de verkoopprijs waarbij dit artikel exact 20% brutowinstmarge
haalt, gegeven zijn eigen inkoopprijs en retourpercentage:
    P = ( C(1-r) + verzendkosten/stuk - verzendopbrengst/stuk )
        / ( (1-r) - payment% - advertentie% - 0,20 )
"""
import pandas as pd

BTW = {"bartogi_nl": 1.21, "bartogi_de": 1.19}
# YTD uit de MT-rapportage, exclusief btw
KOSTEN = {
    "bartogi_nl": dict(advertentie=39286.05, payment=1464.50, verzend=19608.00,
                       verzendopbrengst=5403.24, bruto=187792.86),
    "bartogi_de": dict(advertentie=13424.43, payment=4737.00, verzend=15957.50,
                       verzendopbrengst=4373.89, bruto=152950.62),
}
DOEL = 0.20


def bouw(sleutel: str) -> pd.DataFrame:
    btw, k = BTW[sleutel], KOSTEN[sleutel]
    r = pd.read_pickle(f"bar_regels_{sleutel}.pkl").copy()
    a = pd.read_pickle(f"assortiment_{sleutel}.pkl")
    r["vanprijs"] = r.sku.map(a[a.vanprijs > 0].groupby("sku").vanprijs.median())

    r["bruto_ex"] = r.bruto / btw                      # voor kortingcode, incl afprijzing
    r["netto_ex"] = r.netto / btw                      # na kortingcode
    r["lijst_ex"] = (r.vanprijs.fillna(0) * r.aantal) / btw
    r.loc[r.lijst_ex < r.bruto_ex, "lijst_ex"] = r.bruto_ex
    deel = r.aantal_nu / r.aantal.replace(0, 1)
    r["omzet_na_retour"] = r.netto_ex * deel
    r["inkoop_na_retour"] = r.kostprijs * r.aantal_nu
    r["retourwaarde"] = r.netto_ex - r.omzet_na_retour
    r["afprijzing"] = (r.lijst_ex - r.bruto_ex) * deel

    stuks = r.aantal.sum()
    adv_pct = k["advertentie"] / k["bruto"]
    pay_pct = k["payment"] / k["bruto"]
    verz_stuk = k["verzend"] / stuks
    opbr_stuk = k["verzendopbrengst"] / stuks

    g = r.groupby(["merk", "sku", "artikel", "maat"], dropna=False).agg(
        stuks=("aantal", "sum"), stuks_retour=("geretourneerd", "sum")
        if "geretourneerd" in r else ("aantal", "size"),
        lijst=("lijst_ex", "sum"), bruto=("bruto_ex", "sum"), netto=("netto_ex", "sum"),
        afprijzing=("afprijzing", "sum"), omzet=("omzet_na_retour", "sum"),
        inkoop=("inkoop_na_retour", "sum"), retour=("retourwaarde", "sum"),
        kostprijs=("kostprijs", "median"), vanprijs=("vanprijs", "median"),
    ).reset_index()
    g["stuks_retour"] = r.assign(x=r.aantal - r.aantal_nu).groupby(
        ["merk", "sku", "artikel", "maat"], dropna=False).x.sum().values

    g["advertentie"] = g.bruto * adv_pct
    g["payment"] = g.bruto * pay_pct
    g["verzendkosten"] = g.stuks * verz_stuk
    g["verzendopbrengst"] = g.stuks * opbr_stuk
    g["brutowinst"] = (g.omzet - g.inkoop + g.verzendopbrengst
                       - g.verzendkosten - g.payment - g.advertentie)
    g["marge%"] = g.brutowinst / g.bruto * 100
    g["afprijzing%"] = g.afprijzing / g.lijst * 100
    g["retour%"] = g.stuks_retour / g.stuks * 100
    g["tekort tot 20%"] = DOEL * g.bruto - g.brutowinst
    g["prijs nu"] = g.bruto / g.stuks

    noemer = (1 - g["retour%"] / 100) - pay_pct - adv_pct - DOEL
    g["bodemprijs"] = ((g.kostprijs * (1 - g["retour%"] / 100) + verz_stuk - opbr_stuk)
                       / noemer.where(noemer > 0.02))
    g["bodemprijs incl btw"] = g.bodemprijs * btw
    g["prijs moet omhoog met"] = g["bodemprijs incl btw"] - g["prijs nu"] * btw
    g["shop"] = sleutel
    return g, dict(adv_pct=adv_pct, pay_pct=pay_pct, verz_stuk=verz_stuk,
                   opbr_stuk=opbr_stuk, stuks=stuks)


if __name__ == "__main__":
    pd.set_option("display.width", 230, "display.max_colwidth", 34)
    alles = []
    for sleutel, naam in (("bartogi_nl", "Bartogi NL"), ("bartogi_de", "Bartogi DE")):
        g, p = bouw(sleutel)
        alles.append(g)
        print(f"\n{'='*105}\n=== {naam}: {len(g):,} artikelen (ean x maat), "
              f"{p['stuks']:,.0f} stuks verkocht".replace(",", "."))
        print(f"    advertentie {p['adv_pct']*100:.2f}% van de omzet | payment "
              f"{p['pay_pct']*100:.2f}% | verzendkosten € {p['verz_stuk']:.2f} per stuk | "
              f"verzendopbrengst € {p['opbr_stuk']:.2f} per stuk")
        print(f"    optelsom brutowinst: € {g.brutowinst.sum():,.0f} op bruto omzet "
              f"€ {g.bruto.sum():,.0f} = {g.brutowinst.sum()/g.bruto.sum()*100:.2f}%"
              .replace(",", "."))
    pd.concat(alles).to_pickle("bar_artikelen.pkl")
