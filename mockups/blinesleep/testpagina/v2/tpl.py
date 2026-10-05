import json
HDR=open('theme/templates/index.json').read(); HDR=HDR[:HDR.index('{')]
SI=lambda n:'shopify://shop_images/'+n
def write(name,sections,order):
    open('theme/templates/'+name,'w').write(HDR+json.dumps({'sections':sections,'order':order},indent=2,ensure_ascii=False))
def blocks(lst,typ):
    b={};o=[]
    for i,x in enumerate(lst,1):
        k=f'{typ}_{i}'; b[k]={'type':typ,'settings':x}; o.append(k)
    return {'blocks':b,'block_order':o}
def fc(coll,title,desc='',n=8,cols=4,scheme='scheme-1',pt=56,pb=56,view_all=True):
    return {'type':'featured-collection','settings':{'products_to_show':n,'heading_size':'h2','show_description':bool(desc),'description_style':'body','columns_desktop':cols,'enable_desktop_slider':True,'full_width':False,'show_view_all':view_all,'view_all_style':'link','color_scheme':scheme,'image_ratio':'square','image_shape':'default','show_secondary_image':True,'show_vendor':False,'show_rating':False,'quick_add':'none','columns_mobile':'2','swipe_on_mobile':True,'collection':coll,'title':title,'description':desc,'padding_top':pt,'padding_bottom':pb}}
def tegel(img,title,text,link='',label=''):
    return {'image':SI(img) if img else '','title':title,'text':text,'link':link,'link_label':label}
