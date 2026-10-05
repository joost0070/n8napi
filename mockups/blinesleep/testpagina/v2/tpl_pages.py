from tpl import *
def kop(d,m,eyebrow,heading,intro):
    return {'type':'bline-paginakop','settings':{'image_desktop':SI(d),'image_mobile':SI(m) if m else '','eyebrow':eyebrow,'heading':heading,'intro':intro,'color_scheme':'scheme-1'}}
def bt(img,eyebrow,heading,text,points='',right=False,scheme='scheme-1',btn='',link='',video=''):
    return {'type':'bline-beeld-tekst','settings':{'video_product':video,'image':SI(img) if img else '','image_right':right,'eyebrow':eyebrow,'heading':heading,'text':text,'points':points,'button_label':btn,'button_link':link,'color_scheme':scheme}}
def tg(eyebrow,heading,tiles,cols='3',ratio='vierkant',scheme='scheme-1',intro='',ll='',l=''):
    return {'type':'bline-tegels','settings':{'eyebrow':eyebrow,'heading':heading,'intro':intro,'link_label':ll,'link':l,'columns':cols,'ratio':ratio,'mobile_slider':True,'color_scheme':scheme},**blocks(tiles,'tegel')}
def lb(eyebrow,heading,intro,items,cols='3',ll='',l=''):
    return {'type':'bline-lookbook','settings':{'eyebrow':eyebrow,'heading':heading,'intro':intro,'link_label':ll,'link':l,'columns':cols,'color_scheme':'scheme-1'},**blocks([{'image':SI(i),'product':p,'label':'','groot':g} for i,p,g in items],'foto')}
VT={'type':'bline-vertrouwen','settings':{'color_scheme':'scheme-1'}}
# Materialen
S={'kop':kop('bline-banner-kussen-16x9.jpg','bline-detail-stof-01.jpg','Materialen','Waar het kussen van gemaakt is','<p>Een katoenen hoes, een vulling van traagschuim en een vak opzij. Hieronder per onderdeel wat het is en hoe je het verzorgt.</p>'),
 'hoes':bt('bline-detail-stof-01.jpg','De hoes','Katoen 400 TC','<p>De hoes is van 100% katoen met 400 draden per vierkante inch. Dicht geweven, glad en zacht.</p>','100% katoen, 400 TC\nBies langs de naden\nVolledig afneembaar met een onzichtbare rits\nIn vijf kleuren, ook los te koop'),
 'vulling':bt('bline-detail-vulling-wit.jpg','De vulling','3,8 kg traagschuim','<p>Binnenin zit 3,8 kg traagschuim. Daardoor blijft het kussen staan als je ertegenaan leunt.</p>','Stevig en vormvast\nHet hele kussen weegt 3,9 kg\nNet uitgepakt? Laat het 24 tot 48 uur luchten en schud het op',right=True,scheme='scheme-7'),
 'zijvak':bt('bline-detail-zijvak-03.jpg','Rits en zijvak','Alles binnen handbereik','<p>Aan de zijkant zit een vak voor je boek, bril of telefoon. De rits zit uit het zicht, het label aan de zijkant.</p>','Zijvak voor boek, bril of telefoon\nOnzichtbare rits\nBline-label aan de zijkant'),
 'wassen':tg('Verzorging','Zo was je de hoes',[tegel('','Op 30 °C','<p>Machinewas, normaal programma. Haal de hoes er met de rits af.</p>'),tegel('','Niet bleken','<p>Gebruik een gewoon wasmiddel zonder bleekmiddel.</p>'),tegel('','Niet in de droger','<p>Laat de hoes aan de lucht drogen. Een extra hoes is handig om te wisselen.</p>','shopify://collections/hoezen','Losse hoezen')],scheme='scheme-7'),
 'slider':fc('leeskussens','Het leeskussen in vijf kleuren','',n=5,cols=5),
 'vt':VT}
write('page.materialen.json',S,['kop','hoes','vulling','zijvak','wassen','slider','vt'])
# Lezen in bed
S={'kop':kop('bline-banner-lezen-21x9.jpg','bline-banner-lezen-4x5.jpg','Inspiratie','Lezen in bed','<p>Met een boek, een serie of je laptop. Tik op een foto voor het kussen in die kleur.</p>'),
 'in_bed':lb('In bed','Rechtop met een boek','',[('bline-leeskussen-wit-gebruik-03.jpg','leeskussen-wit',True),('bline-leeskussen-blauw-03.jpg','leeskussen-blauw',False),('bline-leeskussen-beige-03.jpg','leeskussen-beige',False),('bline-leeskussen-grijs-05.jpg','leeskussen-grijs',False),('bline-leeskussen-zwart-03.jpg','leeskussen-zwart',False),('bline-leeskussen-wit-02.jpg','leeskussen-wit',False),('bline-leeskussen-blauw-05.jpg','leeskussen-blauw',False),('bline-leeskussen-grijs-02.jpg','leeskussen-grijs',False),('bline-leeskussen-beige-02.jpg','leeskussen-beige',False)]),
 'video':bt('','Zo gebruik je het','Leunen, lezen, wegleggen','<p>Zet het kussen tegen het hoofdbord, leun achterover en leg je telefoon in het vak opzij.</p>','Blijft staan door 3,8 kg traagschuim\nHoes eraf met één rits\nIn vijf kleuren',scheme='scheme-7',btn='Shop leeskussens',link='shopify://collections/leeskussens',video='leeskussen-wit'),
 'werken':lb('Werken, kijken, op de bank','Ook om te werken en te kijken','',[('bline-leeskussen-wit-04.jpg','leeskussen-wit',False),('bline-leeskussen-grijs-03.jpg','leeskussen-grijs',False),('bline-leeskussen-zwart-05.jpg','leeskussen-zwart',False),('bline-leeskussen-zwart-02.jpg','leeskussen-zwart',False),('bline-leeskussen-wit-03.jpg','leeskussen-wit',False),('bline-leeskussen-blauw-06.jpg','leeskussen-blauw',False)]),
 'slider':fc('bestsellers','Shop de looks','',n=8,cols=4),'vt':VT}
