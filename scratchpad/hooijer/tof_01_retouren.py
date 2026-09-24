"""Tofvel NL en DE: retouren per model, vóór het seizoen begint."""
import re
import pandas as pd
import sql
pd.set_option("display.width", 230, "display.max_colwidth", 60)

oud = pd.read_pickle("retouren.pkl")
oud = oud[oud.shopcode.isin(["TONL", "TODE"])]
nieuw = pd.read_csv("retouren/tofvel_tot_20260923.csv").drop(columns=["Consumer email"])
nieuw["shopcode"] = nieuw["Order number"].str.extract(r"^([A-Z]+)-")
d = pd.concat([oud, nieuw], ignore_index=True).drop_duplicates(
    subset=["Order number", "SKU", "Return reasons description", "Created at"])
d["maand"] = d["Created at"].str[:7]
d["model"] = d["Product name"].str.extract(
    r"^(Mula|Rabara Maha|Rabara|Slipa Maha|Luna Kids|Sundara|Maha|Kaya|Bodhi|Loka)", flags=re.I)[0]
d["model"] = d.model.fillna(d["Product name"].str.split().str[0])
R = {"Too small": "te klein", "Too large": "te groot", "Fit not as expected": "pasvorm",
     "Quality not as expected": "kwaliteit", "Too narrow": "te smal", "Too wide": "te breed"}
d["reden"] = d["Return reasons description"].map(R).fillna("overig")
d["bedrag"] = pd.to_numeric(d["Resolution amount"], errors="coerce")
d.to_pickle("tofvel_retouren.pkl")

print(f"{len(d)} retourregels Tofvel, {d['Created at'].min()[:10]} t/m {d['Created at'].max()[:10]}")
print("\nper maand:", d.maand.value_counts().sort_index().to_dict())

print("\n=== per model ===")
t = pd.crosstab(d.model, d.reden)
t["totaal"] = t.sum(axis=1)
t["ruil%"] = d.groupby("model")["Requested resolution"].apply(lambda s: (s == "Exchange").mean() * 100)
t["terugbetaald €"] = d[d["Requested resolution"] == "Refund"].groupby("model").bedrag.sum()
print(t.sort_values("totaal", ascending=False).fillna(0).to_string(float_format=lambda v: f"{v:,.0f}"))

print("\n=== ruil of terugbetaling, per reden ===")
print(pd.crosstab(d.reden, d["Requested resolution"], margins=True).to_string())

print("\n=== toelichtingen van klanten ===")
for _, r in d[d.return_reason_comment.notna()].sort_values("Created at").iterrows():
    print(f"  [{r.model:<12} {r.reden:<9}] {r.return_reason_comment}")
