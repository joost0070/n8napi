"""Retouranalyse per model en maat, met elke retourreden apart.

Zelfde opzet als 'retouranalyse lazamani.nl en .de', maar zonder samengevoegde
redenen: 'te klein' en 'te smal' vragen een andere oplossing (een maat groter
helpt bij het eerste, niet bij het tweede), dus ze staan in eigen kolommen.

Echt retourpercentage = geretourneerde paren uit bestellingen in het venster,
gedeeld door de verkochte paren uit datzelfde venster (cohort op besteldatum).
"""
import re
import sys
import pandas as pd

REDEN = {
    "Too small": "Te klein", "Too narrow": "Te smal", "Too large": "Te groot",
    "Too wide": "Te wijd", "Fit not as expected": "Pasvorm anders dan verwacht",
    "Quality not as expected": "Kwaliteit tegengevallen",
    "Doesn't meet expectations": "Voldoet niet aan verwachting",
    "Not as online image": "Wijkt af van foto", "Item is damaged": "Beschadigd ontvangen",
    "Received wrong item": "Verkeerd artikel", "Delay in delivery": "Te laat geleverd",
}
KOLOM = {"Te klein": "% te klein", "Te smal": "% te smal", "Te groot": "% te groot",
         "Te wijd": "% te wijd", "Pasvorm anders dan verwacht": "% pasvorm",
         "Kwaliteit tegengevallen": "% kwaliteit",
         "Voldoet niet aan verwachting": "% verwachting"}
THEMA = {
    "instap/opening te nauw": r"instap|opening|instapgat|einstieg|öffnung|aan ?te ?trekken|"
                              r"aantrekken|aan te doen|niet in de|kom .*niet in|krijg .*niet aan|"
                              r"schoenlepel|get in",
    "hoge wreef": r"wreef|spann|instep",
    "te breed/ruim": r"breed|wijd|ruim|breit|wide|zwem",
    "te smal/krap": r"smal|nauw|krap|strak|eng\b|schmal|narrow|tight|bekneld",
    "hiel slipt": r"hiel|hak\b|slipt|slip |uit ?slof|ferse|heel",
    "zool": r"zool|sohle|sole|bobbel|hobbel|stijf|stug|hard",
    "links/rechts verschil": r"links|rechts|linker|rechter|ene slof|de andere",
    "kleur/foto": r"kleur|farbe|foto|colou?r",
    "lengte/maat": r"maat|lengte|size|größe|groter|kleiner",
}
DREMPEL_ADVIES, MIN_VERKOCHT = 10.0, 30


def model_van(titel, patroon):
    m = re.match(patroon, str(titel), flags=re.I) if patroon else None
    return (m.group(1).title() if m else str(titel).split()[0]).strip()


def diagnose(r):
    """Hoofddiagnose plus, als pasvorm ook fors is, een tweede signaal."""
    hoofd = _diagnose(r)
    if r.Retour >= 10 and r["% pasvorm"] >= 20 and not hoofd.startswith("Pasvorm"):
        hoofd += f" · daarnaast pasvorm ({r['% pasvorm']:.0f}%): zie thema's"
    return hoofd


def _diagnose(r):
    if r.Retour < 10:
        return "te weinig retouren om te duiden"
    k, s, g, w = r["% te klein"], r["% te smal"], r["% te groot"], r["% te wijd"]
    p, q = r["% pasvorm"], r["% kwaliteit"] + r["% verwachting"]
    if q >= 30:
        return "Kwaliteit/verwachting vaak genoemd: uitzoeken bij leverancier"
    if k + s >= 50:
        if s < 10 or k >= 2 * s:
            return "Valt klein: maatadvies 'neem een maat groter'"
        if k < 10 or s >= 2 * k:
            return "Valt smal: 'smalle leest' vermelden, een maat groter helpt niet"
        return "Valt klein én smal: maat groter adviseren én 'smalle leest' vermelden"
    if g + w >= 35:
        if w < 10 or g >= 2 * w:
            return "Valt groot: maatadvies 'neem een maat kleiner'"
        if g < 10 or w >= 2 * g:
            return "Valt wijd: 'ruime leest' vermelden"
        return "Valt groot én wijd: maat kleiner adviseren én 'ruime leest' vermelden"
    if p >= 30:
        return "Pasvorm: leest en instap beschrijven op de productpagina (zie thema's)"
    if k >= 35:
        return "Neiging tot klein: maatadvies overwegen"
    return "Gemengde redenen: toelichtingen bekijken"


