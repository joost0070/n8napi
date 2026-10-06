# Bline-mailtemplates voor Klaviyo (HTML/CODE). Huisstijl van de site: warm wit, donkerblauwe knop, Poppins.
CDN='https://cdn.shopify.com/s/files/1/1112/3965/9859/files/'
LOGO=CDN+'bline-logo.png?v=1791194891&width=360'
U='{{ organization.url }}'
F="Poppins,'Segoe UI',Helvetica,Arial,sans-serif"
S="Georgia,'Times New Roman',serif"
INKT='#1D2330'; SUB='#5A6170'; BG='#FBF8F4'; ZAND='#F2EADF'; KNOP='#1F2A37'; LIJN='#E8E2D9'
KLEUREN=['beige','blauw','wit','grijs','zwart']
def beeld(k,w=600): return f"{CDN}bline-leeskussen-{k}-01.jpg?width={w}"
def hoesbeeld(k,w=300): return f"{CDN}bline-hoes-{k}-packshot-01.png?width={w}"
def item_beeld(var):
    # kies de juiste originele foto bij de producttitel (Shopify stuurt geen beeld mee in de checkout)
    s=''
    for i,k in enumerate(KLEUREN):
        kw='if' if i==0 else 'elif'
        s+=f"{{% {kw} 'Hoes' in {var} and '{k.capitalize()}' in {var} %}}{hoesbeeld(k)}"
    for k in KLEUREN:
        s+=f"{{% elif '{k.capitalize()}' in {var} %}}{beeld(k,300)}"
    return s+f"{{% else %}}{beeld('beige',300)}{{% endif %}}"
PRIJS="|floatformat:2|replace:'.|,'"

def knop(tekst,href):
    return f'''<tr><td align="center" class="zij knop" style="padding:26px 40px 0 40px;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;"><tr><td align="center" bgcolor="{KNOP}" style="background:{KNOP};border-radius:50px;mso-padding-alt:15px 44px;"><a href="{href}" target="_blank" style="display:inline-block;padding:15px 44px;font-family:{F};font-size:15px;font-weight:600;color:#ffffff;text-decoration:none;border-radius:50px;">{tekst}</a></td></tr></table></td></tr>'''
def kop(html): return f'<tr><td align="center" class="zij kop" style="padding:26px 40px 0 40px;font-family:{F};font-size:28px;line-height:35px;font-weight:600;color:{INKT};">{html}</td></tr>'
def tekst(html,pad='14px 44px 0 44px',size=16,align='center',kleur=SUB): return f'<tr><td align="{align}" class="zij" style="padding:{pad};font-family:{F};font-size:{size}px;line-height:{int(size*1.6)}px;color:{kleur};">{html}</td></tr>'
def foto(src,href,alt='Bline leeskussen',w=520): return f'<tr><td align="center" class="zij" style="padding:24px 40px 0 40px;"><a href="{href}" target="_blank"><img src="{src}" alt="{alt}" width="{w}" style="display:block;width:100%;max-width:{w}px;height:auto;border-radius:16px;"/></a></td></tr>'
def schuin(w): return f'<span style="font-family:{S};font-style:italic;font-weight:400;">{w}</span>'
def usp():
    rij=lambda t: f'<tr><td style="padding:5px 0;font-family:{F};font-size:14px;line-height:20px;color:{INKT};"><span style="color:#2F7A4B;font-weight:700;">&#10003;</span>&nbsp; {t}</td></tr>'
    return f'''<tr><td align="center" class="zij" style="padding:26px 40px 0 40px;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="background:{ZAND};border-radius:16px;"><tr><td style="padding:18px 24px;"><table border="0" cellpadding="0" cellspacing="0" role="presentation">{rij('Gratis verzending in Nederland en België')}{rij('Binnen 1-2 werkdagen in huis')}{rij('30 dagen proberen')}{rij('4,5 uit 5 op bol.com')}</table></td></tr></table></td></tr>'''
