"""Inline SVG illustrations and icons for the Bline Sleep mockups.

Every illustration is generated with unique gradient/filter ids so that
several of them can live on one page without clashing.
"""
import math
import random

_counter = [0]


def uid():
    _counter[0] += 1
    return f"a{_counter[0]}"


SERIF = "Cormorant Garamond, Georgia, serif"
SANS = "Inter, Helvetica, Arial, sans-serif"

# ---------------------------------------------------------------- icons
ICONS = {
    "search": '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4.5 20.5c0-3.6 3.4-6 7.5-6s7.5 2.4 7.5 6"/>',
    "bag": '<path d="M5 8.5h14l-1.1 12H6.1L5 8.5z"/><path d="M9 8.5V7a3 3 0 0 1 6 0v1.5"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "shield": '<path d="M12 3l7.5 3v5.6c0 4.8-3.2 8-7.5 9.4-4.3-1.4-7.5-4.6-7.5-9.4V6L12 3z"/><path d="M8.7 12.2l2.3 2.3 4.4-4.6"/>',
    "truck": '<path d="M2.5 6.5h11v9.5h-11z"/><path d="M13.5 10h4.2l3 3.2v2.8h-7.2"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
    "moon": '<path d="M19.5 14.6A7.8 7.8 0 1 1 9.4 4.5a6.3 6.3 0 0 0 10.1 10.1z"/>',
    "flask": '<path d="M9 3.5h6"/><path d="M10 3.5v5.8L5.2 17.6A2 2 0 0 0 7 20.5h10a2 2 0 0 0 1.8-2.9L14 9.3V3.5"/><path d="M7.4 14.5h9.2"/>',
    "arrow": '<path d="M4.5 12h15"/><path d="M13.5 6l6 6-6 6"/>',
    "external": '<path d="M14 4.5h5.5V10"/><path d="M19.5 4.5L11 13"/><path d="M18 14v4.8a.7.7 0 0 1-.7.7H5.2a.7.7 0 0 1-.7-.7V6.7c0-.4.3-.7.7-.7H10"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "minus": '<path d="M5 12h14"/>',
    "return": '<path d="M9 14L4.5 9.5 9 5"/><path d="M4.5 9.5h10a5 5 0 0 1 0 10H11"/>',
    "sun": '<circle cx="12" cy="12" r="3.8"/><path d="M12 2.8v2M12 19.2v2M2.8 12h2M19.2 12h2M5.5 5.5l1.4 1.4M17.1 17.1l1.4 1.4M5.5 18.5l1.4-1.4M17.1 6.9l1.4-1.4"/>',
    "layers": '<path d="M12 3.5l8.5 4.6-8.5 4.6-8.5-4.6L12 3.5z"/><path d="M3.5 12.3l8.5 4.6 8.5-4.6"/><path d="M3.5 16.4l8.5 4.6 8.5-4.6"/>',
    "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    "box": '<path d="M3.5 7.5L12 3.8l8.5 3.7v9L12 20.2l-8.5-3.7v-9z"/><path d="M3.5 7.5l8.5 3.8 8.5-3.8"/><path d="M12 11.3v8.9"/>',
    "doc": '<path d="M14 3.5H6.6a.9.9 0 0 0-.9.9v15.2c0 .5.4.9.9.9h10.8c.5 0 .9-.4.9-.9V7.8L14 3.5z"/><path d="M14 3.5v4.3h4.3"/><path d="M8.8 12.5h6.4M8.8 16h4.4"/>',
    "chat": '<path d="M4.5 6.5c0-1.1.9-2 2-2h11c1.1 0 2 .9 2 2v8c0 1.1-.9 2-2 2H10l-4 3.5v-3.5h0.5c-1.1 0-2-.9-2-2v-8z"/>',
    "mail": '<rect x="3.5" y="5.5" width="17" height="13" rx="1.5"/><path d="M4 6.5l8 6 8-6"/>',
    "phone": '<path d="M6.5 3.5h3l1.5 4-2 1.3a10 10 0 0 0 6.2 6.2l1.3-2 4 1.5v3a1.8 1.8 0 0 1-2 1.8C10.4 18.7 5.3 13.6 4.7 5.5a1.8 1.8 0 0 1 1.8-2z"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10" rx="1.5"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>',
    "pin": '<path d="M12 21s6.5-5.6 6.5-11a6.5 6.5 0 0 0-13 0c0 5.4 6.5 11 6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
    "dash": '<circle cx="12" cy="12" r="8.5"/><path d="M8.5 12h7"/>',
    "leaf": '<path d="M5 19c0-8 5-13.5 14.5-14-0.3 9.6-5.8 14.5-14 14.5z"/><path d="M5 19l7-7"/>',
    "scale": '<path d="M12 4v16M6 20h12"/><path d="M5 7h14"/><path d="M5 7l-2.5 6a2.5 2.5 0 0 0 5 0L5 7zM19 7l-2.5 6a2.5 2.5 0 0 0 5 0L19 7z"/>',
    "calendar": '<rect x="4" y="5.5" width="16" height="15" rx="1.5"/><path d="M4 10h16M8.5 3.5v4M15.5 3.5v4"/>',
    "chevron": '<path d="M9 6l6 6-6 6"/>',
    "download": '<path d="M12 4v11"/><path d="M7 10.5l5 5 5-5"/><path d="M5 19.5h14"/>',
    "play": '<path d="M7 4.5v15l12-7.5-12-7.5z"/>',
}


def icon(name, cls=""):
    fill = 'fill="currentColor" stroke="none"' if name == "play" else 'fill="none" stroke="currentColor"'
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" {fill} stroke-width="1.5" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


# ---------------------------------------------------------------- helpers
def noise(u, opacity=0.07):
    """Subtle film grain to make flat gradients feel photographic."""
    return (f'<filter id="{u}n" x="0" y="0" width="100%" height="100%">'
            f'<feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch"/>'
            f'<feColorMatrix values="0 0 0 0 .25 0 0 0 0 .2 0 0 0 0 .15 0 0 0 .9 0"/></filter>',
            f'<rect width="100%" height="100%" filter="url(#{u}n)" opacity="{opacity}"/>')


def blur(u, sd, name="b"):
    return f'<filter id="{u}{name}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{sd}"/></filter>'