def prioriteit(r, gem, top3):
    if r.Verkocht < MIN_VERKOCHT:
        return "Te weinig verkocht om te beoordelen"
    if r["Retour%"] >= gem + DREMPEL_ADVIES:
        return "Aanpakken"
    if r.model in top3 and r["Retour%"] >= gem:
        return "Aanpakken (grootste retourwaarde)"
    if r["Retour%"] < gem - DREMPEL_ADVIES:
        return "Onder gemiddeld, niets doen"
    return "Rond het gemiddelde, monitoren"


def analyse(cfg):
    regels = []
    for sleutel, land in cfg["shops"]:
        r = pd.read_pickle(f"ret_regels_{sleutel}.pkl")
        r["land"] = land
        regels.append(r)
    v = pd.concat(regels, ignore_index=True)
    v = v[(v.datum >= cfg["van"]) & (v.datum <= cfg["tot"])].copy()
    v["model"] = v["product"].map(lambda t: model_van(t, cfg["model"]))
    v["prijs"] = v.netto / v.aantal.replace(0, 1)
    v["week"] = pd.to_datetime(v.datum).dt.to_period("W-SUN").dt.start_time

    ret = cfg["retouren"]().copy()
    ret = ret.drop(columns=[c for c in ("model", "maat", "land", "prijs", "week", "product", "reden") if c in ret])
    ret["SKU"] = ret.SKU.astype(str).str.replace(r"\.0$", "", regex=True).str.zfill(13)
    ret["reden"] = ret["Return reasons description"].map(REDEN).fillna("Overig")
    sleutel_v = v.drop_duplicates(["order", "sku"]).set_index(["order", "sku"])
    ret = ret[ret["Order number"].isin(v.order.unique())].copy()
    ret = ret.join(sleutel_v[["model", "maat", "land", "prijs", "week", "product"]],
                   on=["Order number", "SKU"])
    ongekoppeld = ret.model.isna().sum()
    ret = ret[ret.model.notna()]
    ret["ruil"] = ret["Requested resolution"].eq("Exchange")
    ret["thema's"] = ret.return_reason_comment.fillna("").str.lower().map(
        lambda t: [n for n, pat in THEMA.items() if t and re.search(pat, t)])
    return v, ret, ongekoppeld


