"""Waar komt de brutowinstmarge van 2026 uit?"""
import pandas as pd

d = pd.read_pickle("bar_q4_realistisch.pkl")
YTD = {"NL": dict(bruto=187792.86, winst=13246.69, adv_pct=0.2092),
       "DE": dict(bruto=152950.62, winst=33284.49, adv_pct=0.0878)}

for shopnaam in ("NL", "DE"):
    s = d[d.shop == shopnaam].copy()
    y = YTD[shopnaam]
    s["winst per stuk"] = s.brutowinst / s.stuks.replace(0, 1)
    q4_omzet = s["omzet Q4 nu"].sum()
    q4_winst = (s["verkoopbaar Q4"] * s["winst per stuk"]).sum()
    prijskans = s["kans realistisch"].sum()
    advkans = (y["adv_pct"] - 0.12) * q4_omzet if y["adv_pct"] > 0.12 else 0

    print(f"\n=== Bartogi {shopnaam}: projectie heel 2026 ===")
    print(f"  jan t/m sep : omzet € {y['bruto']:>9,.0f}   brutowinst € {y['winst']:>8,.0f}   "
          f"{y['winst']/y['bruto']*100:>5.2f}%".replace(",", "."))
    print(f"  okt t/m dec : omzet € {q4_omzet:>9,.0f}   brutowinst € {q4_winst:>8,.0f}   "
          f"{q4_winst/q4_omzet*100:>5.2f}%   (bij ongewijzigd beleid)".replace(",", "."))
    jaar_o, jaar_w = y["bruto"] + q4_omzet, y["winst"] + q4_winst
    print(f"  heel 2026   : omzet € {jaar_o:>9,.0f}   brutowinst € {jaar_w:>8,.0f}   "
          f"{jaar_w/jaar_o*100:>5.2f}%".replace(",", "."))
    print(f"\n  met ingrijpen in het vierde kwartaal:")
    stap = jaar_w
    for naam, bedrag in (("prijzen naar bodemprijs (binnen adviesprijs)", prijskans),
                         ("advertentie naar 12% in Q4", advkans)):
        if bedrag <= 0:
            continue
        stap += bedrag
        no = jaar_o + (bedrag if naam.startswith("prijzen") else 0)
        print(f"    + {naam:<44} € {bedrag:>7,.0f}  ->  jaar {stap/no*100:>5.2f}%"
              .replace(",", "."))
    print(f"    Q4-marge wordt daarmee "
          f"{(q4_winst+prijskans+advkans)/(q4_omzet+prijskans)*100:.1f}% in het kwartaal")

print("\n\n=== hoeveel van de voorraad komt dit kwartaal uberhaupt in beweging? ===")
for shopnaam in ("NL", "DE"):
    s = d[d.shop == shopnaam]
    print(f"  Bartogi {shopnaam}: {s.voorraad.sum():,.0f} stuks op voorraad, verwachte vraag "
          f"okt-dec {s['verwacht okt-dec'].sum():,.0f} stuks = "
          f"{s['verwacht okt-dec'].sum()/s.voorraad.sum()*100:.1f}%".replace(",", "."))