def code_blok(coupon,regel='Jouw persoonlijke code, 10% op je bestelling:'):
    return f'''<tr><td align="center" class="zij" style="padding:26px 40px 0 40px;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;"><tr><td align="center" style="border:2px dashed {INKT};border-radius:14px;padding:16px 30px;"><div style="font-family:{F};font-size:13px;line-height:18px;color:{SUB};">{regel}</div><div style="font-family:{F};font-size:26px;line-height:36px;font-weight:700;letter-spacing:2px;color:{INKT};">{{% coupon_code '{coupon}' %}}</div><div style="font-family:{F};font-size:12px;line-height:18px;color:{SUB};">Eenmalig te gebruiken. Vul hem in bij het afrekenen.</div></td></tr></table></td></tr>'''
def kleurrij():
    cel=lambda k: f'<td align="center" width="20%" style="padding:0 4px;"><a href="{U}/products/leeskussen-{k}" target="_blank" style="text-decoration:none;"><img src="{beeld(k,200)}" alt="Leeskussen {k}" width="96" style="display:block;width:100%;max-width:96px;height:auto;border-radius:12px;"/><div style="font-family:{F};font-size:12px;line-height:18px;color:{INKT};padding-top:6px;">{k.capitalize()}</div></a></td>'
    return f'<tr><td align="center" class="zij" style="padding:24px 30px 0 30px;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tr>{"".join(cel(k) for k in KLEUREN)}</tr></table></td></tr>'
def hulp(): return tekst(f'Vragen over de maat of de kleur? App of bel ons op <a href="https://wa.me/31638662833" target="_blank" style="color:{INKT};text-decoration:underline;">06 38 66 28 33</a>. We denken graag mee.',size=14)
def omhulsel(titel,preview,rijen,voet='Liever geen mails meer van Bline?'):
    return f'''<!DOCTYPE html><html lang="nl" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><meta http-equiv="X-UA-Compatible" content="IE=edge"/><title>{titel}</title><!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
<style>body,table,td,a{{-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}}table,td{{mso-table-lspace:0;mso-table-rspace:0;border-collapse:collapse}}img{{-ms-interpolation-mode:bicubic;border:0;height:auto;line-height:100%;outline:none;text-decoration:none}}body{{margin:0!important;padding:0!important;width:100%!important;background-color:{BG}}}.voet a{{color:#8b8f93!important;text-decoration:underline!important}}
@media screen and (max-width:620px){{.vel{{width:100%!important}}.zij{{padding-left:20px!important;padding-right:20px!important}}.kop{{font-size:24px!important;line-height:30px!important}}.knop a{{display:block!important;padding-left:20px!important;padding-right:20px!important}}}}</style></head>
<body style="margin:0;padding:0;background-color:{BG};"><div style="display:none;font-size:1px;color:{BG};line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;">{preview}</div>
<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="background-color:{BG};"><tr><td align="center" style="padding:24px 10px;">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" class="vel" width="600" style="width:600px;max-width:600px;background-color:#ffffff;border-radius:20px;">
<tr><td align="center" style="padding:30px 40px 0 40px;"><a href="{U}" target="_blank"><img src="{LOGO}" alt="Bline" width="120" style="display:block;width:120px;max-width:120px;height:auto;"/></a></td></tr>
{''.join(rijen)}
<tr><td align="center" class="zij voet" style="padding:34px 40px 30px 40px;font-family:{F};font-size:11px;line-height:18px;color:#8b8f93;border-top:0;">{voet} {{% unsubscribe 'Afmelden' %}}.<br/>{{{{ organization.name }}}} · {{{{ organization.full_address }}}}</td></tr>
</table></td></tr></table></body></html>'''

