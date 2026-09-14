#!/usr/bin/env python3
"""Diepere voorraad-analyse: maatcurve, seizoen, gebroken maatreeksen."""
import json, os, re, datetime as dt
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(BASE, 'rows.json')))
TODAY = dt.date(2026, 9, 14)
WEEK = TODAY.isocalendar()[1]


def sortkey(x):
    try: return (0, float(x))
    except Exception: return (1, 99.0)

def norm_size(s):
    if not s: return None
    s = str(s).strip().replace(',', '.')
    m = re.match(r'^(\d{2}(?:\.5)?)', s)
    return m.group(1) if m else s[:8]

for r in rows:
    r['nsize'] = norm_size(r['size'])

# ================= 1. SEIZOENSVERDELING VAN DE VOORRAAD =================
print("=" * 78)
print("1. VOORRAAD NAAR SEIZOEN  (per merk, alleen SKU's met voorraad)")
print("=" * 78)
bs = defaultdict(lambda: defaultdict(float))
for r in rows:
    if r['stock'] > 0:
        bs[r['brand']][r['season_code']] += r['value']
print(f"{'merk':20s} {'FW EUR':>11s} {'SS EUR':>11s} {'ALL EUR':>11s} {'? EUR':>11s}")
tot = defaultdict(float)
for b, v in sorted(bs.items(), key=lambda x: -sum(x[1].values()))[:14]:
    print(f"{b[:20]:20s} {v['FW']:11,.0f} {v['SS']:11,.0f} {v['ALL']:11,.0f} {v['ONBEKEND']:11,.0f}")
    for k, x in v.items(): tot[k] += x
print(f"{'TOTAAL':20s} {tot['FW']:11,.0f} {tot['SS']:11,.0f} {tot['ALL']:11,.0f} {tot['ONBEKEND']:11,.0f}")

# ================= 2. MAATCURVE: verkoop% vs voorraad% =================
print()
print("=" * 78)
print("2. MAATCURVE-AFWIJKING per merk  (aandeel verkoop 12m vs aandeel voorraad)")
print("   negatief = relatief TE WEINIG voorraad | positief = TE VEEL")
print("=" * 78)
for brand in ['Keen', 'Crocs', 'Hunter', 'Tofvel', 'Sockwell', 'Toni Pons', 'Lazamani', 'HEYDUDE']:
    br = [r for r in rows if r['brand'] == brand and r['nsize']]
    if not br: continue
    sold = defaultdict(int); stock = defaultdict(int)
    for r in br:
        sold[r['nsize']] += r['s52']; stock[r['nsize']] += r['stock']
    ts, tk = sum(sold.values()), sum(stock.values())
    if ts < 20 or tk < 50: continue
    print(f"\n  {brand}   (12m verkoop {ts:,} st | voorraad {tk:,} st)")
    hdr, s_row, k_row, d_row = "  maat  ", "  verk% ", "  vrd%  ", "  delta "
    items = sorted(sold.items(), key=lambda x: sortkey(x[0]))
    for size, q in items:
        if q == 0 and stock[size] == 0: continue
        sp, kp = 100 * q / ts, 100 * stock[size] / tk
        hdr += f"{size:>7s}"; s_row += f"{sp:6.1f}%"; k_row += f"{kp:6.1f}%"; d_row += f"{kp-sp:+6.1f} "
    print(hdr); print(s_row); print(k_row); print(d_row)

# ================= 3. GEBROKEN MAATREEKSEN =================
print()
print("=" * 78)
print("3. GEBROKEN MAATREEKSEN  (lopende modellen waar kernmaten op 0 staan)")
print("=" * 78)
bymodel = defaultdict(list)
for r in rows:
    key = (r['brand'], r['parent'] or r['name'])
    bymodel[key].append(r)
broken = []
for (brand, parent), vs in bymodel.items():
    s13 = sum(v['s13'] for v in vs)
    if s13 < 4: continue
    sizes = [v for v in vs if v['nsize']]
    if len(sizes) < 4: continue
    oos = [v for v in sizes if v['stock'] == 0 and v['s52'] > 0]
    if not oos: continue
    lost = sum(v['s52'] for v in oos) / 52 * 4      # gemiste vraag per 4 wk
    broken.append((lost, brand, vs[0]['name'], s13, len(oos), len(sizes),
                   sorted({v['nsize'] for v in oos}, key=sortkey),
                   sum(v['stock'] for v in sizes), vs[0]['price']))
broken.sort(reverse=True)
print(f"{'merk':12s} {'model':34s} {'13w':>4s} {'oos/tot':>8s} {'vrd':>5s} {'mis/4wk':>8s}  maten zonder voorraad")
for lost, brand, name, s13, n_oos, n_tot, sizes, stk, price in broken[:20]:
    print(f"{brand[:12]:12s} {str(name)[:34]:34s} {s13:4d} {n_oos:4d}/{n_tot:<3d} {stk:5d} {lost:8.1f}  {', '.join(sizes[:9])}")

# ================= 4. OVERSTOCK =================
print()
print("=" * 78)
print("4. GROOTSTE OVERSTOCK-POSTEN  (voorraadwaarde vs verkoopsnelheid)")
print("=" * 78)
over = []
for r in rows:
    if r['stock'] <= 0 or r['value'] < 300: continue
    wk = r['s52'] / 52
    woc = r['stock'] / wk if wk > 0 else 999
    if woc >= 52:
        over.append((r['value'], woc, r))
over.sort(key=lambda x: -x[0])
print(f"{'merk':12s} {'artikel':32s} {'mt':>5s} {'sz':>4s} {'jr':>5s} {'vrd':>5s} {'12m':>4s} {'wrd EUR':>9s} {'WoC':>6s}")
for value, woc, r in over[:22]:
    print(f"{r['brand'][:12]:12s} {str(r['name'])[:32]:32s} {str(r['nsize'] or '-'):>5s} "
          f"{r['season_code'][:3]:>4s} {str(r['season_year'] or '-'):>5s} {r['stock']:5d} {r['s52']:4d} "
          f"{value:9,.0f} {('>999' if woc>=999 else f'{woc:.0f}'):>6s}")

# ================= 5. DEAD STOCK =================
print()
print("=" * 78)
print("5. DEAD STOCK  (voorraad, 0 verkoop in 12 mnd, per merk & seizoensjaar)")
print("=" * 78)
dead = defaultdict(lambda: defaultdict(float))
for r in rows:
    if r['stock'] > 0 and r['s52'] == 0:
        dead[r['brand']][str(r['season_year'] or '?')] += r['value']
print(f"{'merk':18s} {'dead EUR':>12s}   opbouw naar seizoensjaar")
for b, ys in sorted(dead.items(), key=lambda x: -sum(x[1].values()))[:14]:
    t = sum(ys.values())
    detail = ' '.join(f"{y}:{v/1000:.0f}k" for y, v in sorted(ys.items(), reverse=True)[:6])
    print(f"{b[:18]:18s} {t:12,.0f}   {detail}")
print(f"\nTOTAAL DEAD STOCK: EUR {sum(sum(y.values()) for y in dead.values()):,.0f}")
