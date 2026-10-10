from tpl import *
old=json.loads(open('theme/templates/index.json').read()[len(HDR):])
S={}
S['hero']={'type':'bline-hero','settings':{'image_desktop':SI('bline-banner-lezen-4x3.jpg'),'image_mobile':SI('bline-banner-lezen-4x5.jpg'),'eyebrow':'Leeskussen met vak voor je boek','heading':'Rechtop lezen in bed','text':'Een stevig kussen dat blijft staan, met een vak opzij voor je telefoon of bril.','label_1':'Shop leeskussens','link_1':'shopify://collections/leeskussens','label_2':'Bekijk de kleuren','link_2':'shopify://pages/kleurengids','score':'4,5 uit 5 op bol.com','color_scheme':'scheme-7'}}
S['vertrouwen']={'type':'bline-vertrouwen','settings':{'color_scheme':'scheme-1'}}
kt=[{'product':f'leeskussen-{k}','image':SI(f'bline-tegel-{k}-sfeer.jpg'),'image_hover':SI(f'bline-tegel-{k}-packshot.jpg')} for k in ['beige','wit','grijs','blauw','zwart']]
S['kleuren']={'type':'bline-kleurtegels','settings':{'eyebrow':'Vijf kleuren','heading':'Kies je kleur','link_label':'Hulp bij kiezen','link':'shopify://pages/kleurengids','color_scheme':'scheme-1'},**blocks(kt,'kleur')}
S['blijft_staan']={'type':'bline-beeld-tekst','settings':{'video_product':'leeskussen-wit','image':SI('bline-banner-werken-4x5.jpg'),'image_right':False,'eyebrow':'Het leeskussen','heading':'Het kussen dat blijft staan','text':'<p>Losse kussens zakken weg. Dit kussen houdt zijn vorm, ook als je er een uur tegenaan leunt.</p>','points':'3,8 kg traagschuim, stevig en vormvast\nVak opzij voor je telefoon, bril of boek\nKatoenen hoes met rits, wasbaar op 30 °C','button_label':'Shop leeskussens','button_link':'shopify://collections/leeskussens','color_scheme':'scheme-7'}}
S['details']={'type':'bline-tegels','settings':{'eyebrow':'Details','heading':'Gemaakt om in te lezen','intro':'','link_label':'','link':'','columns':'3','ratio':'vierkant','mobile_slider':True,'color_scheme':'scheme-1'},**blocks([
  tegel('bline-detail-zijvak-01.jpg','Vak opzij','<p>Je telefoon, bril of boek binnen handbereik. Het vak zit aan de zijkant, uit de weg.</p>'),
  tegel('bline-detail-stof-01.jpg','Hoes met rits','<p>Katoen 400 TC met een bies langs de naden. De rits zit uit het zicht, de hoes gaat zo in de was.</p>'),
  tegel('bline-detail-label-01.jpg','Afgewerkt tot het label','<p>Stevige naden en het Bline-label aan de zijkant. Zo herken je het kussen.</p>','shopify://pages/materialen','Over de materialen')],'tegel')}
S['vergelijk']={'type':'bline-vergelijk','settings':{'eyebrow':'Vergelijk','heading':'Losse kussens of een leeskussen','col_a':'Losse kussens','col_b':'Leeskussen Bline','button_label':'Lees de hele vergelijking','button_link':'shopify://pages/leeskussen-of-losse-kussens','color_scheme':'scheme-1'},**blocks([
  {'label':'Steun','a':'Zakken weg, steeds opschudden','b':'Blijft staan door 3,8 kg traagschuim'},
  {'label':'Spullen','a':'Telefoon en bril liggen los op bed','b':'Vak opzij voor telefoon, bril of boek'},
  {'label':'Ruimte','a':'Drie of vier kussens in bed','b':'Eén kussen van 65 cm breed'},
  {'label':'Wassen','a':'Elke sloop apart','b':'Eén hoes met rits, wasbaar op 30 °C'}],'regel')}