HALLO="Hoi{% if first_name %} {{ first_name|title }}{% endif %},"
def winkelwagen_regels():
    v='item.title'
    return f'''<tr><td align="center" class="zij" style="padding:22px 40px 0 40px;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="border:1px solid {LIJN};border-radius:16px;">
{{% for item in event.extra.line_items %}}<tr><td width="96" style="padding:14px 0 14px 16px;"><img src="{item_beeld(v)}" alt="{{{{ item.title }}}}" width="80" style="display:block;width:80px;height:auto;border-radius:10px;"/></td><td style="padding:14px 16px;font-family:{F};font-size:15px;line-height:21px;color:{INKT};"><strong style="font-weight:600;">{{{{ item.title }}}}</strong><br/><span style="color:{SUB};font-size:13px;">Aantal: {{{{ item.quantity|floatformat:0 }}}}</span></td><td align="right" style="padding:14px 16px 14px 0;font-family:{F};font-size:15px;color:{INKT};white-space:nowrap;">€{{{{ item.line_price{PRIJS} }}}}</td></tr>{{% endfor %}}
<tr><td colspan="2" style="padding:12px 16px;border-top:1px solid {LIJN};font-family:{F};font-size:15px;font-weight:600;color:{INKT};">Totaal, gratis verzonden</td><td align="right" style="padding:12px 16px;border-top:1px solid {LIJN};font-family:{F};font-size:15px;font-weight:600;color:{INKT};white-space:nowrap;">€{{{{ event|lookup:'$value'{PRIJS} }}}}</td></tr></table></td></tr>'''
CHECKOUT='{% if event.extra.responsive_checkout_url %}{{ event.extra.responsive_checkout_url }}{% else %}{{ organization.url }}{% endif %}'

T={}
# ---------- Flow 1: verlaten checkout ----------
T['C1']=('Bline | Verlaten checkout 1','Je leeskussen staat nog klaar','We hebben je keuze bewaard. Afrekenen kan wanneer je wilt.',[
 kop(f'Je leeskussen staat nog {schuin("klaar")}'),
 tekst(HALLO+'<br/>je was bijna klaar met je bestelling. We hebben je keuze bewaard, dus je kunt verder waar je was.'),
 winkelwagen_regels(), knop('Verder met bestellen',CHECKOUT), usp(), hulp()])
T['C2']=('Bline | Verlaten checkout 2','Nog vragen over je leeskussen?','Drie antwoorden die vaak helpen.',[
 kop(f'Nog even {schuin("twijfelen")}?'),
 tekst(HALLO+'<br/>logisch, het is een kussen waar je elke avond tegenaan leunt. Dit vragen mensen het vaakst:'),
 tekst(f'<strong style="color:{INKT};">Past hij op mijn bed?</strong><br/>Hij is 65 cm breed, 50 cm hoog en 45 cm diep. Twee passen naast elkaar op een bed vanaf 140 cm.<br/><br/><strong style="color:{INKT};">Hoe stevig is hij?</strong><br/>Er zit 3,8 kg traagschuim in. Je zakt er niet doorheen als je leunt, hij blijft staan.<br/><br/><strong style="color:{INKT};">Kan de hoes in de was?</strong><br/>Ja, rits hem eraf en was hem op 30 °C.<br/><br/><strong style="color:{INKT};">En als hij toch niet bevalt?</strong><br/>Je hebt 30 dagen om hem te proberen.','18px 44px 0 44px',15,'left'),
 foto(beeld('beige'),CHECKOUT),
 knop('Bekijk je bestelling',CHECKOUT),
 tekst('Kopers op bol.com geven hem een 4,5 uit 5.',size=14), hulp()])
T['C3']=('Bline | Verlaten checkout 3 (10%)','10% op je leeskussen, alleen voor jou','Je persoonlijke code staat in deze mail.',[
 kop(f'Een klein {schuin("duwtje")}'),
 tekst(HALLO+'<br/>je leeskussen ligt nog in je winkelwagen. Met deze persoonlijke code krijg je 10% korting op je bestelling.'),
 code_blok('BLINE_CHECKOUT10'), winkelwagen_regels(), knop('Bestellen met 10% korting',CHECKOUT), usp(), hulp()])
# ---------- Flow 2: product bekeken / winkelwagen ----------
NAAM="{{ event.Name|default:'het Bline leeskussen' }}"
URL="{% if event.URL %}{{ event.URL }}{% else %}{{ organization.url }}{% endif %}"
IMG="{{ event.ImageURL|default:'"+beeld('beige')+"' }}"
T['B1W']=('Bline | Winkelwagen 1','Je winkelwagen staat nog klaar','Je hoeft alleen nog af te rekenen.',[
 kop(f'Nog iets in je {schuin("winkelwagen")}'),
 tekst(HALLO+f'<br/>je legde {NAAM} in je winkelwagen. Hij staat nog voor je klaar.'),
 foto(IMG,URL,NAAM), knop('Naar mijn winkelwagen',U+'/cart'), usp(), hulp()])