write('page.lezen-in-bed.json',S,['kop','in_bed','video','werken','slider','vt'])
# Kleurengids
K=[('wit','Wit','Licht en fris. Past bij wit, lichtgrijs en zachtgroen beddengoed.'),('beige','Beige','Warm en rustig. Mooi bij wit, zand, oudroze en linnen in naturel.'),('blauw','Blauw','Een rustig leiblauw. Mooi bij wit, lichtblauw en grijs, met een warm accent.'),('grijs','Grijs','Neutraal en zacht. Past bij wit, antraciet, roze en mosgroen.'),('zwart','Zwart','Strak en donker. Mooi bij wit, grijs en een streep of ruit.')]
S={'kop':kop('bline-kleuren-strip-01.jpg','bline-tegel-beige-sfeer.jpg','Kleurengids','Welke kleur past bij jouw bed?','<p>Vijf kleuren naast elkaar, met het beddengoed waar ze goed bij staan. Twijfel je? Je hebt 14 dagen bedenktijd.</p>'),
 'kleuren':tg('Vijf kleuren','Naast elkaar',[tegel(f'bline-tegel-{k}-sfeer.jpg',n,f'<p>{t}</p>',f'shopify://products/leeskussen-{k}',f'Shop {n.lower()}') for k,n,t in K],cols='5',ratio='staand'),
 'hoezen':bt('bline-leeskussen-wit-gebruik-04.png','Wisselen','Liever afwisselen?','<p>Neem een tweede hoes in een andere kleur. Met een leeskussen krijg je €9,99 korting op de extra hoes.</p>','',right=True,scheme='scheme-7',btn='Bekijk de hoezen',link='shopify://collections/hoezen-en-sets'),
 'slider':fc('leeskussens','Kies je kleur','',n=5,cols=5),'vt':VT}
write('page.kleurengids.json',S,['kop','kleuren','hoezen','slider','vt'])
# Maatgids
S={'kop':kop('bline-banner-kussen-16x9.jpg','bline-banner-kussen-4x5.jpg','Maatgids','Past het op jouw bed?','<p>Het leeskussen is 65 cm breed, 50 cm hoog en 45 cm diep. Hieronder zie je hoeveel ruimte er overblijft op een bed van 140, 160 en 180 cm.</p>'),
 'maten':bt('bline-leeskussen-maattekening.jpg','De maten','65 x 50 x 45 cm','<p>Breed genoeg om tegenaan te leunen, smal genoeg om naast een kussen te liggen.</p>','Breedte 65 cm\nHoogte 50 cm\nDiepte 45 cm\nGewicht 3,9 kg'),
 'bedden':bt('bline-maatgids-bedden-01.jpg','Op je bed','Zo veel ruimte blijft er over','<p>Op een bed van 140 cm blijft links en rechts 37,5 cm over. Twee leeskussens naast elkaar zijn samen 130 cm breed: dat past op een bed vanaf 140 cm.</p>','140 cm: links en rechts 37,5 cm\n160 cm: links en rechts 47,5 cm\n180 cm: links en rechts 57,5 cm',right=True,scheme='scheme-7',btn='Twee leeskussens',link='shopify://collections/sets-en-bundels'),
 'tips':tg('Tips','Even meten',[tegel('','Hoofdbord','<p>Het kussen staat tegen het hoofdbord of de muur. Zonder hoofdbord werkt het ook.</p>'),tegel('','Diepte','<p>Reken op 45 cm van het hoofdbord naar voren: zo ver schuif je op in bed.</p>'),tegel('','Twijfel?','<p>Je hebt 14 dagen bedenktijd. Bel of app ons gerust: 06 38 66 28 33.</p>','shopify://pages/contact','Contact')]),
 'slider':fc('leeskussens','Het leeskussen in vijf kleuren','',n=5,cols=5),'vt':VT}
write('page.maatgids.json',S,['kop','maten','bedden','tips','slider','vt'])
# Bline Sleep
S={'kop':kop('bline-banner-kussen-16x9.jpg','bline-banner-kussen-4x5.jpg','Binnenkort','Bline Sleep','<p>Na het leeskussen werken we aan meer voor in bed. We laten het pas zien als het goed genoeg is.</p>'),
 'wat':tg('Wat er komt','Voor in bed',[tegel('','Zijden kussensloop','<p>Een sloop van zijde voor je hoofdkussen.</p>'),tegel('','Beddengoed van lyocell','<p>Lyocell wordt gemaakt van houtvezel.</p>'),tegel('','Dekbed','<p>Een dekbed dat past bij de rest van Bline.</p>')],scheme='scheme-7'),
 'aanmelden':{'type':'newsletter','settings':{'color_scheme':'scheme-1','full_width':False,'padding_top':56,'padding_bottom':56},'blocks':{'kop':{'type':'heading','settings':{'heading':'Als eerste weten wanneer Bline Sleep er is','heading_size':'h2'}},'tekst':{'type':'paragraph','settings':{'text':'<p>Laat je e-mailadres achter. We mailen alleen als er iets nieuws is.</p>'}},'formulier':{'type':'email_form','settings':{}}},'block_order':['kop','tekst','formulier']},
 'slider':fc('leeskussens','Nu al te koop: het leeskussen','',n=5,cols=5),'vt':VT}
write('page.bline-sleep.json',S,['kop','wat','aanmelden','slider','vt'])
print('ok')
