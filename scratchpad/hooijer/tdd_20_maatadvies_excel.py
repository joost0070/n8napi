"""Tofvel maatadvies per model naar tofvel_maatadvies_per_model.xlsx (waarden).

Opbouw naar voorbeeld van de Lazamani-retouranalyse, maar met te klein en te smal,
te groot en te wijd, en instap/wreef als aparte redenen.
"""
import pandas as pd
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

d = pd.read_pickle("tdd_maatadvies.pkl")
m, per_maat = d["model"].copy(), d["maat"].copy()
ret = pd.read_pickle("tdd_retouren_los.pkl")

VOLGORDE = ["Te klein (lengte)", "Te groot (lengte)", "Instap te krap / hoge wreef",
            "Te smal (breedte)", "Te wijd / hiel slipt eruit", "Links/rechts verschilt",
            "Zool / comfort / geluid", "Pasvorm, niet toegelicht", "Kwaliteit / overig"]

ADVIES = {
    "Mula": ("Valt klein in maat 36-40 en 44+; maat 41-43 valt normaal. Hoge wreef: grotere "
             "maat helpt niet, verwijs naar Slipa / Slipa Maha.",
             "hoog (252 retourregels, 62 omruilingen)"),
    "Rabara": ("Valt normaal tot iets klein; bij twijfel de grotere maat.",
               "laag (38 retourregels)"),
    "Rabara Maha": ("Valt op maat (te groot en te klein houden elkaar in evenwicht). Aandacht "
                    "voor hoge wreef (12%) en verschil links/rechts (8%): terugkoppelen aan "
                    "leverancier.", "middel (49 retourregels)"),
    "Slipa Maha": ("Valt ruim, vooral vanaf maat 44: bij twijfel de kleinere maat. Open hiel kan "
                   "loslaten; stevige rubberzool is stug en hoorbaar op harde vloer.",
                   "middel (33 retourregels)"),
    "Slipa": ("Te weinig retourredenen voor een uitspraak (4).", "te weinig data"),
    "Luna Kids": ("Te weinig data (5); 3 van 5 'te klein': groeiruimte noemen.", "te weinig data"),
    "Celsi": ("Te weinig data (3).", "te weinig data"),
    "Sundara": ("Te weinig data (4).", "te weinig data"),
    "Mula Lungta": ("Zelfde leest als Mula: zelfde advies.", "via Mula"),
}

