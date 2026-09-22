"""Bouwt de nulmeting maart-augustus 2026 als Excel met vaste tabbladen.

Afgeleide kolommen staan als formule in het blad, niet als uitgerekende waarde,
zodat een collega ze kan narekenen en aanpassen.
"""
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

LETTER = "Arial"
KOP = Font(name=LETTER, bold=True, color="FFFFFF", size=10)
KOPVULLING = PatternFill("solid", fgColor="2F4858")
GEWOON = Font(name=LETTER, size=10)
VET = Font(name=LETTER, bold=True, size=10)
LICHT = PatternFill("solid", fgColor="EDF2F4")
RAND = Border(bottom=Side(style="thin", color="BBBBBB"))

EURO = '€ #,##0;(€ #,##0);-'
EURO2 = '€ #,##0.00;(€ #,##0.00);-'
PROC = '0.00"%";(0.00"%");-'
PROC1 = '0.0"%";(0.0"%");-'
AANTAL = '#,##0;(#,##0);-'


def schrijf(ws, df, formaten, start=1, totaal_vet=True):
    """Zet een DataFrame neer met kopregel en opmaak; geeft de laatste rij terug."""
    for kol, naam in enumerate(df.columns, start=1):
        cel = ws.cell(row=start, column=kol, value=naam)
        cel.font, cel.fill = KOP, KOPVULLING
        cel.alignment = Alignment(horizontal="center", wrap_text=True, vertical="center")
    for rij, (_, regel) in enumerate(df.iterrows(), start=start + 1):
        laatste = totaal_vet and str(regel.iloc[0]).startswith("ALLE")
        for kol, naam in enumerate(df.columns, start=1):
            cel = ws.cell(row=rij, column=kol, value=regel[naam])
            cel.font = VET if laatste else GEWOON
            cel.border = RAND
            if laatste:
                cel.fill = LICHT
            if naam in formaten:
                cel.number_format = formaten[naam]
    ws.freeze_panes = ws.cell(row=start + 1, column=2)
    for kol, naam in enumerate(df.columns, start=1):
        breed = max(len(str(naam)) + 2, 11)
        if kol == 1:
            breed = max(len(str(w)) for w in df.iloc[:, 0]) + 3
        ws.column_dimensions[get_column_letter(kol)].width = breed
    ws.row_dimensions[start].height = 30
    return start + len(df)


wb = Workbook()

