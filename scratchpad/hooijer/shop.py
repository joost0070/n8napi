"""Toegang tot de Shopify Admin API per shop.

Tokens komen uitsluitend uit omgevingsvariabelen. Nooit hardcoderen.

Gebruik:
    import shop
    data = shop.gql('keen_nl', '{ shop { name } }')
"""

from __future__ import annotations

import json
import os
import time
import urllib.request

API_VERSIE = "2025-07"

# sleutel -> (shopify-handle, naam omgevingsvariabele)
SHOPS: dict[str, tuple[str, str]] = {
    "bartogi_nl": ("bartogi-nl", "SHOPIFY_TOKEN_BARTOGI_NL"),
    "bartogi_de": ("bartogi-de", "SHOPIFY_TOKEN_BARTOGI_DE"),
    "keen_nl": ("keen-nl", "SHOPIFY_TOKEN_KEEN_NL"),
    "janjansen": ("jan-jansen-nl", "SHOPIFY_TOKEN_JAN_JANSEN_NL"),
    "heydude_nl": ("heydude-nl", "SHOPIFY_TOKEN_HEYDUDE_NL"),
    "hunter_nl": ("hunter-boots-nl", "SHOPIFY_TOKEN_HUNTER_BOOTS_NL"),
    "lazamani_nl": ("lazamani-nl", "SHOPIFY_TOKEN_LAZAMANI_NL"),
    "lazamani_de": ("lazamani-de", "SHOPIFY_TOKEN_LAZAMANI_DE"),
    "lazamani_en": ("lazamani-en", "SHOPIFY_TOKEN_LAZAMANI_EN"),
    "tonipons_nl": ("toni-pons-nl", "SHOPIFY_TOKEN_TONI_PONS_NL"),
    "tofvel_nl": ("tofvel-nl", "SHOPIFY_TOKEN_TOFVEL_NL"),
    "tofvel_de": ("tofvel-de", "SHOPIFY_TOKEN_TOFVEL_DE"),
    "tofvel_en": ("tofvel-en", "SHOPIFY_TOKEN_TOFVEL_EN"),
    "sockwell_nl": ("sockwell-b2c-nl", "SHOPIFY_TOKEN_SOCKWELL_B2C_NL"),
    "sockwell_de": ("sockwell-b2c-de", "SHOPIFY_TOKEN_SOCKWELL_B2C_DE"),
    "sockwell_en": ("sockwell-b2c-en", "SHOPIFY_TOKEN_SOCKWELL_B2C_EN"),
    "piedinudi_nl": ("piedi-nudi-nl", "SHOPIFY_TOKEN_PIEDI_NUDI_NL"),
}

# Nette naam voor rapportage.
LABELS: dict[str, str] = {
    "lazamani_nl": "Lazamani NL",
    "lazamani_de": "Lazamani DE",
    "lazamani_en": "Lazamani EN",
    "heydude_nl": "HEYDUDE NL",
    "sockwell_nl": "Sockwell NL",
    "sockwell_de": "Sockwell DE",
    "sockwell_en": "Sockwell EN",
    "keen_nl": "KEEN NL",
    "bartogi_nl": "Bartogi NL",
    "bartogi_de": "Bartogi DE",
    "tofvel_nl": "Tofvel NL",
    "tofvel_de": "Tofvel DE",
    "tofvel_en": "Tofvel EN",
    "hunter_nl": "Hunter NL",
    "tonipons_nl": "Toni Pons NL",
    "janjansen": "Jan Jansen NL",
    "piedinudi_nl": "Piedi Nudi NL",
}


class ShopFout(RuntimeError):
    """Iets ging mis bij het bevragen van een shop."""


def token(sleutel: str) -> str:
    if sleutel not in SHOPS:
        raise ShopFout(f"onbekende shopsleutel: {sleutel}")
    _, var = SHOPS[sleutel]
    waarde = os.environ.get(var)
    if not waarde:
        raise ShopFout(f"omgevingsvariabele {var} is niet gezet")
    return waarde


def domein(sleutel: str) -> str:
    return f"{SHOPS[sleutel][0]}.myshopify.com"


def gql(sleutel: str, query: str, variables: dict | None = None,
        pogingen: int = 4, timeout: int = 90) -> dict:
    """Voert een GraphQL-query uit op de Admin API en geeft het data-blok terug."""
    url = f"https://{domein(sleutel)}/admin/api/{API_VERSIE}/graphql.json"
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    laatste: Exception | None = None

    for poging in range(pogingen):
        verzoek = urllib.request.Request(
            url,
            data=body,
            headers={
                "X-Shopify-Access-Token": token(sleutel),
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(verzoek, timeout=timeout) as antwoord:
                payload = json.loads(antwoord.read())
        except Exception as fout:  # netwerk of time-out: opnieuw proberen
            laatste = fout
            time.sleep(2 ** poging)
            continue

        if payload.get("errors"):
            boodschap = "; ".join(f.get("message", "?") for f in payload["errors"])
            # Throttling is tijdelijk, de rest niet.
            if "THROTTLED" in boodschap.upper() or "throttl" in boodschap.lower():
                time.sleep(2 ** poging + 1)
                laatste = ShopFout(boodschap)
                continue
            raise ShopFout(f"{sleutel}: {boodschap}")

        return payload["data"]

    raise ShopFout(f"{sleutel}: geen antwoord na {pogingen} pogingen ({laatste})")


def controleer(sleutel: str) -> dict:
    """Snelle levenstest: antwoordt de shop en welke valuta voert hij?"""
    data = gql(sleutel, "{ shop { name myshopifyDomain currencyCode ianaTimezone } }")
    return data["shop"]
