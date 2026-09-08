#!/usr/bin/env python3
"""Connectiviteitstest voor de ChannelEngine Merchant API (CE-koppeling).

Draait een reeks read-only checks tegen de Merchant API en rapporteert per
endpoint de HTTP-status, de responstijd en een korte samenvatting van de data.

Gebruik:
    python3 scripts/channelengine/channelengine-test.py
    python3 scripts/channelengine/channelengine-test.py --json
    CE_TENANT=mijntenant CE_API_KEY=... python3 .../channelengine-test.py

Auth: als CE_API_KEY gezet is wordt die als `apikey` query-parameter
meegestuurd. Draait het script achter een proxy die de sleutel injecteert,
dan kan CE_API_KEY leeg blijven.

Exitcode 0 als alle verplichte checks slagen, anders 1.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from typing import Any

DEFAULT_TENANT = "hooijerfootwear"
TIMEOUT_SECONDS = 30


@dataclass
class Check:
    """Eén endpoint-check."""

    name: str
    path: str
    params: dict[str, Any] = field(default_factory=dict)
    # Checks die mogen falen zonder de hele run rood te maken, bijvoorbeeld
    # omdat de API-sleutel er bewust geen rechten op heeft.
    optional: bool = False


@dataclass
class Result:
    check: Check
    status: int | None
    duration_ms: int
    ok: bool
    summary: str
    message: str | None = None


def base_url(tenant: str) -> str:
    return f"https://{tenant}.channelengine.net/api/v2"


def build_url(tenant: str, path: str, params: dict[str, Any], api_key: str | None) -> str:
    query = dict(params)
    if api_key:
        query["apikey"] = api_key
    url = f"{base_url(tenant)}/{path.lstrip('/')}"
    if query:
        url = f"{url}?{urllib.parse.urlencode(query, doseq=True)}"
    return url


def call(tenant: str, check: Check, api_key: str | None) -> tuple[int | None, dict[str, Any] | None, str | None, int]:
    """Doe het request. Geeft (status, body, foutmelding, duur in ms) terug."""
    url = build_url(tenant, check.path, check.params, api_key)
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    started = time.monotonic()
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            raw = response.read()
            status = response.status
    except urllib.error.HTTPError as error:
        raw = error.read()
        status = error.code
    except (urllib.error.URLError, TimeoutError) as error:
        duration = int((time.monotonic() - started) * 1000)
        return None, None, str(error), duration

    duration = int((time.monotonic() - started) * 1000)
    try:
        body = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return status, None, "response is geen geldige JSON", duration
    return status, body, None, duration


def summarize(body: dict[str, Any] | None) -> str:
    """Korte, leesbare samenvatting van een CE-response."""
    if not isinstance(body, dict):
        return "-"

    content = body.get("Content")
    if isinstance(content, list):
        total = body.get("TotalCount")
        if total is None:
            return f"{len(content)} item(s)"
        return f"{len(content)} van {total} item(s)"
    if isinstance(content, dict):
        for key in ("Name", "CompanyName"):
            if content.get(key):
                return f"{key}={content[key]}"
        return f"{len(content)} veld(en)"
    return "-"


def run_check(tenant: str, check: Check, api_key: str | None) -> Result:
    status, body, error, duration = call(tenant, check, api_key)

    if error is not None:
        return Result(check, status, duration, False, "-", error)

    success = isinstance(body, dict) and body.get("Success") is True
    ok = status == 200 and success
    message = None
    if not ok and isinstance(body, dict):
        message = body.get("Message")
        errors = body.get("ValidationErrors")
        if errors:
            message = f"{message} {json.dumps(errors, ensure_ascii=False)}".strip()

    return Result(check, status, duration, ok, summarize(body), message)


def stock_location_ids(tenant: str, api_key: str | None) -> list[int]:
    """Haal de stocklocation-ids op; /offer/stock heeft er minstens één nodig."""
    status, body, error, _ = call(tenant, Check("stocklocations", "stocklocations"), api_key)
    if error is not None or status != 200 or not isinstance(body, dict):
        return []
    content = body.get("Content")
    if not isinstance(content, list):
        return []
    return [item["Id"] for item in content if isinstance(item, dict) and isinstance(item.get("Id"), int)]


def build_checks(tenant: str, api_key: str | None) -> list[Check]:
    checks = [
        Check("Settings", "settings"),
        Check("Kanalen", "channels"),
        Check("Stocklocaties", "stocklocations"),
        Check("Producten", "products", {"page": 1}),
        Check("Orders", "orders", {"page": 1}),
        Check("Nieuwe orders", "orders/new", {"page": 1}),
        Check("Retouren", "returns", {"page": 1}),
        # De koppeling gebruikt vaak een sleutel zonder verzendrechten.
        Check("Zendingen", "shipments", {"page": 1}, optional=True),
    ]

    location_ids = stock_location_ids(tenant, api_key)
    if location_ids:
        checks.append(Check("Voorraad", "offer/stock", {"stockLocationIds": location_ids[:1]}))
    return checks


def print_report(tenant: str, results: list[Result]) -> None:
    print(f"ChannelEngine-koppeling: {base_url(tenant)}")
    print("-" * 78)
    for result in results:
        if result.ok:
            mark = "OK  "
        elif result.check.optional:
            mark = "SKIP"
        else:
            mark = "FAIL"
        status = result.status if result.status is not None else "-"
        print(f"[{mark}] {result.check.name:<16} {str(status):>4}  {result.duration_ms:>5} ms  {result.summary}")
        if result.message:
            print(f"       {result.message}")
    print("-" * 78)

    failed = [r for r in results if not r.ok and not r.check.optional]
    skipped = [r for r in results if not r.ok and r.check.optional]
    passed = len(results) - len(failed) - len(skipped)
    print(f"{passed} geslaagd, {len(failed)} gefaald, {len(skipped)} overgeslagen (optioneel)")


def to_json(tenant: str, results: list[Result]) -> str:
    payload = {
        "tenant": tenant,
        "baseUrl": base_url(tenant),
        "checks": [
            {
                "name": r.check.name,
                "path": r.check.path,
                "status": r.status,
                "durationMs": r.duration_ms,
                "ok": r.ok,
                "optional": r.check.optional,
                "summary": r.summary,
                "message": r.message,
            }
            for r in results
        ],
    }
    payload["ok"] = all(r.ok for r in results if not r.check.optional)
    return json.dumps(payload, indent=2, ensure_ascii=False)


def main() -> int:
    parser = argparse.ArgumentParser(description="Test de ChannelEngine-koppeling.")
    parser.add_argument("--tenant", default=os.environ.get("CE_TENANT", DEFAULT_TENANT))
    parser.add_argument("--json", action="store_true", help="Geef de uitslag als JSON.")
    args = parser.parse_args()

    api_key = os.environ.get("CE_API_KEY") or None
    checks = build_checks(args.tenant, api_key)
    results = [run_check(args.tenant, check, api_key) for check in checks]

    if args.json:
        print(to_json(args.tenant, results))
    else:
        print_report(args.tenant, results)

    return 0 if all(r.ok for r in results if not r.check.optional) else 1


if __name__ == "__main__":
    sys.exit(main())