def tabellen(v, ret, cfg):
    verkocht = v.aantal.sum()
    gem = len(ret) / verkocht * 100
    reden_orde = [r for r in REDEN.values() if r in set(ret.reden)] + (
        ["Overig"] if "Overig" in set(ret.reden) else [])

    # per model
    mv = v.groupby("model").agg(Verkocht=("aantal", "sum"), Omzet=("netto", "sum"))
    for land in v.land.unique():
        mv[f"Verkocht {land}"] = v[v.land == land].groupby("model").aantal.sum()
    mr = ret.groupby("model").agg(Retour=("reden", "size"),
                                  Retourwaarde=("prijs", "sum"), ruil=("ruil", "mean"))
    m = mv.join(mr).fillna({"Retour": 0, "Retourwaarde": 0})
    m["Retour%"] = m.Retour / m.Verkocht * 100
    m["Boven gemiddelde"] = m["Retour%"] - gem
    for land in v.land.unique():
        rl = ret[ret.land == land].groupby("model").size()
        m[f"Retour% {land}"] = rl.reindex(m.index).fillna(0) / m[f"Verkocht {land}"] * 100
    kruis = pd.crosstab(ret.model, ret.reden)
    for reden, kol in KOLOM.items():
        m[kol] = (kruis[reden] if reden in kruis else 0) / m.Retour.replace(0, pd.NA) * 100
    m["% overig"] = 100 - m[list(KOLOM.values())].sum(axis=1)
    m["Ruil%"] = m.ruil * 100
    th = ret.explode("thema's").dropna(subset=["thema's"]).groupby(
        ["model", "thema's"]).size().reset_index(name="n").sort_values("n", ascending=False)
    m["Thema's in toelichting"] = th.groupby("model").apply(
        lambda g: ", ".join(f"{t} ({n})" for t, n in zip(g["thema's"], g.n) if n >= 2)[:120],
        include_groups=False)
    m = m.fillna({k: 0 for k in list(KOLOM.values()) + ["% overig"]})
    m["Wat de redenen zeggen"] = m.apply(diagnose, axis=1)
    top3 = set(m[m.Verkocht >= MIN_VERKOCHT].sort_values("Retourwaarde", ascending=False).index[:3])
    m["Prioriteit"] = m.reset_index().apply(lambda r: prioriteit(r, gem, top3), axis=1).values
    m = m.sort_values("Retour", ascending=False).reset_index()

    # per maat
    sv = v.groupby("maat").aantal.sum().rename("Verkocht")
    s = pd.DataFrame(sv).join(ret.groupby("maat").size().rename("Retour")).fillna(0)
    s["Retour%"] = s.Retour / s.Verkocht * 100
    k2 = pd.crosstab(ret.maat, ret.reden)
    for reden, kol in KOLOM.items():
        s[kol] = (k2[reden] if reden in k2 else 0) / s.Retour.replace(0, pd.NA) * 100
    s = s[s.Verkocht >= 20].reset_index()
    s["_k"] = pd.to_numeric(s.maat.str.extract(r"(\d+(?:[.,]\d)?)")[0].str.replace(",", "."),
                            errors="coerce")
    s = s.sort_values(["_k", "maat"]).drop(columns="_k")

    # model x maat
    top = m[m.Verkocht >= MIN_VERKOCHT].model.head(35)
    vm = v[v.model.isin(top)].pivot_table(index="model", columns="maat", values="aantal",
                                          aggfunc="sum").fillna(0)
    rm = ret[ret.model.isin(top)].pivot_table(index="model", columns="maat", values="reden",
                                              aggfunc="size").reindex_like(vm).fillna(0)
    pct = (rm / vm.where(vm >= 5) * 100).round(0)
    orde = sorted(vm.columns, key=lambda x: (float(re.sub(r"[^\d.]", "", x.replace(",", ".")) or 0), x))
    pct, vm = pct.reindex(index=top, columns=orde), vm.reindex(index=top, columns=orde)

    # per week
    w = v.groupby(["week", "land"]).aantal.sum().unstack(fill_value=0)
    wr = ret.groupby(["week", "land"]).size().unstack(fill_value=0).reindex_like(w).fillna(0)
    week = pd.DataFrame(index=w.index)
    for land in w.columns:
        week[f"Verkocht {land}"] = w[land]
        week[f"Retour {land}"] = wr[land]
        week[f"Retour% {land}"] = wr[land] / w[land].replace(0, pd.NA) * 100
    week["Retour% totaal"] = wr.sum(axis=1) / w.sum(axis=1) * 100
    grens = pd.Timestamp(cfg["retouren_tot"]) - pd.Timedelta(days=21)
    week["Status"] = ["compleet" if d <= grens else "retouren nog onderweg" for d in week.index]
    week = week.reset_index().rename(columns={"week": "Bestelweek vanaf"})

    # redenen
    rd = pd.crosstab(ret.reden, ret.land)
    rd["Totaal"] = rd.sum(axis=1)
    rd["% van retouren"] = rd.Totaal / len(ret) * 100
    rd["% van verkoop"] = rd.Totaal / verkocht * 100
    rd["Retourwaarde"] = ret.groupby("reden").prijs.sum()
    rd["Ruil%"] = ret.groupby("reden").ruil.mean() * 100
    rd = rd.sort_values("Totaal", ascending=False).reset_index().rename(columns={"reden": "Reden"})

    # model x reden aantallen
    mxr = pd.crosstab(ret.model, ret.reden)[reden_orde]
    mxr["Totaal"] = mxr.sum(axis=1)
    mxr = mxr.sort_values("Totaal", ascending=False).reset_index().rename(columns={"model": "Model"})

    return dict(gem=gem, verkocht=verkocht, model=m, maat=s, pct=pct, n=vm, week=week,
                redenen=rd, mxr=mxr)
