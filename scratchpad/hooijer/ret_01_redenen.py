"""Retourredenen per shop en per model (Returnista, jan t/m aug 2026)."""
import re
import pandas as pd
pd.set_option("display.width", 230, "display.max_colwidth", 46)

d = pd.read_pickle("retouren.pkl")
SHOP = {"LANL":"Lazamani NL","LADE":"Lazamani DE","LAEN":"Lazamani EN","HDNL":"HEYDUDE NL",
        "KENL":"KEEN NL","BANL":"Bartogi NL","BADE":"Bartogi DE","TONL":"Tofvel NL",
        "TODE":"Tofvel DE","HUNL":"Hunter NL","TPNL":"Toni Pons NL","SWNL":"Sockwell NL",
        "SWDE":"Sockwell DE","JJNL":"Jan Jansen NL"}
d["shop"] = d.shopcode.map(SHOP).fillna(d.shopcode)
GROEP = {"Too small":"te klein","Too large":"te groot","Too narrow":"te smal",
         "Too wide":"te breed","Fit not as expected":"pasvorm",
         "Quality not as expected":"kwaliteit","Doesn't meet expectations":"verwachting",
         "Not as online image":"verwachting","Item is damaged":"beschadigd/fout",
         "Received wrong item":"beschadigd/fout","Delay in delivery":"overig"}
d["reden"] = d["Return reasons description"].map(GROEP).fillna("overig")
d["maat/pasvorm"] = d.reden.isin(["te klein","te groot","te smal","te breed","pasvorm"])
d["model"] = d["Product name"].str.replace(r"\s+(Black|White|Gold|Tan|Brown|Grey|Navy|Blue|"
                                           r"Beige|Taupe|Cognac|Offwhite|Off-White)\b.*$", "",
                                           regex=True, flags=re.I)

print("=== reden per shop (% van de retourregels) ===")
t = pd.crosstab(d.shop, d.reden, normalize="index") * 100
t["regels"] = d.shop.value_counts()
t["ruilen%"] = d.groupby("shop")["Requested resolution"].apply(lambda s: (s == "Exchange").mean()*100)
cols = ["regels","te klein","te groot","te smal","te breed","pasvorm","kwaliteit","verwachting","ruilen%"]
print(t[[c for c in cols if c in t]].sort_values("regels", ascending=False).to_string(
    float_format=lambda v: f"{v:,.0f}"))

print("\n\n=== modellen die structureel klein of groot vallen (minstens 15 maatretouren) ===")
m = d[d.reden.isin(["te klein","te groot"])].groupby(["shop","Product name"]).reden.value_counts().unstack(fill_value=0)
m["totaal"] = m.sum(axis=1)
m["% te klein"] = m["te klein"] / m.totaal * 100
m = m[m.totaal >= 15].sort_values("totaal", ascending=False)
print(m[(m["% te klein"] >= 75) | (m["% te klein"] <= 25)].head(25).to_string(
    float_format=lambda v: f"{v:,.0f}"))

print("\n\n=== modellen met veel kwaliteitsklachten (minstens 10) ===")
q = d[d.reden == "kwaliteit"].groupby(["shop","Product name"]).size().sort_values(ascending=False)
alle = d.groupby(["shop","Product name"]).size()
qq = pd.DataFrame({"kwaliteit": q, "alle retouren": alle}).dropna()
qq["aandeel%"] = qq.kwaliteit / qq["alle retouren"] * 100
print(qq[qq.kwaliteit >= 10].sort_values("kwaliteit", ascending=False).head(15).to_string(
    float_format=lambda v: f"{v:,.0f}"))
d.to_pickle("retouren_verrijkt.pkl")
