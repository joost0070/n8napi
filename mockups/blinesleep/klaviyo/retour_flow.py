"""Bline: bevestigingsmail bij een retouraanmelding (online ontbindingsfunctie op /pages/ontbinden).

Het thema stuurt bij "Bevestig mijn retour" een Klaviyo-event "Ontbinding gemeld" met naam, bestelnummer,
producten en ontvangen_op. Deze flow mailt de klant direct een ontvangstbevestiging met die gegevens
(wettelijk verplicht: bevestiging op een duurzame drager met inhoud, datum en tijd).
Gebruik: python3 retour_flow.py  (maakt template, metric en flow aan, zet de flow live en bewaart de id's).
"""
import json, time, requests, os
from kv import k
import mails as m

A = 'KLAVIYO_BlineSleep'
INFO = f'border-collapse:separate;background-color:{m.ZAND};border-radius:14px;'


def regel(label, waarde):
    return (f'<tr><td style="padding:6px 18px;font-family:{m.F};font-size:14px;line-height:20px;color:{m.SUB};width:130px;" valign="top">{label}</td>'
            f'<td style="padding:6px 18px;font-family:{m.F};font-size:14px;line-height:20px;color:{m.INKT};font-weight:600;">{waarde}</td></tr>')


def html():
    gegevens = (f'<tr><td align="center" class="zij" style="padding:22px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="{INFO}">'
                '<tr><td colspan="2" style="height:10px;"></td></tr>'
                + regel('Bestelnummer', '{{ event.bestelnummer }}')
                + regel('Producten', '{{ event.producten }}')
                + regel('Ontvangen op', '{{ event.ontvangen_op }}')
                + '<tr><td colspan="2" style="height:10px;"></td></tr></table></td></tr>')
    rijen = [
        m.kop('Je retour is ' + m.schuin('aangemeld')),
        m.tekst("Hoi {{ event.naam|default:'' }},<br/>we hebben je retour goed ontvangen. Daarmee is de koop van de producten hieronder ongedaan gemaakt. Bewaar deze mail als bevestiging."),
        gegevens,
        m.tekst('<strong style="color:%s;">Hoe nu verder?</strong><br/>Binnen een werkdag krijg je van ons een gratis retourlabel van PostNL. Stuur je een losse hoes terug, dan krijg je het retouradres. Stuur het binnen 14 dagen terug, compleet en schoon, het liefst in de originele doos.' % m.INKT, align='left'),
        m.tekst('Zodra het pakket binnen is, of je laat zien dat je het hebt verstuurd, krijg je het aankoopbedrag binnen 14 dagen terug. Op dezelfde manier als je betaalde.', align='left'),
        m.hulp(),
    ]
    return m.omhulsel('Je retour is aangemeld', 'Je krijgt binnen een werkdag je gratis retourlabel van PostNL.', rijen,
                      voet='Je krijgt deze mail omdat je een retour hebt aangemeld bij Bline.')


if __name__ == '__main__':
    sc, t = k(A, 'POST', 'templates/', {'data': {'type': 'template', 'attributes': {'name': 'Bline | Retour aangemeld (bevestiging)', 'editor_type': 'CODE', 'html': html()}}})
    print('template', sc); tid = t['data']['id']
    # metric aanmaken met een testevent op een testprofiel (wordt daarna onderdrukt)
    ev = {'data': {'type': 'event', 'attributes': {
        'properties': {'naam': 'Test', 'bestelnummer': '#TEST', 'producten': 'De hele bestelling', 'ontvangen_op': 'test'},
        'metric': {'data': {'type': 'metric', 'attributes': {'name': 'Ontbinding gemeld'}}},
        'profile': {'data': {'type': 'profile', 'attributes': {'email': 'retour-test@example.com'}}}}}}
    print('event', k(A, 'POST', 'events/', ev)[0])
    mid = None
    for _ in range(20):
        sc, j = k(A, 'GET', 'metrics/', params={'filter': 'equals(name,"Ontbinding gemeld")'})
        if j.get('data'): mid = j['data'][0]['id']; break
        time.sleep(3)
    print('metric', mid)
    flow = {'data': {'type': 'flow', 'attributes': {'name': 'Bline | Retour aangemeld: bevestiging (direct)', 'definition': {
        'triggers': [{'type': 'metric', 'id': mid, 'trigger_filter': None}],
        'profile_filter': None,
        'actions': [{'temporary_id': 'r1', 'type': 'send-email', 'data': {'message': {
            'from_email': 'mail@blinesleep.nl', 'from_label': 'Bline', 'reply_to_email': 'mail@blinesleep.nl', 'cc_email': None, 'bcc_email': 'mail@blinesleep.nl',
            'subject_line': 'Je retour is aangemeld', 'preview_text': 'Je krijgt binnen een werkdag je gratis retourlabel van PostNL.',
            'template_id': tid, 'smart_sending_enabled': False, 'transactional': False, 'add_tracking_params': False, 'custom_tracking_params': None,
            'additional_filters': None, 'name': 'Retour aangemeld: bevestiging'}, 'status': 'live'}, 'links': {'next': None}}],
        'entry_action_id': 'r1'}}}}
    sc, f = k(A, 'POST', 'flows/', flow)
    print('flow', sc, json.dumps(f)[:300])
    fid = f['data']['id']
    print('live', k(A, 'PATCH', f'flows/{fid}/', {'data': {'type': 'flow', 'id': fid, 'attributes': {'status': 'live'}}})[0])
    # testprofiel onderdrukken
    print('onderdruk', k(A, 'POST', 'profile-suppression-bulk-create-jobs/', {'data': {'type': 'profile-suppression-bulk-create-job', 'attributes': {'profiles': {'data': [{'type': 'profile', 'attributes': {'email': 'retour-test@example.com'}}]}}}})[0])
    ids = json.load(open('flow_ids.json')); ids['retour'] = fid; json.dump(ids, open('flow_ids.json', 'w'), indent=1)
    tids = json.load(open('template_ids.json')); tids['RETOUR'] = tid; json.dump(tids, open('template_ids.json', 'w'), indent=1)
    print('klaar', fid, tid, mid)
