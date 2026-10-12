"""Maakt de Meta-advertenties uit ../upload_meta.json aan, allemaal op PAUSED in de klaarstaande advertentieset.

Gebruik: python3 maak_ads.py [naam|alle] [opt-out-lijst]. Token uit de omgeving (zie m.py), nooit in deze map.
ids.json houdt bij wat al bestaat, dus opnieuw draaien maakt geen dubbele advertenties.
"""
import json, os, sys
from m import *
B=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/'
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D=json.load(open(B+'upload_meta.json')); H=json.load(open('hashes.json')); st=json.load(open('ids.json'))
st.setdefault('ads',{})
UTM='utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}'
# Geen AI-bewerkingen van beeld of tekst door Meta: alleen echte, goedgekeurde beelden en eigen teksten.
UIT = sys.argv[2] if len(sys.argv) > 2 else ('image_touchups,image_uncrop,image_templates,image_brightness_and_contrast,'
       'image_background_gen,image_animation,text_optimizations,text_generation,description_automation,'
       'inline_comment,enhance_cta,product_extensions,site_extensions')
DOF={'creative_features_spec':{k:{'enroll_status':'OPT_OUT'} for k in UIT.split(',') if k}} if UIT else None
def lijst(x): return x if isinstance(x,list) else [x]
plan=[]
for a in D['advertenties']:
    b45=lijst(a['beeld_4x5']); b916=lijst(a['beeld_9x16'])
    for n,(p45,p916) in enumerate(zip(b45,b916),1):
        naam=a['naam'] if len(b45)==1 else a['naam'].replace('_',f'_',1)+f'_v{n}'
        plan.append((naam,H[p45],H[p916],a['primaire_tekst'][0],a['kop'],a['link']))
alleen=sys.argv[1] if len(sys.argv)>1 else 'alle'
for naam,h45,h916,body,kop,link in plan:
    if alleen!='alle' and naam!=alleen: continue
    if naam in st['ads']: print('bestaat', naam); continue
    afs={'images':[{'hash':h45,'adlabels':[{'name':'f45'}]},{'hash':h916,'adlabels':[{'name':'f916'}]}],
         'bodies':[{'text':body,'adlabels':[{'name':'tekst'}]}],'titles':[{'text':kop,'adlabels':[{'name':'kop'}]}],
         'link_urls':[{'website_url':link,'adlabels':[{'name':'url'}]}],'call_to_action_types':['SHOP_NOW'],'ad_formats':['SINGLE_IMAGE'],
         'optimization_type':'PLACEMENT',
         'asset_customization_rules':[
           {'customization_spec':{'publisher_platforms':['facebook','instagram','messenger'],'facebook_positions':['story','facebook_reels'],'instagram_positions':['story','reels'],'messenger_positions':['story']},
            'image_label':{'name':'f916'},'body_label':{'name':'tekst'},'title_label':{'name':'kop'},'link_url_label':{'name':'url'},'priority':1},
           {'customization_spec':{'publisher_platforms':['facebook','instagram','messenger','audience_network']},
            'image_label':{'name':'f45'},'body_label':{'name':'tekst'},'title_label':{'name':'kop'},'link_url_label':{'name':'url'},'priority':2}]}
    cr={'name':naam,'object_story_spec':{'page_id':PAGE},'asset_feed_spec':afs,'url_tags':UTM}
    if DOF: cr['degrees_of_freedom_spec']=DOF
    r=post(A+'/adcreatives', cr)
    if 'id' not in r: print('FOUT creative', naam, json.dumps(r.get('error',r))[:600]); continue
    ad=post(A+'/ads', {'name':naam,'adset_id':st['adset'],'creative':{'creative_id':r['id']},'status':'PAUSED'})
    if 'id' not in ad: print('FOUT ad', naam, json.dumps(ad.get('error',ad))[:600]); continue
    st['ads'][naam]={'ad':ad['id'],'creative':r['id']}; json.dump(st,open('ids.json','w'),indent=1); print('ok', naam, ad['id'])
print(len(plan),'gepland;', len(st['ads']),'klaar')
