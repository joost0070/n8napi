#!/usr/bin/env python3
"""Voorraad-watch prototype: bouwt merk/maat-analyse uit ChannelEngine data."""
import json, glob, os, sys, math, datetime as dt
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
TODAY = dt.date(2026, 9, 14)

def load_products():
    prods = {}
    for f in glob.glob(os.path.join(BASE, 'prod', 'p*.json')):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        for p in d.get('Content') or []:
            ed = {e['Key']: e['Value'] for e in p.get('ExtraData') or []}
            prods[p['MerchantProductNo']] = {
                'mpn': p['MerchantProductNo'],
                'parent': p.get('ParentMerchantProductNo'),
                'name': p.get('Name'),
                'brand': (p.get('Brand') or ed.get('merk') or 'ONBEKEND').strip(),
                'size': p.get('Size'),
                'color': p.get('Color'),
                'ean': p.get('Ean'),
                'stock': p.get('Stock') or 0,
                'price': p.get('Price') or 0.0,
                'purchase': p.get('PurchasePrice'),
                'active': p.get('IsActive'),
                'cat': p.get('CategoryTrail'),
                'season': ed.get('seizoen_NL') or ed.get('seizoen_EN'),
                'season_year': ed.get('Seizoensjaar'),
                'model': ed.get('model'),
                'gender': ed.get('geslacht_NL'),
                'target': ed.get('Doelgroep_NL'),
                'shopify_nl': ed.get('shopify_id_NL'),
            }
    return prods

def load_orders():
    """returns list of (date, mpn, qty, channel, status, revenue)"""
    lines = []
    for f in glob.glob(os.path.join(BASE, 'ord', 'o*.json')):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        for o in d.get('Content') or []:
            try:
                od = dt.datetime.fromisoformat(o['OrderDate']).date()
            except Exception:
                continue
            for l in o.get('Lines') or []:
                if l.get('Status') in ('CANCELED',):
                    continue
                lines.append((od, l.get('MerchantProductNo'), l.get('Quantity') or 0,
                              o.get('ChannelName'), l.get('Status'),
                              l.get('LineTotalExclVat') or 0.0))
    return lines

def load_returns():
    rl = defaultdict(int)
    f = os.path.join(BASE, 'ret_all.json')
    if not os.path.exists(f):
        return rl
    for d in json.load(open(f)):
        for r in d.get('Content') or []:
            for l in r.get('Lines') or []:
                rl[l.get('MerchantProductNo')] += (l.get('Quantity') or 1)
    return rl

def season_of(p):
    s = (p.get('season') or '').lower()
    if 'herfst' in s or 'winter' in s or 'autumn' in s:
        return 'FW'
    if 'lente' in s or 'zomer' in s or 'spring' in s or 'summer' in s:
        return 'SS'
    if 'alle' in s or 'all' in s:
        return 'ALL'
    return 'ONBEKEND'

def main():
    prods = load_products()
    orders = load_orders()
    returns = load_returns()
    print(f"producten: {len(prods):,} | orderregels: {len(orders):,} | retourregels: {len(returns):,}")

    # ---- verkoop aggregeren over vensters
    sold_52w = defaultdict(int); sold_13w = defaultdict(int); sold_4w = defaultdict(int)
    rev_52w = defaultdict(float)
    per_week = defaultdict(int)
    channels = defaultdict(int)
    for od, mpn, q, ch, st, rev in orders:
        age = (TODAY - od).days
        if age < 0: continue
        if age <= 365: sold_52w[mpn] += q; rev_52w[mpn] += rev; per_week[od.isocalendar()[:2]] += q
        if age <= 91: sold_13w[mpn] += q
        if age <= 28: sold_4w[mpn] += q
        channels[ch] += q

    print("\n=== KANALEN (stuks, 12 mnd) ===")
    for c, q in sorted(channels.items(), key=lambda x: -x[1])[:15]:
        print(f"  {str(c)[:38]:40s} {q:7,}")

    # ---- match rate
    matched = sum(1 for m in sold_52w if m in prods)
    print(f"\nmatch orderregel->product: {matched}/{len(sold_52w)} unieke SKU's")

    # ---- merkoverzicht
    rows = []
    for mpn, p in prods.items():
        if p['parent'] is None:   # alleen varianten (maat-niveau)
            continue
        s52 = sold_52w.get(mpn, 0); s13 = sold_13w.get(mpn, 0); s4 = sold_4w.get(mpn, 0)
        stock = p['stock'] or 0
        cost = p['purchase'] if p['purchase'] not in (None, 0) else (p['price'] or 0) * 0.45
        rows.append({**p, 's52': s52, 's13': s13, 's4': s4,
                     'ret': returns.get(mpn, 0),
                     'value': stock * (cost or 0), 'season_code': season_of(p)})

    print(f"\nvarianten (maat-SKU's): {len(rows):,}")
    with_stock = [r for r in rows if r['stock'] > 0]
    print(f"met voorraad: {len(with_stock):,} | totaal stuks: {sum(r['stock'] for r in with_stock):,} "
          f"| inkoopwaarde: EUR {sum(r['value'] for r in with_stock):,.0f}")

    # ---- per merk
    bm = defaultdict(lambda: defaultdict(float))
    for r in with_stock:
        b = bm[r['brand']]
        b['skus'] += 1; b['stock'] += r['stock']; b['value'] += r['value']
        b['s52'] += r['s52']; b['s13'] += r['s13']; b['s4'] += r['s4']; b['ret'] += r['ret']
    print("\n=== TOP MERKEN OP VOORRAADWAARDE ===")
    print(f"{'merk':22s} {'skus':>6s} {'stuks':>8s} {'waarde EUR':>12s} {'12m verk':>9s} {'13w':>6s} {'4w':>5s} {'WoC':>7s}")
    for b, v in sorted(bm.items(), key=lambda x: -x[1]['value'])[:25]:
        wk = v['s13'] / 13 if v['s13'] else 0
        woc = (v['stock'] / wk) if wk else float('inf')
        print(f"{b[:22]:22s} {int(v['skus']):6,} {int(v['stock']):8,} {v['value']:12,.0f} "
              f"{int(v['s52']):9,} {int(v['s13']):6,} {int(v['s4']):5,} "
              f"{('---' if woc==float('inf') else f'{woc:,.0f}'):>7s}")

    json.dump([{k: v for k, v in r.items()} for r in rows],
              open(os.path.join(BASE, 'rows.json'), 'w'))
    json.dump({f"{y}-W{w:02d}": q for (y, w), q in sorted(per_week.items())},
              open(os.path.join(BASE, 'weekly.json'), 'w'), indent=1)
    print("\n-> rows.json + weekly.json geschreven")

if __name__ == '__main__':
    main()
