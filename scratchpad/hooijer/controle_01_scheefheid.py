"""Zet de rangschikking op winkelwagenpercentage duurdere shops onterecht bovenaan?

Toets 1: hangt de plek in de oude rangschikking samen met de orderwaarde?
Toets 2: hoeveel van het 'gat' van elke shop is te verklaren uit zijn prijspunt?
         Per shop wordt de lijn opnieuw bepaald zonder die shop zelf mee te nemen,
         zodat een shop niet zijn eigen doel bepaalt.
"""
import numpy as np
import pandas as pd

pd.set_option("display.width", 210)

df = pd.read_pickle("nulmeting_v2.pkl")
df = df[(df.sleutel != "_totaal") & (df.sessions >= 10000)].copy()
BESTE = df["wagen%"].max()

# --- oude methode: iedereen naar de beste shop
df["gat naar beste"] = (BESTE - df["wagen%"]).clip(lower=0)
df["extra orders oud"] = (df["gat naar beste"] / 100 * df.sessions
                          * df["afreken%"] / 100 * df["order%"] / 100)
df["omzet oud"] = df["extra orders oud"] * df.AOV

# --- prijsgecorrigeerd doel, telkens zonder de shop zelf
doelen = []
for naam in df.shop:
    rest = df[df.shop != naam]
    helling, snij = np.polyfit(rest.AOV, rest["wagen%"], 1)
    doelen.append(helling * df.loc[df.shop == naam, "AOV"].iloc[0] + snij)
df["doel bij prijspunt"] = doelen
df["gat na correctie"] = (df["doel bij prijspunt"] - df["wagen%"]).clip(lower=0)
df["extra orders nieuw"] = (df["gat na correctie"] / 100 * df.sessions
                            * df["afreken%"] / 100 * df["order%"] / 100)
df["omzet nieuw"] = df["extra orders nieuw"] * df.AOV

df["rang oud"] = df["omzet oud"].rank(ascending=False).astype(int)
df["rang nieuw"] = df["omzet nieuw"].rank(ascending=False).astype(int)
df["verschuiving"] = df["rang oud"] - df["rang nieuw"]

r_aov_rang = df.AOV.rank().corr(df["rang oud"].rank())
r_aov_gat = df.AOV.corr(df["gat naar beste"])
print("TOETS 1 — is de oude rangschikking scheef naar dure shops?")
print(f"  samenhang AOV met het 'gat naar de beste shop' : {r_aov_gat:+.2f}")
print(f"  samenhang AOV met de plek in de oude lijst      : {r_aov_rang:+.2f}")
print("  (negatief bij de rangvolgorde betekent: hoe duurder, hoe hoger in de lijst)\n")

verklaard = 1 - df["gat na correctie"].sum() / df["gat naar beste"].sum()
print(f"TOETS 2 — {verklaard*100:.0f}% van alle gemeten 'achterstand' verdwijnt zodra je "
      f"het prijspunt meeneemt.\n")

toon = df[["shop", "sessions", "AOV", "wagen%", "doel bij prijspunt", "gat naar beste",
           "gat na correctie", "omzet oud", "omzet nieuw", "rang oud", "rang nieuw",
           "verschuiving"]].sort_values("omzet nieuw", ascending=False)
print(toon.to_string(index=False, float_format=lambda v: f"{v:,.2f}"))
df.to_pickle("controle_scheefheid.pkl")