TEKSTEN = [
    ("Mula (ook Mula Lungta)", "NL",
     "Maatadvies: de Mula valt klein. Heb je maat 36 t/m 40 of 44 en groter, kies dan één maat "
     "groter dan je gewone schoenmaat. Bij maat 41 t/m 43 kies je je gewone maat. "
     "Van de klanten die ruilden, koos ruim 9 op de 10 een grotere maat.\n"
     "Hoge wreef? De Mula heeft een gesloten instap. Een grotere maat maakt die opening niet "
     "ruimer. Kies dan de Slipa of Slipa Maha met open instap."),
    ("Mula (ook Mula Lungta)", "DE",
     "Größenberatung: Der Mula fällt klein aus. Bei Größe 36 bis 40 sowie ab 44 empfehlen wir "
     "eine Nummer größer als Ihre übliche Schuhgröße. Bei 41 bis 43 wählen Sie Ihre normale "
     "Größe.\nHoher Spann? Der Mula hat einen geschlossenen Einstieg, der durch eine größere "
     "Größe nicht weiter wird. Wählen Sie dann den Slipa oder Slipa Maha mit offenem Einstieg."),
    ("Rabara", "NL",
     "Maatadvies: de Rabara valt normaal tot iets klein. Twijfel je tussen twee maten, kies dan "
     "de grotere."),
    ("Rabara", "DE",
     "Größenberatung: Der Rabara fällt normal bis leicht klein aus. Im Zweifel die größere "
     "Größe wählen."),
    ("Rabara Maha", "NL",
     "Maatadvies: de Rabara Maha valt op maat; kies je gewone schoenmaat.\n"
     "Hoge wreef? Kies de Slipa Maha met lage instap.\n"
     "Stevige rubberzool: slijtvast en geschikt voor buiten. Zoek je een zachte zool, kies dan "
     "de Mula."),
    ("Rabara Maha", "DE",
     "Größenberatung: Der Rabara Maha fällt normal aus; wählen Sie Ihre übliche Größe.\n"
     "Hoher Spann? Wählen Sie den Slipa Maha mit niedrigem Einstieg.\n"
     "Feste Gummisohle: strapazierfähig und auch für draußen. Für eine weiche Sohle wählen Sie "
     "den Mula."),
    ("Slipa Maha", "NL",
     "Maatadvies: de Slipa Maha valt ruim, vooral vanaf maat 44. Twijfel je, kies dan de "
     "kleinere maat.\nOpen hiel: heb je een smalle voet of hiel, dan kan je hiel eruit glippen. "
     "Kies dan de Rabara Maha, die hoger om de voet sluit.\nStevige rubberzool: slijtvast, "
     "maar stugger dan een leren zool en hoorbaar op laminaat of tegels."),
    ("Slipa Maha", "DE",
     "Größenberatung: Der Slipa Maha fällt groß aus, besonders ab Größe 44. Im Zweifel die "
     "kleinere Größe wählen.\nOffene Ferse: Bei schmalem Fuß kann die Ferse herausrutschen; "
     "dann ist der höher geschnittene Rabara Maha die bessere Wahl.\nFeste Gummisohle: "
     "strapazierfähig, aber fester als eine Ledersohle und auf Laminat oder Fliesen hörbar."),
    ("Luna Kids", "NL",
     "Maatadvies: kies bij twijfel een maat groter, dan heeft de voet ruimte om te groeien."),
]

for c in VOLGORDE:
    if c not in m:
        m[c] = 0
m = m.reset_index().rename(columns={"index": "model"})
m["advies"] = m.model.map(lambda x: ADVIES.get(x, ("", ""))[0])
m["betrouwbaarheid"] = m.model.map(lambda x: ADVIES.get(x, ("", ""))[1])
m = m[["model", "verkocht", "retour", "retour_%", "returnista_n"] + VOLGORDE +
      ["omruil_n", "maat_omhoog", "maat_omlaag", "advies", "betrouwbaarheid"]]
m = m.sort_values("verkocht", ascending=False).round(1)
m.columns = ["Model", "Verkocht (okt 24-aug 26)", "Retour paren", "Retour %",
             "Retourregels met reden (2026)"] + [f"% {c}" for c in VOLGORDE] + \
            ["Omruilingen", "Maat omhoog", "Maat omlaag", "Advies", "Betrouwbaarheid"]

per_maat = per_maat[per_maat.verkocht >= 20].round(1)
per_maat.columns = ["Model", "Maat", "Verkocht", "Retour paren", "Retour %"]

a = pd.concat([pd.read_pickle(f"assortiment_tofvel_{s}.pkl") for s in ["nl", "de"]]).drop_duplicates("sku")
a["sku"] = a.sku.astype(str).str.zfill(13)
ret["sku"] = ret.SKU.astype(str).str.split(".").str[0].str.zfill(13)
ret = ret.merge(a[["sku", "maat"]], on="sku", how="left")
ret["maatgroep"] = pd.to_numeric(ret.maat, errors="coerce").map(
    lambda v: "35-37" if v <= 37 else ("38-40" if v <= 40 else ("41-43" if v <= 43 else "44+")))
mx = pd.crosstab([ret.model, ret.maatgroep], ret.reden_los).reindex(columns=VOLGORDE, fill_value=0)
mx["Totaal"] = mx.sum(axis=1)
mx = mx.reset_index().rename(columns={"model": "Model", "maatgroep": "Maatgroep"})

voorb = ret.dropna(subset=["return_reason_comment"])[
    ["model", "maat", "reden_los", "Return reasons description", "return_reason_comment"]]