T['B1B']=('Bline | Product bekeken 1','Even teruggekomen?','Leunen zonder kussenstapel.',[
 kop(f'Lezen in bed, maar dan {schuin("comfortabel")}'),
 tekst(HALLO+f'<br/>je keek naar {NAAM}. Een stapel kussens zakt weg zodra je gaat zitten. Bline blijft staan.'),
 foto(IMG,URL,NAAM),
 tekst(f'<strong style="color:{INKT};">3,8 kg traagschuim</strong> dat stevig blijft · <strong style="color:{INKT};">vak voor je telefoon</strong> · <strong style="color:{INKT};">hoes die in de was kan</strong>','18px 44px 0 44px',15),
 knop('Bekijk het leeskussen',URL), usp(), hulp()])
T['B2']=('Bline | Bekeken of winkelwagen 2','Welke kleur past bij jouw bed?','Vijf kleuren, één stevig kussen.',[
 kop(f'Welke kleur past bij {schuin("jouw")} bed?'),
 tekst(HALLO+'<br/>zelfde kussen, vijf kleuren. Lezen, werken, gamen of een serie kijken: met Bline zit je rechtop in bed zonder kussens te stapelen.'),
 kleurrij(), knop('Kies je kleur',U+'/#kleuren'),
 tekst('Kopers op bol.com geven hem een 4,5 uit 5. Nu ook rechtstreeks bij ons, voor dezelfde prijs.',size=14), usp(), hulp()])
# ---------- Flow 3: welkom ----------
T['W1']=('Bline | Welkom 1 (10%)','Welkom bij Bline: 10% op je eerste bestelling','Je persoonlijke code staat erin.',[
 kop(f'Welkom bij {schuin("Bline")}'),
 tekst(HALLO+'<br/>leuk dat je erbij bent. Als welkom krijg je 10% korting op je eerste bestelling.'),
 code_blok('BLINE_WELKOM10'), foto(beeld('beige'),U+'/#kleuren'),
 tekst('Bline is het leeskussen dat blijft staan. Stevig traagschuim, een vak voor je telefoon en een hoes die zo in de was kan.'),
 knop('Kies je kleur',U+'/#kleuren'), usp()])
T['W2']=('Bline | Welkom 2','Zo zit je rechtop in bed zonder kussenstapel','Waarom Bline blijft staan.',[
 kop(f'Stevig van {schuin("binnen")}, zacht van buiten'),
 tekst(HALLO+'<br/>waarom zakt een gewone stapel kussens weg en Bline niet? Het zit in wat erin zit.'),
 foto(CDN+'bline-leeskussen-beige-04.jpg?width=600',U+'/products/leeskussen-beige','Bline leeskussen met de rits open en de vulling zichtbaar'),
 tekst(f'<strong style="color:{INKT};">3,8 kg traagschuim.</strong> Leun er gerust tegenaan, hij blijft staan.<br/><br/><strong style="color:{INKT};">Vak voor je telefoon.</strong> Opzij, zodat hij niet tussen de lakens verdwijnt.<br/><br/><strong style="color:{INKT};">Hoes van katoen 400 TC.</strong> Rits hem eraf en was hem op 30 °C.<br/><br/><strong style="color:{INKT};">65 x 50 x 45 cm.</strong> Twee passen naast elkaar op een bed vanaf 140 cm.','18px 44px 0 44px',15,'left'),
 knop('Bekijk het leeskussen',U+'/products/leeskussen-beige'),
 tekst('Je welkomstkorting van 10% staat in onze eerste mail.',size=14)])
T['W3']=('Bline | Welkom 3 (10%)','Je 10% staat nog klaar','Gratis verzending en 30 dagen proberen.',[
 kop(f'Je 10% staat nog {schuin("klaar")}'),
 tekst(HALLO+'<br/>nog geen leeskussen uitgekozen? Hier is je persoonlijke code nog een keer.'),
 code_blok('BLINE_WELKOM10'), kleurrij(), knop('Kies je kleur',U+'/#kleuren'), usp(), hulp()])
def bouw(sleutel):
    naam,onderwerp,preview,rijen=T[sleutel]
    return naam,onderwerp,preview,omhulsel(onderwerp,preview,rijen)
