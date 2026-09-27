"""Tofvel-deepdive: weekcijfers en targets uit het MT-rapport (uploadbestand).

Schrijft tdd_mt_weken.pkl (per week per Tofvel-kanaal) en tdd_mt_targets.pkl.
"""
import re
import pandas as pd

F = "bartogi/2026 _ MT-rapportage _ Omzet en kosten Week en YTD (3).xlsx"
# kolomkop (begin) -> eigen naam; de weektabbladen verschillen in opbouw
KOL = {"Webshop": "kanaal", "Bruto weektarget": "target", "Bruto omzet": "bruto",
       "Kortingen": "korting", "Retouren": "retour", "Verzend": "verzendopbrengst",
       "Netto omzet": "netto", "Inkoopkosten": "inkoop", "Payment": "payment",
       "Platformkosten": "payment", "Verzendkosten": "verzendkosten",
       "Advertentiekosten": "advertentie", "Brutowinst": "brutowinst"}


def kolommen(koprij):
    uit = {}
    for i, v in enumerate(koprij):
        v = " ".join(str(v).split())
        for begin, naam in KOL.items():
            if v.startswith(begin) and naam not in uit.values() and \
                    not v.endswith(("percentage", "marge")):
                uit[i] = naam
                break
    return uit

x = pd.ExcelFile(F)
rijen = []
for tab in x.sheet_names:
    m = re.match(r"Week (\d+) \+ YTD", tab)
    if not m:
        continue
    df = pd.read_excel(F, sheet_name=tab, header=None)
    kop = df.index[df[1].astype(str).str.contains("Webshop", na=False)]
    if len(kop) < 2:  # week 25 heeft alleen een YTD-blok: overslaan
        continue
    kol = kolommen(df.iloc[kop[0]].tolist())
    weekblok = df.iloc[kop[0] + 1: kop[1]] if len(kop) > 1 else df.iloc[kop[0] + 1:]
    for _, r in weekblok.iterrows():
        if str(r[1]).startswith("Tofvel"):
            rij = {"week": int(m.group(1))}
            rij.update({naam: r[i] for i, naam in kol.items()})
            rijen.append(rij)
weken = pd.DataFrame(rijen).sort_values(["kanaal", "week"])
for k in set(KOL.values()):
    if k != "kanaal":
        weken[k] = pd.to_numeric(weken[k], errors="coerce").fillna(0)
weken.to_pickle("tdd_mt_weken.pkl")

wt = pd.read_excel(F, sheet_name="Weektargets", header=0)
wt = wt[["Week", "Weekstart", "Tofvel"]].dropna()
wt.to_pickle("tdd_mt_targets.pkl")

pd.set_option("display.width", 250)
print(weken.to_string())
print(wt.to_string())