def svg(vb, body, defs="", aspect="xMidYMid slice", label=""):
    lab = f' role="img" aria-label="{label}"' if label else ' aria-hidden="true"'
    return (f'<svg viewBox="{vb}" preserveAspectRatio="{aspect}" xmlns="http://www.w3.org/2000/svg"{lab}>'
            f'<defs>{defs}</defs>{body}</svg>')


def plume(cx, cy, r, seed=1, n=56, color="#FFFFFF", sw=1.0, op=0.95, core="#F2ECE2"):
    """A down cluster: many fine, slightly curved filaments from a small core."""
    rnd = random.Random(seed)
    out = [f'<g stroke="{color}" stroke-width="{sw}" fill="none" stroke-linecap="round" opacity="{op}">']
    for i in range(n):
        a = 2 * math.pi * i / n + rnd.uniform(-0.12, 0.12)
        L = r * rnd.uniform(0.55, 1.0)
        ex, ey = cx + L * math.cos(a), cy + L * math.sin(a)
        bend = rnd.uniform(-0.35, 0.35) * L
        mx, my = cx + 0.5 * L * math.cos(a) - bend * math.sin(a), cy + 0.5 * L * math.sin(a) + bend * math.cos(a)
        out.append(f'<path d="M{cx:.1f},{cy:.1f} Q{mx:.1f},{my:.1f} {ex:.1f},{ey:.1f}"/>')
    out.append('</g>')
    out.append(f'<g stroke="{color}" stroke-width="{sw*0.6:.2f}" fill="none" opacity="{op*0.55:.2f}">')
    for i in range(n // 2):
        a = rnd.uniform(0, 2 * math.pi)
        L = r * rnd.uniform(0.3, 0.75)
        ex, ey = cx + L * math.cos(a), cy + L * math.sin(a)
        out.append(f'<path d="M{cx:.1f},{cy:.1f} L{ex:.1f},{ey:.1f}"/>')
    out.append('</g>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{max(r*0.09,1.5):.1f}" fill="{core}"/>')
    return "".join(out)


# ---------------------------------------------------------------- object groups
def g_duvet_stack(u, layers=3, band=True):
    """Folded quilted duvet stack, local box ~300 x 210."""
    d = (f'<linearGradient id="{u}dl" x1="0" y1="0" x2="0" y2="1">'
         f'<stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#F7F2EA"/><stop offset="1" stop-color="#E4DACA"/></linearGradient>'
         f'<radialGradient id="{u}dp" cx=".5" cy=".35" r=".6"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>')
    shape = "M14,8 C100,-1 200,-1 286,8 C301,24 301,46 286,60 C200,69 100,69 14,60 C-1,46 -1,24 14,8 Z"
    parts = [f'<defs>{d}</defs>']
    for i in range(layers):
        y = 52 * (layers - 1 - i) + 40
        x = [0, 6, -3, 4][i % 4]
        parts.append(f'<g transform="translate({x},{y})">'
                     f'<path d="{shape}" fill="url(#{u}dl)" stroke="#DCD0BD" stroke-width="1"/>'
                     f'<ellipse cx="150" cy="22" rx="120" ry="14" fill="url(#{u}dp)"/>'
                     f'<g stroke="#D3C6B1" stroke-width="1.1" stroke-dasharray="3 3" fill="none">'
                     f'<path d="M75,6 C73,26 73,44 75,63"/><path d="M150,4 C148,26 148,44 150,65"/><path d="M225,6 C227,26 227,44 225,63"/>'
                     f'</g></g>')
    top = 40
    if band:
        parts.append(f'<rect x="206" y="{top-4}" width="24" height="{52*(layers-1)+72}" fill="#E5D6B9" opacity=".9"/>'
                     f'<rect x="206" y="{top-4}" width="2" height="{52*(layers-1)+72}" fill="#CDB98F" opacity=".6"/>'
                     f'<g transform="translate(190,{52*(layers-1)+top+40}) rotate(-6)">'
                     f'<rect width="62" height="34" rx="3" fill="#FBF7EF" stroke="#C8B48A" stroke-width=".8"/>'
                     f'<circle cx="8" cy="17" r="2.4" fill="none" stroke="#C8B48A" stroke-width=".8"/>'
                     f'<text x="36" y="22" text-anchor="middle" font-family="{SERIF}" font-size="15" fill="#1F2A37">bline</text></g>')
    return "".join(parts)


def g_sheet_stack(u, colors=("#FBF8F3", "#E6E9E1", "#F1EADF", "#DDE2D6"), ribbon=True):
    """Crisp folded Tencel sheets, local box ~260 x 150."""
    parts = [f'<defs><linearGradient id="{u}sh" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".55"/>'
             f'<stop offset="1" stop-color="#000" stop-opacity=".05"/></linearGradient></defs>']
    n = len(colors)
    for i, c in enumerate(colors):
        y = 30 * (n - 1 - i) + 20
        x = [0, 4, -2, 3][i % 4]
        parts.append(f'<g transform="translate({x},{y})">'
                     f'<rect width="260" height="32" rx="7" fill="{c}" stroke="#D8CEBE" stroke-width=".9"/>'
                     f'<rect width="260" height="32" rx="7" fill="url(#{u}sh)"/>'
                     f'<path d="M8,11 H252 M8,21 H252" stroke="#000" stroke-opacity=".05"/></g>')
    if ribbon:
        h = 30 * (n - 1) + 36
        parts.append(f'<rect x="90" y="18" width="16" height="{h}" fill="#7C8B74" opacity=".9"/>'
                     f'<path d="M98,20 C80,-2 62,4 70,16 C74,22 88,22 98,20 Z" fill="#8E9C86"/>'
                     f'<path d="M98,20 C116,-2 134,4 126,16 C122,22 108,22 98,20 Z" fill="#8E9C86"/>'
                     f'<circle cx="98" cy="20" r="4.5" fill="#6E7C67"/>')
    return "".join(parts)


def g_pillow(u, light="#FFFFFF", dark="#E5DBCB", seam="#D8CCB8"):
    """Plump pillow, local box 300 x 180."""
    shape = "M20,30 C60,6 240,6 280,30 C300,70 300,110 280,150 C240,174 60,174 20,150 C0,110 0,70 20,30 Z"
    inner = "M30,38 C70,18 230,18 270,38 C286,72 286,108 270,142 C230,162 70,162 30,142 C14,108 14,72 30,38 Z"
    return (f'<defs><radialGradient id="{u}pg" cx=".45" cy=".4" r=".7"><stop offset="0" stop-color="{light}"/>'
            f'<stop offset=".7" stop-color="{light}" stop-opacity=".0"/></radialGradient>'
            f'<linearGradient id="{u}pb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{light}"/><stop offset="1" stop-color="{dark}"/></linearGradient></defs>'
            f'<path d="{shape}" fill="url(#{u}pb)" stroke="{seam}" stroke-width="1"/>'
            f'<path d="{shape}" fill="url(#{u}pg)"/>'
            f'<path d="{inner}" fill="none" stroke="{seam}" stroke-width=".9" opacity=".7"/>')


def g_silk(u, base=("#E9DAC1", "#FAF3E7", "#D8C3A0", "#F4EADB")):
    """Silk pillowcase with sheen, local box 300 x 170."""
    shape = "M18,26 C70,8 230,8 282,26 C298,64 298,106 282,144 C230,162 70,162 18,144 C2,106 2,64 18,26 Z"
    a, b, c, d = base
    return (f'<defs><linearGradient id="{u}sk" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{a}"/><stop offset=".32" stop-color="{b}"/><stop offset=".55" stop-color="{c}"/>'
            f'<stop offset=".78" stop-color="{d}"/><stop offset="1" stop-color="{c}"/></linearGradient>'
            f'{blur(u, 6, "sb")}</defs>'
            f'<path d="{shape}" fill="url(#{u}sk)"/>'
            f'<g filter="url(#{u}sb)" opacity=".75"><path d="M40,120 C110,60 170,40 250,36" stroke="#fff" stroke-width="10" fill="none"/>'
            f'<path d="M70,148 C140,110 200,90 270,84" stroke="#fff" stroke-width="5" fill="none" opacity=".7"/></g>'
            f'<path d="M232,16 C236,60 236,110 232,154" stroke="#000" stroke-opacity=".08" stroke-width="1.2" fill="none"/>'
            f'<path d="{shape}" fill="none" stroke="#000" stroke-opacity=".06"/>')


def g_hand(u):
    """Stylised open palm seen from above, local box 400 x 420."""
    skin, shade, hi = "#E6C8AC", "#D2AE8F", "#F0DBC7"
    fingers = ""
    for (x, y, h, rot) in [(108, 92, 150, -14), (156, 62, 176, -5), (206, 58, 178, 4), (254, 84, 150, 13)]:
        fingers += (f'<rect x="{x}" y="{y}" width="40" height="{h}" rx="20" fill="url(#{u}sk)" '
                    f'transform="rotate({rot} {x+20} {y+h})"/>')
    return (f'<defs><linearGradient id="{u}sk" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{hi}"/>'
            f'<stop offset="1" stop-color="{skin}"/></linearGradient>'
            f'<radialGradient id="{u}pa" cx=".5" cy=".45" r=".6"><stop offset="0" stop-color="{hi}"/><stop offset="1" stop-color="{skin}"/></radialGradient></defs>'
            f'<path d="M150,330 C150,380 140,420 130,440 L300,440 C290,410 285,380 290,330 Z" fill="{skin}"/>'
            f'{fingers}'
            f'<path d="M300,250 C330,214 360,196 380,206 C396,214 388,240 366,262 C344,286 322,300 300,306 Z" fill="url(#{u}sk)"/>'
            f'<path d="M96,230 C94,180 140,156 214,156 C292,156 320,190 316,250 C312,318 268,350 210,352 C150,354 98,316 96,230 Z" fill="url(#{u}pa)"/>'
            f'<path d="M126,282 C170,300 240,300 290,270" stroke="{shade}" stroke-width="2" fill="none" opacity=".55"/>'
            f'<path d="M140,214 C180,206 230,208 268,224" stroke="{shade}" stroke-width="1.6" fill="none" opacity=".45"/>')


# ---------------------------------------------------------------- scenes
def bedroom(label="Slaapkamer met donsdekbed in ochtendlicht", w=1248, h=560):
    u = uid()
    ndef, nrect = noise(u, 0.06)
    defs = (f'<linearGradient id="{u}w" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EFE8DC"/><stop offset="1" stop-color="#E2D6C3"/></linearGradient>'
            f'<linearGradient id="{u}f" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#D6C7AE"/><stop offset="1" stop-color="#C6B596"/></linearGradient>'
            f'<linearGradient id="{u}hb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#D3C5AD"/><stop offset="1" stop-color="#C2B193"/></linearGradient>'
            f'<linearGradient id="{u}dv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#EEE6D9"/></linearGradient>'
            f'<linearGradient id="{u}dr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F2EBE0"/><stop offset="1" stop-color="#DED2BF"/></linearGradient>'
            f'<radialGradient id="{u}lamp" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFF4DD" stop-opacity=".9"/><stop offset="1" stop-color="#FFF4DD" stop-opacity="0"/></radialGradient>'
            f'<clipPath id="{u}dc"><path d="M228,372 C420,350 800,350 992,372 L1006,486 C800,500 420,500 214,486 Z"/></clipPath>'
            + blur(u, 22) + blur(u, 8, "s") + ndef)
    quilt = "".join(f'<path d="M{x},350 C{x-4},420 {x-6},460 {x-8},500" />' for x in range(318, 1000, 96))
    quilt += "".join(f'<path d="M210,{y} C420,{y-14} 800,{y-14} 1010,{y}"/>' for y in (408, 446))
    puffs = "".join(f'<ellipse cx="{x}" cy="{y}" rx="34" ry="11" fill="#fff" opacity=".8"/>' for x in range(270, 990, 96) for y in (386, 426, 466))
    body = (f'<rect width="{w}" height="{h}" fill="url(#{u}w)"/>'
            f'<g filter="url(#{u}b)" opacity=".55"><polygon points="760,0 1040,0 900,470 600,470" fill="#FFF9EE"/>'
            f'<polygon points="1080,0 1160,0 1040,470 960,470" fill="#FFF9EE" opacity=".7"/></g>'
            f'<rect y="470" width="{w}" height="{h-470}" fill="url(#{u}f)"/>'
            f'<rect y="468" width="{w}" height="3" fill="#BCA988" opacity=".35"/>'
            # side stool with vase
            f'<rect x="96" y="380" width="96" height="92" rx="6" fill="#CDBD9F"/><rect x="96" y="380" width="96" height="8" rx="3" fill="#BEAC8B"/>'
            f'<path d="M128,380 C120,350 122,330 136,322 L152,322 C166,330 168,350 160,380 Z" fill="#EFE8DC" stroke="#D8CCB8"/>'
            f'<g stroke="#7C8B74" stroke-width="2" fill="none" stroke-linecap="round"><path d="M144,324 C140,270 120,230 100,200"/><path d="M144,324 C150,260 170,226 196,206"/>'
            f'<path d="M144,324 C146,280 150,240 146,190"/></g>'
            f'<g fill="#8E9C86">' + "".join(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="3.5" transform="rotate({r} {x} {y})"/>' for x, y, r in
                                             [(108, 212, -40), (118, 236, -30), (172, 222, 30), (184, 214, 40), (160, 240, 20), (147, 200, -80), (146, 222, 80), (126, 258, -20)]) + '</g>'
            # shadow + bed
            f'<ellipse cx="610" cy="512" rx="430" ry="20" fill="#7F6C52" opacity=".35" filter="url(#{u}s)"/>'
            f'<rect x="270" y="140" width="680" height="260" rx="22" fill="url(#{u}hb)"/>'
            + "".join(f'<rect x="{x}" y="150" width="2" height="240" fill="#B5A385" opacity=".5"/>' for x in range(338, 950, 68)) +
            f'<rect x="240" y="386" width="740" height="104" rx="10" fill="#DBCDB6"/>'
            f'<rect x="262" y="488" width="14" height="22" fill="#A99472"/><rect x="944" y="488" width="14" height="22" fill="#A99472"/>'
            # pillows
            f'<g transform="translate(312,250) scale(0.95,0.68)">{g_pillow(u+"p1")}</g>'
            f'<g transform="translate(624,250) scale(0.95,0.68)">{g_pillow(u+"p2")}</g>'
            f'<g transform="translate(478,300) scale(0.72,0.5)">{g_silk(u+"s1")}</g>'
            # duvet
            f'<path d="M228,372 C420,350 800,350 992,372 L1006,486 C800,500 420,500 214,486 Z" fill="url(#{u}dv)"/>'
            f'<g clip-path="url(#{u}dc)">{puffs}<g stroke="#E0D5C3" stroke-width="1.4" fill="none">{quilt}</g></g>'
            f'<path d="M214,486 C420,500 800,500 1006,486 L1000,520 C800,534 420,534 220,520 Z" fill="url(#{u}dr)"/>'
            f'<path d="M228,372 C420,350 800,350 992,372 L990,388 C800,368 420,368 230,388 Z" fill="#FBF8F3" stroke="#E3D9C8"/>'
            # sage throw
            f'<path d="M760,366 C820,364 880,366 930,370 L948,494 C900,500 840,502 788,500 Z" fill="#7C8B74" opacity=".92"/>'
            f'<path d="M760,366 C820,364 880,366 930,370 L932,382 C880,378 820,376 762,378 Z" fill="#91A089"/>'
            f'<path d="M788,500 C840,502 900,500 948,494 L944,528 C900,534 840,536 792,532 Z" fill="#6D7B66"/>'
            # nightstand + lamp
            f'<circle cx="1110" cy="250" r="120" fill="url(#{u}lamp)"/>'
            f'<rect x="1030" y="372" width="150" height="104" rx="6" fill="#C9B898"/><rect x="1030" y="372" width="150" height="9" rx="3" fill="#B8A582"/>'
            f'<path d="M1042,420 H1168" stroke="#B19D79" stroke-width="1.5"/><circle cx="1105" cy="398" r="3" fill="#A48F69"/>'
            f'<rect x="1088" y="352" width="30" height="20" rx="4" fill="#E9E1D4"/><path d="M1103,352 V282" stroke="#9B8764" stroke-width="3"/>'
            f'<path d="M1068,284 L1138,284 L1124,222 L1082,222 Z" fill="#F6EFE2" stroke="#E0D3BC"/>'
            f'<rect x="1046" y="356" width="30" height="16" rx="2" fill="#7C8B74" opacity=".8"/><rect x="1046" y="350" width="26" height="7" rx="2" fill="#E9E1D4"/>'
            + nrect)
    return svg(f"0 0 {w} {h}", body, defs, label=label)


def product_scene(kind, bg=("#F1EBE1", "#E2D7C6"), label="", w=400, h=460):
    """Studio-style product shot on a soft backdrop."""
    u = uid()
    ndef, nrect = noise(u, 0.05)
    defs = (f'<radialGradient id="{u}bg" cx=".5" cy=".38" r=".85"><stop offset="0" stop-color="{bg[0]}"/><stop offset="1" stop-color="{bg[1]}"/></radialGradient>'
            f'<linearGradient id="{u}fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".07"/></linearGradient>'
            + blur(u, 10, "s") + ndef)
    floor = f'<rect y="{h*0.68:.0f}" width="{w}" height="{h*0.32:.0f}" fill="url(#{u}fl)"/>'
    if kind == "duvet":
        obj = (f'<ellipse cx="200" cy="356" rx="160" ry="16" fill="#6E5B42" opacity=".28" filter="url(#{u}s)"/>'
               f'<g transform="translate(50,110)">{g_duvet_stack(u+"d")}</g>')
    elif kind == "duvet-big":
        obj = (f'<ellipse cx="200" cy="372" rx="170" ry="16" fill="#6E5B42" opacity=".28" filter="url(#{u}s)"/>'
               f'<g transform="translate(40,74) scale(1.07)">{g_duvet_stack(u+"d", layers=4)}</g>')
    elif kind == "sheets":
        obj = (f'<ellipse cx="200" cy="338" rx="150" ry="14" fill="#6E5B42" opacity=".25" filter="url(#{u}s)"/>'
               f'<g transform="translate(70,190)">{g_sheet_stack(u+"t")}</g>'
               f'<g transform="translate(150,300) scale(.5)">{g_pillow(u+"pp", "#FBF8F3", "#E6DED1")}</g>')
    elif kind == "silk":
        obj = (f'<ellipse cx="200" cy="330" rx="140" ry="14" fill="#6E5B42" opacity=".22" filter="url(#{u}s)"/>'
               f'<g transform="translate(60,170) scale(.94)">{g_silk(u+"k")}</g>')
    elif kind == "pillow":
        obj = (f'<ellipse cx="200" cy="330" rx="140" ry="14" fill="#6E5B42" opacity=".22" filter="url(#{u}s)"/>'
               f'<g transform="translate(55,165) scale(.97)">{g_pillow(u+"pl")}</g>')
    else:
        obj = ""
    return svg(f"0 0 {w} {h}", f'<rect width="{w}" height="{h}" fill="url(#{u}bg)"/>{floor}{obj}{nrect}', defs, label=label)


def bundle_scene(label="De Slaapset: donsdekbed, Tencel set en twee kussens"):
    u = uid()
    ndef, nrect = noise(u, 0.05)
    defs = (f'<radialGradient id="{u}bg" cx=".4" cy=".35" r=".9"><stop offset="0" stop-color="#F2ECE2"/><stop offset="1" stop-color="#DCD0BC"/></radialGradient>'
            + blur(u, 12, "s") + ndef)
    body = (f'<rect width="700" height="560" fill="url(#{u}bg)"/>'
            f'<rect y="390" width="700" height="170" fill="#000" opacity=".04"/>'
            f'<ellipse cx="340" cy="430" rx="290" ry="22" fill="#6E5B42" opacity=".28" filter="url(#{u}s)"/>'
            f'<g transform="translate(150,120) scale(.95)">{g_pillow(u+"a")}</g>'
            f'<g transform="translate(300,140) scale(.95)">{g_pillow(u+"b", "#FFFFFF", "#E8DFD2")}</g>'
            f'<g transform="translate(70,214) scale(1.05)">{g_duvet_stack(u+"d", band=True)}</g>'
            f'<g transform="translate(380,300)">{g_sheet_stack(u+"t", ribbon=True)}</g>'
            f'<g transform="translate(410,404) scale(.52)">{g_silk(u+"k")}</g>' + nrect)
    return svg("0 0 700 560", body, defs, label=label)


def seam_detail(label="Detail van cassettes met tussenwanden"):
    u = uid()
    ndef, nrect = noise(u, 0.06)
    defs = (f'<radialGradient id="{u}c" cx=".45" cy=".4" r=".65"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".7" stop-color="#F3EDE3"/><stop offset="1" stop-color="#DCD0BC"/></radialGradient>'
            + ndef)
    cells = ""
    for i in range(-2, 8):
        for j in range(-2, 8):
            cells += f'<rect x="{i*110}" y="{j*110}" width="106" height="106" rx="26" fill="url(#{u}c)"/>'
    stitches = "".join(f'<path d="M{i*110-2},-240 V900" />' for i in range(-2, 9)) + "".join(f'<path d="M-240,{j*110-2} H900" />' for j in range(-2, 9))
    body = (f'<rect width="400" height="400" fill="#D8CCB8"/>'
            f'<g transform="rotate(-14 200 200)">{cells}<g stroke="#B9A98D" stroke-width="1.3" stroke-dasharray="4 3.5" fill="none">{stitches}</g></g>'
            f'<g transform="translate(250,280) rotate(-8)"><rect width="118" height="64" rx="3" fill="#F8F3EA" stroke="#CBB994"/>'
            f'<text x="59" y="27" text-anchor="middle" font-family="{SERIF}" font-size="18" fill="#1F2A37">bline</text>'
            f'<text x="59" y="46" text-anchor="middle" font-family="{SANS}" font-size="8" letter-spacing="1.6" fill="#7C8B74">95% DONS · 750+</text></g>'
            + nrect)
    return svg("0 0 400 400", body, defs, label=label)


def hand_down(label="Hand met een donsbolletje", bg=("#EDE6DA", "#D9CCB7")):
    u = uid()
    ndef, nrect = noise(u, 0.05)
    defs = (f'<radialGradient id="{u}bg" cx=".5" cy=".4" r=".8"><stop offset="0" stop-color="{bg[0]}"/><stop offset="1" stop-color="{bg[1]}"/></radialGradient>'
            f'<radialGradient id="{u}glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff" stop-opacity=".8"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>'
            + blur(u, 10, "s") + ndef)
    body = (f'<rect width="400" height="420" fill="url(#{u}bg)"/>'
            f'<ellipse cx="210" cy="300" rx="150" ry="50" fill="#6E5B42" opacity=".18" filter="url(#{u}s)"/>'
            f'<g transform="translate(0,10)">{g_hand(u)}</g>'
            f'<circle cx="208" cy="228" r="110" fill="url(#{u}glow)"/>'
            + plume(208, 226, 92, seed=7, n=90, color="#FFFFFF", sw=1.1, op=.95)
            + plume(208, 226, 60, seed=9, n=50, color="#F4EEE4", sw=.9, op=.8)
            + nrect)
    return svg("0 0 400 420", body, defs, label=label)


def step_art(kind):
    u = uid()
    ink, gold = "#1F2A37", "#B8996A"
    if kind == "factory":
        b = (f'<path d="M40,130 H300" stroke="{ink}" stroke-width="1.2" opacity=".35"/>'
             f'<path d="M70,130 V72 L110,52 V72 L150,52 V72 L190,52 V72 L230,52 V130" fill="#F7F4EF" stroke="{ink}" stroke-width="1.4" stroke-linejoin="round"/>'
             f'<path d="M110,52 V72 M150,52 V72 M190,52 V72" stroke="{gold}" stroke-width="1.4"/>'
             f'<rect x="240" y="40" width="16" height="90" fill="#F7F4EF" stroke="{ink}" stroke-width="1.4"/>'
             f'<path d="M248,34 C240,22 256,16 250,6" stroke="{gold}" stroke-width="1.2" fill="none"/>'
             + "".join(f'<rect x="{x}" y="88" width="20" height="16" fill="#E9E1D4" stroke="{ink}" stroke-width="1.1"/>' for x in (86, 120, 154, 188))
             + f'<rect x="132" y="110" width="26" height="20" fill="{gold}" opacity=".35" stroke="{ink}" stroke-width="1.1"/>')
    elif kind == "inspect":
        b = (f'<rect x="60" y="56" width="170" height="74" rx="14" fill="#FFFDF9" stroke="{ink}" stroke-width="1.3"/>'
             f'<g stroke="{ink}" stroke-opacity=".3" stroke-dasharray="3 3"><path d="M117,58 V128 M174,58 V128 M62,93 H228"/></g>'
             f'<circle cx="196" cy="70" r="34" fill="#F7F4EF" fill-opacity=".85" stroke="{ink}" stroke-width="1.6"/>'
             f'<path d="M220,94 L248,122" stroke="{ink}" stroke-width="5" stroke-linecap="round"/>'
             f'<path d="M181,71 L192,82 L212,60" stroke="{gold}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
             f'<path d="M40,130 H300" stroke="{ink}" stroke-width="1.2" opacity=".35"/>')
    else:
        b = (f'<path d="M30,130 H300" stroke="{ink}" stroke-width="1.2" opacity=".35"/>'
             f'<path d="M58,70 H150 V122 H58 Z" fill="#F7F4EF" stroke="{ink}" stroke-width="1.4"/>'
             f'<path d="M150,86 H182 L200,104 V122 H150" fill="#F7F4EF" stroke="{ink}" stroke-width="1.4" stroke-linejoin="round"/>'
             f'<circle cx="84" cy="124" r="9" fill="#F7F4EF" stroke="{ink}" stroke-width="1.4"/><circle cx="178" cy="124" r="9" fill="#F7F4EF" stroke="{ink}" stroke-width="1.4"/>'
             f'<rect x="78" y="80" width="40" height="30" fill="#E9E1D4" stroke="{gold}" stroke-width="1.2"/><path d="M98,80 V110" stroke="{gold}" stroke-width="1.2"/>'
             f'<path d="M228,130 V88 L256,66 L284,88 V130" fill="#F7F4EF" stroke="{ink}" stroke-width="1.4" stroke-linejoin="round"/>'
             f'<rect x="248" y="104" width="16" height="26" fill="{gold}" opacity=".4" stroke="{ink}" stroke-width="1.1"/>'
             f'<g transform="translate(240,40)"><rect width="22" height="5" fill="#B5615A" opacity=".75"/><rect y="5" width="22" height="5" fill="#fff" stroke="#ddd" stroke-width=".3"/><rect y="10" width="22" height="5" fill="#3E5F8A" opacity=".75"/>'
             f'<path d="M0,0 V30" stroke="{ink}" stroke-width="1.1"/></g>'
             f'<path d="M210,104 H222" stroke="{gold}" stroke-width="1.4" stroke-dasharray="2 3"/>')
    return svg("0 0 340 150", f'<rect width="340" height="150" fill="#F1EBE1"/>{b}', aspect="xMidYMid meet")


def video_scene(kind):
    u = uid()
    ndef, nrect = noise(u, 0.08)
    if kind == "sort":
        defs = (f'<radialGradient id="{u}bg" cx=".55" cy=".45" r=".8"><stop offset="0" stop-color="#4A4E52"/><stop offset="1" stop-color="#1E242C"/></radialGradient>'
                f'<radialGradient id="{u}dr" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#6B6A66" stop-opacity=".6"/><stop offset="1" stop-color="#3A3F45" stop-opacity=".2"/></radialGradient>'
                + blur(u, 30) + blur(u, 2.2, "d") + ndef)
        pl = ""
        rnd = random.Random(3)
        for i in range(26):
            x, y, r = rnd.uniform(140, 560), rnd.uniform(80, 400), rnd.uniform(12, 34)
            far = i % 3 == 0
            g = plume(x, y, r, seed=i + 20, n=34, color="#F4EEE4", sw=.8, op=.55 if far else .9, core="#E9E1D4")
            pl += f'<g filter="url(#{u}d)">{g}</g>' if far else g
        body = (f'<rect width="700" height="480" fill="url(#{u}bg)"/>'
                f'<polygon points="0,0 260,0 520,480 160,480" fill="#FFE9C4" opacity=".14" filter="url(#{u}b)"/>'
                f'<circle cx="350" cy="240" r="210" fill="url(#{u}dr)" stroke="#fff" stroke-opacity=".12" stroke-width="2"/>'
                f'<circle cx="350" cy="240" r="170" fill="none" stroke="#fff" stroke-opacity=".06" stroke-width="14"/>'
                f'{pl}'
                f'<rect x="0" y="430" width="700" height="50" fill="#14191F" opacity=".6"/>' + nrect)
        return svg("0 0 700 480", body, defs)
    if kind == "inspect":
        defs = (f'<linearGradient id="{u}bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4C4A47"/><stop offset="1" stop-color="#2A2F36"/></linearGradient>'
                f'<radialGradient id="{u}gl" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFF3D9" stop-opacity=".55"/><stop offset="1" stop-color="#FFF3D9" stop-opacity="0"/></radialGradient>'
                f'<linearGradient id="{u}tb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F4EEE4"/><stop offset="1" stop-color="#D7CAB4"/></linearGradient>'
                + ndef)
        grid = "".join(f'<path d="M{150+i*80},250 L{100+i*100},440" />' for i in range(6)) + "".join(f'<path d="M{150-k*12},{250+k*48} H{550+k*12}"/>' for k in (1, 2, 3))
        body = (f'<rect width="700" height="480" fill="url(#{u}bg)"/>'
                f'<ellipse cx="350" cy="300" rx="300" ry="170" fill="url(#{u}gl)"/>'
                f'<path d="M150,250 H550 L610,440 H90 Z" fill="url(#{u}tb)"/>'
                f'<g stroke="#C9BBA2" stroke-width="1.4" stroke-dasharray="5 4" fill="none">{grid}</g>'
                f'<path d="M520,0 V60 L430,140" stroke="#20262E" stroke-width="6" fill="none"/>'
                f'<path d="M390,120 L470,160 L452,190 L372,150 Z" fill="#1A1F26"/>'
                f'<path d="M378,152 L456,190 L380,330 L250,260 Z" fill="#FFF3D9" opacity=".12"/>'
                f'<g transform="translate(480,300) rotate(8)"><rect width="110" height="140" rx="6" fill="#F7F4EF"/><rect x="34" y="-8" width="42" height="16" rx="4" fill="#7C8B74"/>'
                + "".join(f'<path d="M16,{30+i*24} l6,6 l10,-12" stroke="#7C8B74" stroke-width="2.2" fill="none" stroke-linecap="round"/><rect x="40" y="{30+i*24}" width="54" height="5" rx="2" fill="#D9CDB8"/>' for i in range(4))
                + '</g>' + nrect)
        return svg("0 0 700 480", body, defs)
    # joost / talking head
    defs = (f'<linearGradient id="{u}bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#55544F"/><stop offset="1" stop-color="#262C33"/></linearGradient>'
            + blur(u, 3.5, "d") + blur(u, 30) + ndef)
    rolls = ""
    rnd = random.Random(5)
    cols = ["#E9E1D4", "#C9D0C2", "#F4EFE6", "#B9A98D", "#8E9C86", "#DCD1BF"]
    for row, y in enumerate((70, 190, 310)):
        rolls += f'<rect x="0" y="{y+52}" width="700" height="8" fill="#1B2028" opacity=".8"/>'
        x = 10
        while x < 700:
            r = rnd.uniform(22, 30)
            c = rnd.choice(cols)
            rolls += f'<circle cx="{x+r:.0f}" cy="{y+52-r:.0f}" r="{r:.0f}" fill="{c}" opacity=".85"/><circle cx="{x+r:.0f}" cy="{y+52-r:.0f}" r="5" fill="#2A2F36" opacity=".6"/>'
            x += 2 * r + 4
    body = (f'<rect width="700" height="480" fill="url(#{u}bg)"/>'
            f'<g filter="url(#{u}d)" opacity=".7">{rolls}</g>'
            f'<rect width="700" height="480" fill="#1F2A37" opacity=".25"/>'
            f'<ellipse cx="420" cy="230" rx="200" ry="200" fill="#FFF0D6" opacity=".12" filter="url(#{u}b)"/>'
            f'<path d="M290,480 C292,400 330,350 420,340 C510,350 548,400 552,480 Z" fill="#2B3A4A"/>'
            f'<path d="M395,342 C400,360 440,360 446,342 L440,318 H400 Z" fill="#CFA98A"/>'
            f'<ellipse cx="420" cy="262" rx="52" ry="64" fill="#DDBB9E"/>'
            f'<path d="M368,250 C362,200 400,184 426,186 C462,188 480,212 472,250 C466,226 446,214 420,214 C394,214 376,226 368,250 Z" fill="#4A3B30"/>'
            f'<path d="M375,348 L420,372 L466,348" stroke="#3B4C5E" stroke-width="3" fill="none"/>' + nrect)
    return svg("0 0 700 480", body, defs)


def avatar():
    u = uid()
    return svg("0 0 52 52", f'<rect width="52" height="52" fill="#DCD1BF"/><path d="M8,56 C10,40 18,34 26,34 C34,34 42,40 44,56 Z" fill="#2B3A4A"/>'
               f'<ellipse cx="26" cy="22" rx="9" ry="11" fill="#DDBB9E"/><path d="M17,20 C16,11 23,9 27,9 C33,10 36,14 35,20 C33,16 30,14 26,14 C22,14 19,16 17,20 Z" fill="#4A3B30"/>',
               label="Joost")


def factory_floor():
    u = uid()
    ndef, nrect = noise(u, 0.07)
    defs = (f'<linearGradient id="{u}bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E8DFD0"/><stop offset=".55" stop-color="#D2C4AC"/><stop offset="1" stop-color="#B9A88B"/></linearGradient>'
            f'<radialGradient id="{u}gl" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFF7E6" stop-opacity=".9"/><stop offset="1" stop-color="#FFF7E6" stop-opacity="0"/></radialGradient>'
            + ndef)
    b = f'<rect width="500" height="300" fill="url(#{u}bg)"/>'
    for k, (y, s) in enumerate([(70, .5), (110, .75), (170, 1.1)]):
        for i in range(-2, 3):
            x = 250 + i * 150 * s
            b += (f'<circle cx="{x:.0f}" cy="{y-40*s:.0f}" r="{40*s:.0f}" fill="url(#{u}gl)"/>'
                  f'<path d="M{x-14*s:.0f},{y-44*s:.0f} H{x+14*s:.0f} L{x+20*s:.0f},{y-34*s:.0f} H{x-20*s:.0f} Z" fill="#3E4650"/>'
                  f'<path d="M{x:.0f},0 V{y-44*s:.0f}" stroke="#3E4650" stroke-width="{1.2*s:.1f}"/>'
                  f'<rect x="{x-50*s:.0f}" y="{y+30*s:.0f}" width="{100*s:.0f}" height="{18*s:.0f}" fill="#6E6152"/>'
                  f'<rect x="{x-36*s:.0f}" y="{y+16*s:.0f}" width="{56*s:.0f}" height="{16*s:.0f}" rx="{5*s:.0f}" fill="#FBF8F3"/>'
                  f'<rect x="{x+22*s:.0f}" y="{y+8*s:.0f}" width="{16*s:.0f}" height="{24*s:.0f}" fill="#2E3540"/>')
    return svg("0 0 500 300", b + nrect, defs, label="Naaiatelier in de fabriek")


def scale_scene():
    u = uid()
    ndef, nrect = noise(u, 0.06)
    defs = f'<radialGradient id="{u}bg" cx=".5" cy=".3" r=".9"><stop offset="0" stop-color="#F0EAE0"/><stop offset="1" stop-color="#D3C6B0"/></radialGradient>' + ndef
    b = (f'<rect width="300" height="300" fill="url(#{u}bg)"/>'
         f'<rect x="50" y="200" width="200" height="40" rx="8" fill="#2E3540"/><rect x="40" y="186" width="220" height="16" rx="5" fill="#C9CDD2"/>'
         f'<rect x="112" y="210" width="76" height="22" rx="3" fill="#0F1419"/>'
         f'<text x="150" y="226" text-anchor="middle" font-family="{SANS}" font-size="13" font-weight="600" fill="#B8E0A8">520 g</text>'
         + plume(110, 160, 30, 31, 40) + plume(160, 150, 38, 32, 50) + plume(200, 164, 26, 33, 36) + plume(140, 120, 24, 34, 34) + plume(186, 126, 22, 35, 30)
         + nrect)
    return svg("0 0 300 300", b, defs, label="Vulgewicht wegen")


def lab_scene():
    u = uid()
    ndef, nrect = noise(u, 0.05)
    defs = (f'<linearGradient id="{u}bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E7ECE3"/><stop offset="1" stop-color="#C9D0C2"/></linearGradient>' + ndef)
    b = (f'<rect width="300" height="300" fill="url(#{u}bg)"/>'
         f'<ellipse cx="140" cy="190" rx="100" ry="40" fill="#fff" opacity=".55" stroke="#fff"/>'
         f'<ellipse cx="140" cy="186" rx="88" ry="33" fill="none" stroke="#A9B59F" stroke-width="1.2"/>'
         + plume(140, 180, 40, 41, 60, color="#FFFFFF") +
         f'<path d="M232,90 H262 M238,90 V140 L222,196 C219,206 226,212 234,212 H262 C270,212 276,206 273,196 L256,140 V90" fill="#fff" fill-opacity=".45" stroke="#5F6E58" stroke-width="1.4"/>'
         f'<path d="M226,180 H270 L273,196 C276,206 270,212 262,212 H234 C226,212 219,206 222,196 Z" fill="#7C8B74" opacity=".5"/>' + nrect)
    return svg("0 0 300 300", b, defs, label="Steekproef in het lab")


def boxes_scene():
    u = uid()
    ndef, nrect = noise(u, 0.06)
    defs = f'<linearGradient id="{u}bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EEE7DB"/><stop offset="1" stop-color="#D9CDB9"/></linearGradient>' + ndef

    def box(x, y, w, h):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#C9AE84"/><rect x="{x}" y="{y}" width="{w}" height="{h*0.12:.0f}" fill="#B99C70"/>'
                f'<rect x="{x+w/2-7:.0f}" y="{y}" width="14" height="{h}" fill="#D9C4A0" opacity=".8"/>'
                f'<text x="{x+w*0.25:.0f}" y="{y+h*0.62:.0f}" text-anchor="middle" font-family="{SERIF}" font-size="{h*0.2:.0f}" fill="#1F2A37" opacity=".75">bline</text>'
                f'<rect x="{x+w*0.62:.0f}" y="{y+h*0.4:.0f}" width="{w*0.3:.0f}" height="{h*0.32:.0f}" fill="#FBF8F3"/>'
                f'<path d="M{x+w*0.65:.0f},{y+h*0.5:.0f} h{w*0.22:.0f} M{x+w*0.65:.0f},{y+h*0.6:.0f} h{w*0.16:.0f}" stroke="#1F2A37" stroke-width="1.2" opacity=".5"/>')
    b = (f'<rect width="360" height="300" fill="url(#{u}bg)"/><rect y="250" width="360" height="50" fill="#000" opacity=".05"/>'
         + box(40, 160, 150, 92) + box(196, 176, 130, 76) + box(70, 76, 130, 84))
    return svg("0 0 360 300", b + nrect, defs, label="Dozen klaar voor verzending in Nederland")