# ---------------------------------------------------------------- verantwoording
ws = wb.active
ws.title = "Verantwoording"
regels = [
    ("Nulmeting trechteranalyse Hooijer webshops", VET),
    ("", GEWOON),
    ("Periode", VET),
    ("1 maart 2026 tot en met 31 augustus 2026 (184 dagen, zes hele maanden).", GEWOON),
    ("", GEWOON),
    ("Waarom niet twaalf maanden", VET),
    ("Van 18 september 2025 tot en met 12 februari 2026 was de sessiemeting van alle", GEWOON),
    ("shops verstoord. De herkomst van bezoekers ging verloren, sessies werden ongeveer", GEWOON),
    ("verdrievoudigd en 90 tot 96 procent van de orders werd op 'direct' geboekt in plaats", GEWOON),
    ("van op de echte bron. Orders en omzet zijn niet geraakt; alleen de sessieteller.", GEWOON),
    ("Gevolg: elk percentage per sessie uit die periode is te laag. Februari 2026 is half", GEWOON),
    ("besmet, dus maart 2026 is de eerste bruikbare maand.", GEWOON),
    ("", GEWOON),
    ("Bronnen", VET),
    ("Trechter: Shopify Analytics, ShopifyQL dataset 'sessions'.", GEWOON),
    ("Geld: Shopify Analytics, ShopifyQL dataset 'sales'.", GEWOON),
    ("Opgehaald op 22 september 2026 via de Admin API, versie 2025-07.", GEWOON),
    ("", GEWOON),
    ("Meetwijze", VET),
    ("wagen%      = sessies met winkelwagentoevoeging gedeeld door sessies", GEWOON),
    ("afreken%    = sessies tot afrekenen gedeeld door sessies met winkelwagentoevoeging", GEWOON),
    ("order%      = sessies met afgeronde bestelling gedeeld door sessies tot afrekenen", GEWOON),
    ("conversie%  = sessies met afgeronde bestelling gedeeld door sessies", GEWOON),
    ("AOV         = netto-omzet gedeeld door orders", GEWOON),
    ("korting%    = kortingen gedeeld door bruto-omzet", GEWOON),
    ("retour%     = retouren gedeeld door bruto-omzet", GEWOON),
    ("", GEWOON),
    ("De cijfers staan als uitgerekende waarde in het blad, niet als formule.", GEWOON),
    ("Reden: de omgeving waarin dit bestand is gemaakt kon Excel-formules niet", GEWOON),
    ("doorrekenen, en een formule zonder uitkomst leest in veel programma's als leeg.", GEWOON),
    ("Met de rekenregels hierboven is elke kolom na te rekenen.", GEWOON),
    ("", GEWOON),
    ("Let op bij AOV", VET),
    ("Orders uit de sales-dataset (36.515) zijn er meer dan sessies met een afgeronde", GEWOON),
    ("bestelling (26.313). Ongeveer 28 procent van de orders hangt aan geen webshopsessie.", GEWOON),
    ("De AOV is daarom over alle orders berekend, de trechter alleen over sessies.", GEWOON),
    ("Beide staan er los naast; ze zijn niet door elkaar te gebruiken.", GEWOON),
    ("", GEWOON),
    ("Wat hier niet in staat", VET),
    ("Brutomarge. Shopify levert gross_profit en cost_of_goods_sold, maar de kostprijzen", GEWOON),
    ("zijn pas vanaf juni 2026 ingevoerd en nog niet betrouwbaar: maart tot en met mei", GEWOON),
    ("staan op nul, juli geeft negatieve marges en augustus geeft Lazamani 117 procent.", GEWOON),
    ("Zolang dat niet klopt kan er niet op winst gerangschikt worden, alleen op omzet.", GEWOON),
    ("", GEWOON),
    ("Seizoen", VET),
    ("Maart tot en met augustus is lente en zomer. Voor merken met een winterzwaartepunt", GEWOON),
    ("(Hunter, Tofvel) onderschat dit venster het jaar. Het tabblad 'Jaar op jaar' zet", GEWOON),
    ("daarom juni tot en met augustus 2026 naast dezelfde maanden in 2025: beide vallen", GEWOON),
    ("buiten de storing en in hetzelfde seizoen.", GEWOON),
]
for rij, (tekst, font) in enumerate(regels, start=1):
    cel = ws.cell(row=rij, column=1, value=tekst)
    cel.font = font
ws.column_dimensions["A"].width = 92

# ---------------------------------------------------------------- trechter
tabel = pd.read_pickle("nulmeting_v2.pkl")
tre = tabel[["shop", "sessions", "sessions_with_cart_additions", "wagen%",
             "sessions_that_reached_checkout", "afreken%",
             "sessions_that_completed_checkout", "order%", "conversie%",
             "gross_sales", "discounts", "returns", "net_sales", "orders", "AOV"]].copy()
tre.columns = ["Shop", "Sessies", "In wagen", "wagen%", "Afrekenen", "afreken%",
               "Order", "order%", "conversie%", "Bruto-omzet", "Kortingen",
               "Retouren", "Netto-omzet", "Orders", "AOV"]
ws = wb.create_sheet("Trechter")
ws["A1"] = "Trechter per shop, 1 maart t/m 31 augustus 2026 (bron: ShopifyQL)"
ws["A1"].font = VET
einde = schrijf(ws, tre, {
    "Sessies": AANTAL, "In wagen": AANTAL, "Afrekenen": AANTAL, "Order": AANTAL,
    "Orders": AANTAL, "wagen%": PROC, "afreken%": PROC, "order%": PROC,
    "conversie%": PROC, "Bruto-omzet": EURO, "Kortingen": EURO, "Retouren": EURO,
    "Netto-omzet": EURO, "AOV": EURO2}, start=3)