voorb.columns = ["Model", "Maat", "Reden (los)", "Reden Returnista", "Toelichting klant"]

samen = [
    ("Tofvel NL + DE, maatadvies per model", ""),
    ("", ""),
    ("Waarom deze analyse", "In het vorige document stonden 'te klein' en 'te smal' samen. Bij "
     "sloffen zijn dat verschillende problemen met een andere oplossing: te klein los je op met "
     "een grotere maat, een te krappe instap of hoge wreef niet."),
    ("Bronnen", "Retourpercentage per model en maat: Shopify-orders okt 2024 - aug 2026 "
     "(NL + DE, webshop), geretourneerde paren incl. omruil. Redenen: Returnista jan - 23 sep 2026 "
     "(388 regels). 'Pasvorm anders dan verwacht' en 'Kwaliteit' zijn opgesplitst op basis van de "
     "toelichting van de klant (106 toelichtingen). Omruilrichting: omruilorder in Shopify "
     "gekoppeld aan de oorspronkelijke order (100 van 107 omruilingen)."),
    ("Belangrijkste uitkomst", "Mula (72% van alle retourregels) valt klein in maat 36-40 en 44+: "
     "85 keer 'te klein' tegen 2 keer 'te groot' in 38-40. Bij omruilen koos 57 van de 62 klanten "
     "één maat groter. Daarnaast gaat 14% van de Mula-retouren over een te krappe instap of hoge "
     "wreef; meerdere klanten schrijven dat een grotere maat dat niet oplost."),
    ("", "Slipa Maha valt juist ruim (30% te groot) en krijgt klachten over de stugge, hoorbare "
     "rubberzool (21%). Rabara Maha valt op maat; aandachtspunten zijn hoge wreef en verschil "
     "tussen linker en rechter slof (handwerk)."),
    ("Terugkoppeling leverancier", "9 retouren (Mula 5, Rabara Maha 4) gaan over een verschil "
     "tussen links en rechts; 3 over een bobbel of scheve zool. Dat is kwaliteitscontrole, geen "
     "maatadvies."),
    ("Let op", "Aantallen per model buiten Mula zijn klein; kijk naar de kolom Betrouwbaarheid. "
     "Retourpercentage Shopify telt omruilingen mee en ligt daarom hoger dan het "
     "geld-terug-percentage."),
]

with pd.ExcelWriter("tofvel_maatadvies_per_model.xlsx", engine="openpyxl") as x:
    pd.DataFrame(samen, columns=["", " "]).to_excel(x, sheet_name="Samenvatting", index=False)
    m.to_excel(x, sheet_name="Per model", index=False)
    pd.DataFrame(TEKSTEN, columns=["Model", "Taal", "Tekst voor productpagina"]).to_excel(
        x, sheet_name="Teksten productpagina", index=False)
    mx.to_excel(x, sheet_name="Redenen per maatgroep", index=False)
    per_maat.to_excel(x, sheet_name="Retour% per maat", index=False)
    voorb.to_excel(x, sheet_name="Toelichtingen klanten", index=False)
    for ws in x.book.worksheets:
        for rij in ws.iter_rows():
            for c in rij:
                c.font = Font(name="Arial", size=10, bold=c.row == 1,
                              color="FFFFFF" if c.row == 1 else "000000")
                c.alignment = Alignment(wrap_text=True, vertical="top")
                if c.row == 1:
                    c.fill = PatternFill("solid", fgColor="1F4E78")
        for i, kol in enumerate(ws.columns, 1):
            breedte = max(len(str(c.value or "")) for c in list(kol)[:100])
            ws.column_dimensions[get_column_letter(i)].width = min(max(9, breedte + 2), 70)
        ws.freeze_panes = "A2"
    x.book["Samenvatting"].column_dimensions["A"].width = 28
    x.book["Samenvatting"].column_dimensions["B"].width = 110
    x.book["Teksten productpagina"].column_dimensions["C"].width = 110
print(m.iloc[:, [0, 1, 3, 5, 6, 7, 8, 9, 10, 11]].to_string())
