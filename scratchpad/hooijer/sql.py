"""ShopifyQL-vragen stellen aan Shopify Analytics.

Gebruik:
    import sql
    df = sql.vraag('keen_nl', "FROM sessions SHOW sessions SINCE -12m UNTIL today")

Let op: ShopifyQL kent een eigen kostenplafond (1000 punten per minuut per shop),
los van het gewone GraphQL-plafond. `vraag` wacht vanzelf als het vol zit.
"""

from __future__ import annotations

import json
import time
import urllib.request

import pandas as pd

import shop

# Getalkolommen die ShopifyQL als tekst teruggeeft en die we numeriek willen.
_TEKSTKOLOMMEN = {"month", "week", "day", "referrer_source", "utm_source",
                  "utm_medium", "utm_campaign", "landing_page_path",
                  "product_title", "product_type", "referrer_name",
                  "referrer_host", "billing_country", "hour"}


class VraagFout(RuntimeError):
    """ShopifyQL kon de vraag niet beantwoorden."""


def _naar_getal(kolom: pd.Series) -> pd.Series:
    getallen = pd.to_numeric(kolom, errors="coerce")
    return kolom if getallen.isna().all() else getallen


def vraag(sleutel: str, query: str, pogingen: int = 5,
          timeout: int = 120) -> pd.DataFrame:
    """Stelt een ShopifyQL-vraag en geeft het antwoord als DataFrame terug."""
    graphql = """
    query($q: String!) {
      shopifyqlQuery(query: $q) {
        parseErrors
        tableData { columns { name } rows }
      }
    }
    """
    url = f"https://{shop.domein(sleutel)}/admin/api/{shop.API_VERSIE}/graphql.json"
    body = json.dumps({"query": graphql, "variables": {"q": query}}).encode()
    laatste: Exception | None = None

    for poging in range(pogingen):
        verzoek = urllib.request.Request(
            url,
            data=body,
            headers={
                "X-Shopify-Access-Token": shop.token(sleutel),
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(verzoek, timeout=timeout) as antwoord:
                payload = json.loads(antwoord.read())
        except Exception as fout:
            laatste = fout
            time.sleep(2 ** poging)
            continue

        if payload.get("errors"):
            boodschap = "; ".join(f.get("message", "?") for f in payload["errors"])
            if "throttl" in boodschap.lower():
                time.sleep(5 * (poging + 1))
                laatste = VraagFout(boodschap)
                continue
            raise VraagFout(f"{sleutel}: {boodschap}\n  vraag: {query}")

        antwoord_blok = payload["data"]["shopifyqlQuery"]
        if antwoord_blok["parseErrors"]:
            raise VraagFout(
                f"{sleutel}: {antwoord_blok['parseErrors']}\n  vraag: {query}")

        tabel = antwoord_blok["tableData"]
        if tabel is None:
            return pd.DataFrame()

        kolommen = [k["name"] for k in tabel["columns"]]
        df = pd.DataFrame(tabel["rows"], columns=kolommen)
        for kolom in df.columns:
            if kolom not in _TEKSTKOLOMMEN:
                df[kolom] = _naar_getal(df[kolom])
        return df

    raise VraagFout(f"{sleutel}: geen antwoord na {pogingen} pogingen ({laatste})")
