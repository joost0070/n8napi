from tpl import *
raw=open('theme/templates/collection.json').read(); d=json.loads(raw[len(HDR):])
d['sections']['banner']['settings'].update({'show_collection_image':True,'color_scheme':'scheme-7'})
g=d['sections']['product-grid']['settings']; g.update({'columns_desktop':4,'show_secondary_image':True,'products_per_page':24,'padding_top':40,'padding_bottom':56})
d['sections']['vertrouwen']={'type':'bline-vertrouwen','settings':{'color_scheme':'scheme-1'}}
d['sections']['ingangen']={'type':'bline-tegels','settings':{'eyebrow':'Shop op moment','heading':'Waar lees jij?','intro':'','link_label':'','link':'','columns':'4','ratio':'staand','mobile_slider':True,'color_scheme':'scheme-7'},**blocks([
  tegel('bline-banner-lezen-4x5.jpg','Lezen in bed','','shopify://collections/lezen-in-bed','Bekijk'),
  tegel('bline-sfeer-bank-zwart-4x5.jpg','Ontspannen op de bank','','shopify://collections/ontspannen-op-de-bank','Bekijk'),
  tegel('bline-banner-werken-4x5.jpg','Werken in bed','','shopify://collections/sets-en-bundels','Bekijk de sets'),
  tegel('bline-cadeaubon-01.jpg' if False else 'bline-banner-kussen-4x5.jpg','Cadeau','','shopify://collections/cadeau','Bekijk')],'tegel')}
d['sections']['lookbook_link']={'type':'bline-beeld-tekst','settings':{'video_product':'','image':SI('bline-detail-zijvak-01.jpg'),'image_right':False,'eyebrow':'Materialen','heading':'Katoen, traagschuim en een vak opzij','text':'<p>Hoe de hoes, de vulling en het zijvak gemaakt zijn, met foto\'s van dichtbij.</p>','points':'','button_label':'Bekijk de materialen','button_link':'shopify://pages/materialen','color_scheme':'scheme-1'}}
d['order']=['banner','vertrouwen','product-grid','ingangen','lookbook_link']
open('theme/templates/collection.json','w').write(HDR+json.dumps(d,indent=2,ensure_ascii=False))
v=json.loads(json.dumps(d)); v['sections']['product-grid']['settings']['columns_desktop']=5
open('theme/templates/collection.vijf.json','w').write(HDR+json.dumps(v,indent=2,ensure_ascii=False))
print('ok')
