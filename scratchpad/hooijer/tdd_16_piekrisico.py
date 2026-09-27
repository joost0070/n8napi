"""Tofvel-deepdive: piekrisico okt-dec (targetweken 40-53) per SKU en uitwijk per maat.

Vraag = verkochte stuks okt-dec 2025 (NL+DE+EU). Tekort = vraag - huidige voorraad.
Uitwijk: kan de klant in dezelfde maat een ander kleur van hetzelfde model kopen
waar ruim voorraad van is (voorraad > eigen vraag)? Schrijft tdd_piekrisico.pkl.
"""
import pandas as pd

FAM = r"^(Mula Lungta|Mula|Rabara Maha|Rabara|Slipa Maha|Slipa|Luna Kids|Celsi|Sundara)"

if __name__ == "__main__":
    a = pd.read_pickle("assortiment_tofvel_nl.pkl")
    r = pd.read_pickle("tdd_regels_verrijkt.pkl")
    r = r[r.web & (r.d >= "2025-10-01") & (r.d <= "2025-12-31")]
    v = a.merge(r.groupby("sku").aantal.sum().rename("vraag"), left_on="sku",
                right_index=True, how="left").fillna({"vraag": 0})
    v["model"] = v.titel.str.extract(FAM)[0]
    v["tekort"] = (v.vraag - v.voorraad.clip(lower=0)).clip(lower=0)
    v["overschot"] = (v.voorraad.clip(lower=0) - v.vraag).clip(lower=0)
    ruimte = v.groupby(["model", "maat"]).overschot.sum().rename("ruimte_zelfde_maat")
    v = v.join(ruimte, on=["model", "maat"])
    v["ruimte_andere_kleur"] = v.ruimte_zelfde_maat - v.overschot
    v["winst_per_paar"] = v.prijs / 1.21 - v.kostprijs - 6 - 0.007 * v.prijs / 1.21
    v.to_pickle("tdd_piekrisico.pkl")
    t = v[v.tekort > 0]
    print("Vraag okt-dec 2025:", v.vraag.sum(), " tekort:", t.tekort.sum(),
          " omzet excl. btw:", round((t.tekort * t.prijs / 1.21).sum()),
          " bijdrage:", round((t.tekort * t.winst_per_paar).sum()))
    kan = t[t.ruimte_andere_kleur >= t.tekort]
    print("waarvan zelfde model+maat in andere kleur ruim op voorraad:", kan.tekort.sum())
    per = t.groupby("titel").agg(vraag=("vraag", "sum"), tekort=("tekort", "sum"),
                                 bijdrage=("winst_per_paar", "first")).sort_values(
        "tekort", ascending=False)
    per["bijdrage_risico"] = per.tekort * per.bijdrage
    print(per.head(15).round(0).to_string())
    m = v[v.model == "Mula"].groupby("titel").agg(voorraad=("voorraad", "sum"),
                                                   vraag=("vraag", "sum"))
    m["seizoenen_voorraad"] = m.voorraad / m.vraag.where(m.vraag > 0)
    print(m.sort_values("voorraad", ascending=False).round(1).to_string())
    print("Totale voorraad:", v.voorraad.clip(lower=0).sum(), "paar; vraag okt-dec 2025:", v.vraag.sum())