S['sets']=fc('sets-en-bundels','Sets met €9,99 korting','<p>Een leeskussen met een extra hoes, of twee leeskussens. De korting gaat er in de winkelwagen automatisch af.</p>',n=8,cols=4)
S['reviews']={'type':'bline-reviewband','settings':{'heading':'Zo beoordelen kopers het kussen','score':'4,5','bron':'op basis van 13 reviews op bol.com','n5':9,'n4':3,'n3':0,'n2':1,'n1':0,'text':'Het leeskussen is ook te koop bij bol.com. Daar komen deze reviews vandaan.','color_scheme':'scheme-7'}}
lb=[('bline-leeskussen-wit-gebruik-03.jpg','leeskussen-wit',True),('bline-leeskussen-blauw-03.jpg','leeskussen-blauw',False),('bline-leeskussen-grijs-05.jpg','leeskussen-grijs',False),('bline-leeskussen-zwart-02.jpg','leeskussen-zwart',False),('bline-leeskussen-beige-03.jpg','leeskussen-beige',False),('bline-leeskussen-wit-02.jpg','leeskussen-wit',False)]
S['lookbook']={'type':'bline-lookbook','settings':{'eyebrow':'Inspiratie','heading':'Lezen in bed','intro':'Met een boek, een serie of je laptop. Tik op een foto voor het kussen in die kleur.','link_label':'Meer inspiratie','link':'shopify://pages/lezen-in-bed','columns':'3','color_scheme':'scheme-1'},**blocks([{'image':SI(i),'product':p,'label':'','groot':g} for i,p,g in lb],'foto')}
S['materialen']={'type':'bline-tegels','settings':{'eyebrow':'Materialen','heading':'Waar het kussen van gemaakt is','intro':'','link_label':'Alles over de materialen','link':'shopify://pages/materialen','columns':'3','ratio':'staand','mobile_slider':True,'color_scheme':'scheme-7'},**blocks([
  tegel('bline-hoes-beige-packshot-01.png','Katoen 400 TC','<p>Een dichte, zachte katoenen hoes in vijf kleuren.</p>','shopify://pages/materialen'),
  tegel('bline-detail-vulling-wit.jpg','3,8 kg traagschuim','<p>Geeft steun en houdt zijn vorm, ook na lang leunen.</p>','shopify://pages/materialen'),
  tegel('bline-leeskussen-blauw-04.jpg','Onzichtbare rits','<p>De hoes gaat er in één keer af en kan op 30 °C in de was.</p>','shopify://pages/materialen')],'tegel')}
S['over']={'type':'bline-beeld-tekst','settings':{'video_product':'','image':SI('bline-banner-kussen-4x5.jpg'),'image_right':True,'eyebrow':'Over Bline','heading':'Een klein merk uit Borne','text':'<p>Bline is een Nederlands merk voor lezen en slapen in bed. Het leeskussen verkopen we ook via bol.com, waar het 4,5 uit 5 sterren heeft.</p>','points':'','button_label':'Over Bline','button_link':'shopify://pages/over-bline','color_scheme':'scheme-1'}}
S['verhalen']={'type':'featured-blog','settings':{'blog':'blog','post_limit':3,'heading':'Verhalen','heading_size':'h2','columns_desktop':3,'show_view_all':True,'show_image':True,'show_date':False,'show_author':False,'color_scheme':'scheme-1','padding_top':56,'padding_bottom':40}}
v=old['sections']['vragen']; v['block_order']=[b for b in v['block_order'] if b!='vraag_5']; v['blocks'].pop('vraag_5',None)
v['settings']['padding_top']=40; v['settings']['padding_bottom']=64
S['vragen']=v
order=['hero','vertrouwen','kleuren','blijft_staan','details','vergelijk','sets','reviews','lookbook','materialen','over','verhalen','vragen']
write('index.json',S,order)
print('ok')
