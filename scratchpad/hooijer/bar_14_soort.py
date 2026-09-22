"""Productsoort afleiden uit de artikelnaam, voor het seizoenspatroon."""
import re
import pandas as pd

REGELS = [
    ("Kerstartikelen", r"kerst|holiday elf|christmas"),
    ("Kleding", r"jacket|jas\b|coat|parka|mantel|broek|trui|shirt|vest|poncho"),
    ("Tassen", r"\bbag\b|crossbody|rugzak|tas\b|backpack|tote"),
    ("Teenslippers/slippers", r"teenslipper|slipper|pantolette|zehentrenner|flip|slides"),
    ("Sandalen", r"sandal|sandale"),
    ("Espadrilles", r"espadrille"),
    ("Instappers/klompen", r"instapper|clog|klomp|loafer|mule|mocassin|moc\b|slip-on|slipon|slide\b"),
    ("Sneakers", r"sneaker"),
    ("Ballerina's/flats", r"ballerina|flats\b|flat\b"),
    ("Laarzen/boots", r"laars|laarz|boots|boot|stiefel|wellington|chelsea"),
    ("Wandelschoenen", r"wandelschoen|wanderschuh|hiking|trail|bergschoen|wanderstiefel"),
    ("Wandelsandalen", r"wandelsandal|wandersandal"),
    ("Pantoffels", r"pantoffel|sloffen|hausschuh"),
    ("Sokken", r"sok|socks|kous"),
    ("Veterschoenen/nette schoenen", r"veter|derby|brogue|schnür"),
    ("Onderhoud/accessoires", r"creme|spray|veters|inleg|zool|verzorg|collonil"),
]


def soort(naam: str) -> str:
    t = str(naam).lower()
    for label, patroon in REGELS:
        if re.search(patroon, t):
            return label
    return "Overig"


if __name__ == "__main__":
    pd.set_option("display.width", 200)
    d = pd.read_pickle("bar_artikelen.pkl")
    d["soort"] = d.artikel.map(soort)
    g = d.groupby("soort").agg(artikelen=("artikel", "nunique"), stuks=("stuks", "sum"),
                               omzet=("bruto", "sum")).reset_index()
    g["aandeel omzet%"] = g.omzet / g.omzet.sum() * 100
    print("=== dekking van de indeling op de verkopen van 2026 ===")
    print(g.sort_values("omzet", ascending=False).to_string(
        index=False, float_format=lambda v: f"{v:,.1f}"))
    over = d[d.soort == "Overig"]
    print(f"\n  niet ingedeeld: {over.bruto.sum()/d.bruto.sum()*100:.1f}% van de omzet")
    if len(over):
        print("  voorbeelden:", over.artikel.drop_duplicates().head(12).tolist())
