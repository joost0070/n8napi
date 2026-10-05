import os
import requests, hashlib
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cdn_cache'); os.makedirs(CACHE, exist_ok=True)
def cdn(route):
    u = route.request.url; f = os.path.join(CACHE, hashlib.md5(u.encode()).hexdigest())
    if not os.path.exists(f):
        r = requests.get(u, timeout=60)
        if r.status_code != 200: return route.fulfill(status=r.status_code, body=b'')
        open(f, 'wb').write(r.content); open(f + '.ct', 'w').write(r.headers.get('content-type', 'image/jpeg'))
    route.fulfill(status=200, body=open(f, 'rb').read(), headers={'content-type': open(f + '.ct').read(), 'access-control-allow-origin': '*'})
