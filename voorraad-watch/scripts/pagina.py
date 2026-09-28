"""Zet overzicht.json (uitvoer van uitverkoop.py) in de overzichtspagina.

    cd <datamap> && python3 <repo>/voorraad-watch/scripts/pagina.py   -> voorraadradar.html
"""
import json, os, re
HIER = os.path.dirname(os.path.abspath(__file__))
B = os.environ.get('RADAR_DATA') or os.getcwd()
sjabloon = open(os.path.join(HIER, '..', 'pagina', 'voorraadradar.html'), encoding='utf-8').read()
data = json.dumps(json.load(open(os.path.join(B, 'overzicht.json'))), ensure_ascii=False, separators=(',', ':'))
data = data.replace('</', '<\\/')
html, n = re.subn(r'/\*DATA\*/.*?/\*EINDDATA\*/', lambda m: '/*DATA*/' + data + '/*EINDDATA*/', sjabloon, count=1, flags=re.S)
assert n == 1, 'datablok niet gevonden in het sjabloon'
open(os.path.join(B, 'voorraadradar.html'), 'w', encoding='utf-8').write(html)
print(f"voorraadradar.html: {len(html) / 1e6:.1f} MB")
