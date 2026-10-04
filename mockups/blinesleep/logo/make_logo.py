"""Bouwt het Bline-woordmerk als SVG (monolijn, afgeronde uiteinden), gelijk aan het label op het kussen."""
from pathlib import Path
OUT = Path(__file__).parent
SW = 9  # lijndikte
INK = "#1F2A37"

def word(color, sw=SW):
    s = f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    return f'''
  <g {s}>
    <path d="M10 26 V80"/>
    <circle cx="30" cy="80" r="20"/>
    <path d="M66 26 V84 A16 16 0 0 0 82 100"/>
    <path d="M100 63 V100"/>
    <path d="M118 100 V80 A19 19 0 0 1 156 80 V100"/>
    <path d="M174 80 H214 A20 20 0 1 0 207.5 95"/>
  </g>
  <circle cx="100" cy="42" r="{sw*0.62:.2f}" fill="{color}"/>'''

def svg(body, vb):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="bline">{body}\n</svg>\n'

VB = "0 16 224 94"  # strak om het woord, met halve lijndikte marge
(OUT / "bline-logo.svg").write_text(svg(word(INK), VB))
(OUT / "bline-logo-wit.svg").write_text(svg(word("#FFFFFF"), VB))

# Lockup met 'sleep' eronder, klein en gespatieerd (voor footer en verpakking)
lock = word(INK) + f'''
  <text x="112" y="140" text-anchor="middle" font-family="Inter, Helvetica, Arial, sans-serif" font-size="17" letter-spacing="9" fill="{INK}" opacity=".72">SLEEP</text>'''
(OUT / "bline-logo-sleep.svg").write_text(svg(lock, "0 16 224 134"))

# Icoon: de 'b' op zand, voor favicon en social
icon = f'''
  <rect x="0" y="0" width="120" height="120" rx="26" fill="#E9E1D4"/>
  <g transform="translate(26 -2)" stroke="{INK}" stroke-width="11" stroke-linecap="round" fill="none">
    <path d="M12 22 V80"/>
    <circle cx="34" cy="80" r="22"/>
  </g>'''
(OUT / "bline-icoon.svg").write_text(svg(icon, "0 0 120 120"))
print("ok")