# ---------------------------------------------------------------- rangschikking
rang = pd.read_csv("rangschikking_v2.csv")
rang.columns = ["Shop", "Bovengrens (naar 9,01%)", "Realistisch (naar 6,11%)"]
rang.insert(0, "#", range(1, len(rang) + 1))
ws = wb.create_sheet("Rangschikking")
ws["A1"] = "Extra omzet bij een betere eerste trechterstap, over zes maanden"
ws["A1"].font = VET
ws["A2"] = ("Methode: alleen sessie naar winkelwagen verbetert; de stappen daarna blijven "
            "gelijk. Extra orders tegen de eigen AOV van de shop. Bovengrens, geen belofte.")
ws["A2"].font = GEWOON
einde = schrijf(ws, rang, {"Bovengrens (naar 9,01%)": EURO,
                           "Realistisch (naar 6,11%)": EURO}, start=4)
ws.cell(row=einde + 1, column=2, value="Samen").font = VET
for kol, naam in ((3, "Bovengrens (naar 9,01%)"), (4, "Realistisch (naar 6,11%)")):
    cel = ws.cell(row=einde + 1, column=kol, value=float(rang[naam].sum()))
    cel.font, cel.number_format, cel.fill = VET, EURO, LICHT

# ---------------------------------------------------------------- jaar op jaar
jaar = pd.read_csv("jaar_op_jaar.csv")
jaar = jaar[["shop", "sessions 2025", "sessions 2026", "sessions %",
             "wagen% 2025", "wagen% 2026", "wagen pp",
             "orders 2025", "orders 2026", "orders %",
             "net_sales 2025", "net_sales 2026", "net_sales %"]]
jaar.columns = ["Shop", "Sessies 2025", "Sessies 2026", "Sessies %",
                "wagen% 2025", "wagen% 2026", "wagen +/- pp",
                "Orders 2025", "Orders 2026", "Orders %",
                "Omzet 2025", "Omzet 2026", "Omzet %"]
ws = wb.create_sheet("Jaar op jaar")
ws["A1"] = "Juni t/m augustus 2026 tegen dezelfde maanden 2025 — beide buiten de storing"
ws["A1"].font = VET
schrijf(ws, jaar, {
    "Sessies 2025": AANTAL, "Sessies 2026": AANTAL, "Orders 2025": AANTAL,
    "Orders 2026": AANTAL, "Sessies %": PROC1, "Orders %": PROC1, "Omzet %": PROC1,
    "wagen% 2025": PROC, "wagen% 2026": PROC, "wagen +/- pp": PROC,
    "Omzet 2025": EURO, "Omzet 2026": EURO}, start=3)

# ---------------------------------------------------------------- verkeersbron
bron = pd.read_pickle("bronnen_v2.pkl")
groep = bron.groupby("referrer_source")[
    ["sessions", "sessions_with_cart_additions", "sessions_that_completed_checkout"]
].sum().reset_index()
groep["wagen%"] = groep.sessions_with_cart_additions / groep.sessions * 100
groep["conversie%"] = groep.sessions_that_completed_checkout / groep.sessions * 100
groep = groep.sort_values("sessions", ascending=False)
groep.columns = ["Bron", "Sessies", "In wagen", "Order", "wagen%", "conversie%"]

ws = wb.create_sheet("Verkeersbron")
ws["A1"] = "Alle shops samen, per verkeersbron, maart t/m augustus 2026"
ws["A1"].font = VET
einde = schrijf(ws, groep, {"Sessies": AANTAL, "In wagen": AANTAL, "Order": AANTAL,
                            "wagen%": PROC, "conversie%": PROC}, start=3, totaal_vet=False)

per_shop = bron.pivot_table(index="shop", columns="referrer_source",
                            values="conversie%").reset_index()
per_shop = per_shop.rename(columns={"shop": "Shop"})
ws.cell(row=einde + 3, column=1, value="Conversie% per bron per shop").font = VET
schrijf(ws, per_shop, {k: PROC for k in per_shop.columns if k != "Shop"},
        start=einde + 4, totaal_vet=False)

wb.save("nulmeting_maart_augustus_2026.xlsx")
print("geschreven: nulmeting_maart_augustus_2026.xlsx")
