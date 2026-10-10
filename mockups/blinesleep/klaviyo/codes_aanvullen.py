"""Vult de unieke kortingscodes aan: eerst in Shopify (de korting zelf), daarna dezelfde codes in Klaviyo (de pool waaruit de mails uitdelen).
Gebruik: python3 codes_aanvullen.py <aantal per coupon>   (standaard 1750; samen met de bestaande 250 wordt dat 2000)
De waarschuwing bij weinig codes zet hij op 200.
"""
import sys, secrets, string, time, json
sys.path.insert(0, '/tmp/claude-0/-home-user-n8napi/94df064a-2091-5b03-a485-9cd9ce529587/scratchpad/eigen')
from gq import gql
from kv import k

A = 'KLAVIYO_BlineSleep'
SETS = [('BLINE_WELKOM10', 'BLW-', 'gid://shopify/DiscountCodeNode/1853144269139'),
        ('BLINE_CHECKOUT10', 'BLC-', 'gid://shopify/DiscountCodeNode/1853144301907')]
TEKENS = ''.join(c for c in string.ascii_uppercase + string.digits if c not in 'O0I1L')


def nieuwe_codes(prefix, n):
    return sorted({prefix + ''.join(secrets.choice(TEKENS) for _ in range(7)) for _ in range(n + 20)})[:n]


aantal = int(sys.argv[1]) if len(sys.argv) > 1 else 1750
for coupon, prefix, disc in SETS:
    codes = nieuwe_codes(prefix, aantal)
    # Shopify: per 250 codes
    for i in range(0, len(codes), 250):
        r = gql('mutation($d:ID!,$c:[DiscountRedeemCodeInput!]!){discountRedeemCodeBulkAdd(discountId:$d,codes:$c){bulkCreation{id} userErrors{message}}}',
                {'d': disc, 'c': [{'code': c} for c in codes[i:i + 250]]})
        e = r['data']['discountRedeemCodeBulkAdd']['userErrors']
        if e: sys.exit(f'shopify fout {coupon}: {e}')
        time.sleep(1)
    # wachten tot Shopify ze heeft verwerkt
    for _ in range(30):
        n = gql('query($id:ID!){codeDiscountNode(id:$id){codeDiscount{... on DiscountCodeBasic{codesCount{count}}}}}', {'id': disc})['data']['codeDiscountNode']['codeDiscount']['codesCount']['count']
        if n >= 250 + aantal: break
        time.sleep(4)
    print(coupon, 'shopify codes', n)
    # Klaviyo: per 1000 codes
    for i in range(0, len(codes), 1000):
        body = {'data': {'type': 'coupon-code-bulk-create-job', 'attributes': {'coupon-codes': {'data': [
            {'type': 'coupon-code', 'attributes': {'unique_code': c}, 'relationships': {'coupon': {'data': {'type': 'coupon', 'id': coupon}}}} for c in codes[i:i + 1000]]}}}}
        sc, j = k(A, 'POST', 'coupon-code-bulk-create-jobs/', body)
        print(coupon, 'klaviyo job', sc)
        if sc >= 300: sys.exit(json.dumps(j)[:400])
    sc, j = k(A, 'PATCH', f'coupons/{coupon}/', {'data': {'type': 'coupon', 'id': coupon, 'attributes': {'monitor_configuration': {'low_balance_threshold': 200}}}})
    print(coupon, 'drempel', sc)
