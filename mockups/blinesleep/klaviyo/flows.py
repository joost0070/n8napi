from kv import *
import mails
A='KLAVIYO_BlineSleep'
ids=json.load(open('template_ids.json'))
PLACED,CHECKOUT,CART,VIEW,LIJST='StA4jb','TCYTd3','VrqLHw','UNpJ6T','SAeiP6'
def geen(metric,tijd='flow-start'):
    return {'type':'profile-metric','metric_id':metric,'measurement':'count','measurement_filter':{'type':'numeric','operator':'equals','value':0},'timeframe_filter':{'type':'date','operator':tijd},'metric_filters':None}
def wel(metric):
    return {'type':'profile-metric','metric_id':metric,'measurement':'count','measurement_filter':{'type':'numeric','operator':'greater-than','value':0},'timeframe_filter':{'type':'date','operator':'flow-start'},'metric_filters':None}
def wacht(i,waarde,eenheid,nxt): return {'temporary_id':i,'type':'time-delay','data':{'unit':eenheid,'value':waarde,'secondary_value':0,'timezone':'profile'},'links':{'next':nxt}}
def mail(i,key,naam,nxt,smart=False):
    n,onderwerp,preview,_=mails.bouw(key)
    return {'temporary_id':i,'type':'send-email','data':{'message':{'from_email':'mail@blinesleep.nl','from_label':'Bline','reply_to_email':'mail@blinesleep.nl','cc_email':None,'bcc_email':None,
        'subject_line':onderwerp,'preview_text':preview,'template_id':ids[key],'smart_sending_enabled':smart,'transactional':False,'add_tracking_params':True,
        'custom_tracking_params':[{'param':'utm_source','value':'klaviyo'},{'param':'utm_medium','value':'email'},{'param':'utm_campaign','value':'{message_name}'},{'param':'utm_id','value':'{flow_id}'}],
        'additional_filters':None,'name':naam},'status':'live'},'links':{'next':nxt}}
def split(i,cond,ja,nee): return {'temporary_id':i,'type':'conditional-split','data':{'profile_filter':{'condition_groups':[{'conditions':[cond]}]}},'links':{'next_if_true':ja,'next_if_false':nee}}
F={}
F['checkout']=('Bline | Verlaten checkout (3 mails, mail 3 met 10%)',{
 'triggers':[{'type':'metric','id':CHECKOUT,'trigger_filter':None}],
 'profile_filter':{'condition_groups':[{'conditions':[geen(PLACED)]}]},
 'actions':[wacht('a1',1,'hours','a2'),mail('a2','C1','Checkout 1: staat nog klaar (1 uur)','a3'),
            wacht('a3',23,'hours','a4'),mail('a4','C2','Checkout 2: vragen (24 uur)','a5'),
            wacht('a5',2,'days','a6'),mail('a6','C3','Checkout 3: 10% code (3 dagen)',None)],
 'entry_action_id':'a1'})
F['bekeken']=('Bline | Product bekeken en winkelwagen (2 mails)',{
 'triggers':[{'type':'metric','id':VIEW,'trigger_filter':None}],
 'profile_filter':{'condition_groups':[{'conditions':[geen(PLACED)]},{'conditions':[geen(CHECKOUT)]}]},
 'actions':[wacht('b1',2,'hours','b2'),split('b2',wel(CART),'b3','b6'),
            mail('b3','B1W','Winkelwagen 1 (2 uur)','b4',True),wacht('b4',2,'days','b5'),mail('b5','B2','Winkelwagen 2: kleuren (2 dagen)',None,True),
            mail('b6','B1B','Bekeken 1 (2 uur)','b7',True),wacht('b7',2,'days','b8'),mail('b8','B2','Bekeken 2: kleuren (2 dagen)',None,True)],
 'entry_action_id':'b1'})
F['welkom']=('Bline | Welkom met 10% (3 mails)',{
 'triggers':[{'type':'list','id':LIJST}],
 'profile_filter':{'condition_groups':[{'conditions':[geen(PLACED,'alltime')]}]},
 'actions':[mail('w1','W1','Welkom 1: 10% code (direct)','w2'),wacht('w2',2,'days','w3'),mail('w3','W2','Welkom 2: stevig van binnen (2 dagen)','w4'),
            wacht('w4',3,'days','w5'),mail('w5','W3','Welkom 3: 10% nog klaar (5 dagen)',None)],
 'entry_action_id':'w1'})