def lab_report_scene():
    u = uid()
    ndef, nrect = noise(u, 0.05)
    defs = (f'<radialGradient id="{u}bg" cx=".4" cy=".35" r=".9"><stop offset="0" stop-color="#F2ECE2"/><stop offset="1" stop-color="#D8CBB5"/></radialGradient>'
            + blur(u, 12, "s") + ndef)
    rows = "".join(
        f'<rect x="40" y="{204+i*36}" width="110" height="7" rx="3" fill="#C9C0B2"/><rect x="200" y="{204+i*36}" width="60" height="7" rx="3" fill="#1F2A37" opacity=".75"/>'
        f'<path d="M290,{200+i*36} l6,6 l10,-12" stroke="#7C8B74" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
        f'<path d="M30,{226+i*36} H320" stroke="#E7E0D5"/>' for i in range(5))
    doc = (f'<rect width="350" height="440" rx="6" fill="#FFFDF9"/>'
           f'<text x="30" y="50" font-family="{SANS}" font-size="11" letter-spacing="2.5" fill="#7C8B74">LABRAPPORT</text>'
           f'<text x="30" y="88" font-family="{SERIF}" font-size="30" fill="#1F2A37">Partij BL-D-2610</text>'
           f'<text x="30" y="114" font-family="{SANS}" font-size="11" fill="#6E7581">Donsdekbed 4 seizoenen · steekproef 3 st.</text>'
           f'<rect x="30" y="140" width="290" height="1" fill="#B8996A" opacity=".6"/>'
           f'<text x="30" y="178" font-family="{SANS}" font-size="10" letter-spacing="1.6" fill="#6E7581">TEST</text>'
           f'<text x="200" y="178" font-family="{SANS}" font-size="10" letter-spacing="1.6" fill="#6E7581">UITSLAG</text>{rows}')
    seal = (f'<circle r="46" fill="#F7F1E6" stroke="#B8996A" stroke-width="1.5"/><circle r="38" fill="none" stroke="#B8996A" stroke-width=".8" stroke-dasharray="2 3"/>'
            f'<text y="-4" text-anchor="middle" font-family="{SERIF}" font-size="17" fill="#1F2A37">Voldoet</text>'
            f'<text y="14" text-anchor="middle" font-family="{SANS}" font-size="7.5" letter-spacing="1.4" fill="#7C8B74">AAN NORM</text>')
    body = (f'<rect width="640" height="576" fill="url(#{u}bg)"/>'
            f'<rect x="150" y="96" width="350" height="440" rx="6" fill="#4E3F2C" opacity=".25" filter="url(#{u}s)" transform="rotate(-4 325 316)"/>'
            f'<g transform="translate(140,70) rotate(-4 175 220)">{doc}</g>'
            f'<g transform="translate(470,140) rotate(10)">{seal}</g>'
            f'<ellipse cx="470" cy="470" rx="96" ry="40" fill="#4E3F2C" opacity=".2" filter="url(#{u}s)"/>'
            f'<ellipse cx="470" cy="456" rx="96" ry="40" fill="#fff" fill-opacity=".6" stroke="#fff"/>'
            f'<ellipse cx="470" cy="452" rx="84" ry="33" fill="none" stroke="#C9BBA2"/>'
            + plume(470, 446, 44, 51, 70) + nrect)
    return svg("0 0 640 576", body, defs, label="Labrapport met donsbolletje")
