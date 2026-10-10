from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
import numpy as np, json, os
O='orig/'; B='bewerkt/'; LOG=[]
def op(n): return Image.open(O+n).convert('RGB')
def save(im,name,src,how,alt,q=86):
    im.save(B+name,'JPEG',quality=q,optimize=True,progressive=True)
    LOG.append(dict(nieuw=name,bron=src,bewerking=how,alt=alt,px=f'{im.width} x {im.height}'))
def crop_ratio(im,rw,rh,cx,cy,w=None):
    W,H=im.size
    if w is None:
        w=min(W,H*rw/rh)
    h=w*rh/rw
    x0=min(max(cx-w/2,0),W-w); y0=min(max(cy-h/2,0),H-h)
    return im.crop((int(x0),int(y0),int(x0+w),int(y0+h)))
def fit(im,w,h): return im.resize((w,h),Image.LANCZOS)
def sharpen(im,a=0.6): return im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=int(a*100),threshold=2))
LK='bline-leeskussen-'
# 1 hero desktop 21:9 (zuivere uitsnede) en 4:3 voor de gesplitste hero
src=op(LK+'wit-gebruik-02.jpg')
save(sharpen(fit(src.crop((0,350,6000,2921)),3200,1371),0.4),'bline-banner-lezen-21x9.jpg',LK+'wit-gebruik-02.jpg (echte foto)','uitsnede 21:9 over de volle breedte, 3200 x 1371, licht verscherpt','Vrouw leest een boek in bed tegen het leeskussen Bline, kleur Wit, met haar telefoon in het zijvak')
save(sharpen(fit(src.crop((667,0,6000,4000)),2400,1800),0.4),'bline-banner-lezen-4x3.jpg',LK+'wit-gebruik-02.jpg (echte foto)','uitsnede 4:3 met kussen, zijvak, gezicht en boek, 2400 x 1800, licht verscherpt','Vrouw leest een boek in bed tegen het leeskussen Bline, kleur Wit, met haar telefoon in het zijvak')
# 2 hero 16:9
save(sharpen(fit(crop_ratio(src,16,9,3000,1900),2400,1350),0.4),'bline-banner-lezen-16x9.jpg',LK+'wit-gebruik-02.jpg (echte foto)','uitsnede 16:9, verkleind naar 2400 x 1350, licht verscherpt','Vrouw leest een boek in bed tegen het leeskussen Bline, kleur Wit')
# 3 hero mobiel 4:5
save(sharpen(fit(src.crop((2250,0,5450,4000)),1600,2000),0.4),'bline-banner-lezen-4x5.jpg',LK+'wit-gebruik-02.jpg (echte foto)','uitsnede 4:5 rond gezicht, boek en kussen, 1600 x 2000, licht verscherpt','Vrouw leest een boek in bed tegen het leeskussen Bline, kleur Wit')
# 4 laptop banners
s1=op(LK+'wit-gebruik-01.jpg')
save(sharpen(fit(crop_ratio(s1,16,9,3000,2050),2400,1350),0.4),'bline-banner-werken-16x9.jpg',LK+'wit-gebruik-01.jpg (echte foto)','uitsnede 16:9, 2400 x 1350, licht verscherpt','Vrouw werkt op haar laptop in bed tegen het leeskussen Bline, kleur Wit')
save(sharpen(fit(s1.crop((1700,0,4900,4000)),1600,2000),0.4),'bline-banner-werken-4x5.jpg',LK+'wit-gebruik-01.jpg (echte foto)','uitsnede 4:5, 1600 x 2000','Vrouw werkt op haar laptop in bed tegen het leeskussen Bline, kleur Wit')
s3=op(LK+'wit-gebruik-03.jpg')
save(sharpen(fit(crop_ratio(s3,4,5,2400,2100),1600,2000),0.4),'bline-sfeer-wit-4x5.jpg',LK+'wit-gebruik-03.jpg (echte foto)','uitsnede 4:5, 1600 x 2000','Vrouw met laptop lacht in bed tegen het leeskussen Bline, kleur Wit, met haar telefoon in het zijvak')
pk=op(LK+'wit-packshot-01.jpg')
save(sharpen(fit(crop_ratio(pk,16,9,3300,2300,5800),2400,1350),0.4),'bline-banner-kussen-16x9.jpg',LK+'wit-packshot-01.jpg (echte foto)','uitsnede 16:9, 2400 x 1350','Leeskussen Bline, kleur Wit, op een bed met een open boek ervoor')
save(sharpen(fit(crop_ratio(pk,4,5,3550,2200,3200),1600,2000),0.4),'bline-banner-kussen-4x5.jpg',LK+'wit-packshot-01.jpg (echte foto)','uitsnede 4:5, 1600 x 2000','Leeskussen Bline, kleur Wit, op een bed met een open boek ervoor')
# 5 macro's
save(sharpen(fit(src.crop((700,1900,2500,3500)).crop((0,0,1800,1600)),1600,1422).crop((0,0,1600,1422)).resize((1600,1422)),0.5),'bline-detail-zijvak-01.jpg',LK+'wit-gebruik-02.jpg (echte foto)','uitsnede van het zijvak met telefoon en het label, 1600 x 1422, verscherpt','Zijvak van het leeskussen Bline, kleur Wit, met een telefoon erin en het Bline-label ernaast')
pass #(,LK+'wit-gebruik-02.jpg (echte foto)','vierkante uitsnede van het zijvak met telefoon en het label, 1600 x 1600, verscherpt','Zijvak van het leeskussen Bline, kleur Wit, met een telefoon erin en het Bline-label ernaast')
save(sharpen(fit(pk.crop((3100,1800,4700,3400)),1600,1600),0.5),'bline-detail-stof-01.jpg',LK+'wit-packshot-01.jpg (echte foto)','vierkante uitsnede van stof, bies en rits, 1600 x 1600, verscherpt','Katoenen hoes van het leeskussen Bline, kleur Wit, van dichtbij met de bies en het lipje van de rits')
lab=op(LK+'wit-07.jpg')
save(sharpen(lab,0.3),'bline-detail-label-01.jpg',LK+'wit-07.jpg (bol-foto)','licht verscherpt, verder gelijk','Bline-label op de hoes van het leeskussen, kleur Wit')
vf=Image.open('vf/t22.0.jpg').convert('RGB')
save(sharpen(vf,0.5),'bline-detail-zijvak-03.jpg','video leeskussen.mp4 (echte video, beeld op 22,0 s)','stilstaand beeld uit de video, 1080 x 1080, verscherpt','Telefoon in het zijvak van het leeskussen Bline, kleur Wit, met bies en label')
for kl in []:
    r=op(LK+f'{kl}-04.jpg')
    save(sharpen(fit(crop_ratio(r,1,1,r.width*0.32,r.height*0.62,r.width*0.6),1200,1200),0.4),f'bline-detail-vulling-{kl}.jpg',LK+f'{kl}-04.jpg (bol-beeld)','vierkante uitsnede van de open rits met traagschuim, 1200 x 1200',f'Traagschuim in het leeskussen Bline, kleur {kl.capitalize()}, met de rits open')
r=op(LK+'wit-06.jpg')
save(sharpen(fit(crop_ratio(r,1,1,r.width*0.32,r.height*0.62,r.width*0.6),1200,1200),0.4),'bline-detail-vulling-wit.jpg',LK+'wit-06.jpg (bol-foto)','vierkante uitsnede van de open rits met traagschuim, 1200 x 1200','Traagschuim in het leeskussen Bline, kleur Wit, met de rits open')

def font(sz,w='Bold'):
    f=ImageFont.truetype('NunitoSans.ttf',sz); f.set_variation_by_name(w); return f
KL=['wit','beige','blauw','grijs','zwart']; KN={k:k.capitalize() for k in KL}
INK=(31,42,55)
# 6 kleurtegels sfeer 4:5 (zelfde pose in alle kleuren), licht gelijkgetrokken
tiles={}
for k in KL:
    im=op(LK+'wit-gebruik-02.jpg') if k=='wit' else op(LK+f'{k}-gebruik-01.png')
    W,H=im.size; w=int(H*0.8); cx=int(W*0.45)
    tiles[k]=im.crop((cx-w//2,0,cx-w//2+w,H)).resize((1088,1360),Image.LANCZOS)
def wall_l(im): return np.array(im.convert('L').crop((40,40,300,300))).mean()
ref=np.median([wall_l(t) for t in tiles.values()])
for k,t in tiles.items():
    f=max(0.94,min(1.06,ref/wall_l(t)))
    t2=ImageEnhance.Brightness(t).enhance(f)
    src_n=(LK+'wit-gebruik-02.jpg (echte foto)') if k=='wit' else (LK+f'{k}-gebruik-01.png')
    save(sharpen(t2,0.4),f'bline-tegel-{k}-sfeer.jpg',src_n,f'uitsnede 4:5 in dezelfde kader voor alle vijf kleuren, 1088 x 1360, helderheid x{f:.2f} gelijkgetrokken op de muur, licht verscherpt',f'Vrouw leest een boek tegen het leeskussen Bline, kleur {KN[k]}, met haar telefoon in het zijvak')
# 7 packshots 4:5 voor hover
for k in KL:
    im=op(LK+f'{k}-01.jpg'); W,H=im.size; w=int(H*0.8)
    t=im.crop(((W-w)//2,0,(W-w)//2+w,H)).resize((1088,1360),Image.LANCZOS)
    save(sharpen(t,0.3),f'bline-tegel-{k}-packshot.jpg',LK+f'{k}-01.jpg (bol-beeld)','uitsnede 4:5 uit het midden, 1088 x 1360',f'Leeskussen Bline, kleur {KN[k]}, op een bed met een opengeslagen boek')
# 8 kleurenstrip en hoezenstrip
sl=[]
for k in KL:
    im=op(LK+f'{k}-01.jpg').resize((2048,2048),Image.LANCZOS); sl.append(im.crop((614,0,1434,2048)))
st=Image.new('RGB',(5*820+4*12,2048),'white')
for i,x in enumerate(sl): st.paste(x,(i*832,0))
st=st.resize((3000,int(3000*st.height/st.width)),Image.LANCZOS)
save(sharpen(st,0.3),'bline-kleuren-strip-01.jpg','bline-leeskussen-wit-01.jpg, -beige-01, -blauw-01, -grijs-01, -zwart-01 (bol-beelden, zelfde scène)','vijf smalle uitsneden naast elkaar met 12 px wit ertussen, 3000 x '+str(st.height),'Het leeskussen Bline in vijf kleuren naast elkaar: wit, beige, blauw, grijs en zwart')
sl=[]
for k in KL:
    im=op(f'bline-hoes-{k}-packshot-01.png'); W,H=im.size; sl.append(im.crop((W//2-340,0,W//2+340,H)))
st=Image.new('RGB',(5*680+4*12,1361),'white')
for i,x in enumerate(sl): st.paste(x,(i*692,0))
save(sharpen(st,0.3),'bline-hoezen-strip-01.jpg','bline-hoes-<kleur>-packshot-01.png (vijf kleuren)','vijf uitsneden uit het midden naast elkaar met 12 px wit ertussen, 3448 x 1361','Losse hoezen voor het leeskussen Bline in vijf kleuren naast elkaar, elk met het Bline-label')
# 9 bank
b=op(LK+'wit-03.jpg')
save(sharpen(fit(crop_ratio(b,16,9,1024,1024),2048,1152),0.3),'bline-banner-bank-16x9.jpg',LK+'wit-03.jpg (bol-beeld)','uitsnede 16:9, 2048 x 1152','Vrouw leest op de bank tegen het leeskussen Bline, kleur Wit, met haar telefoon in het zijvak')
b=op(LK+'zwart-02.jpg')
save(sharpen(fit(crop_ratio(b,4,5,1024,1024),1600,2000),0.3),'bline-sfeer-bank-zwart-4x5.jpg',LK+'zwart-02.jpg (bol-beeld)','uitsnede 4:5, 1600 x 2000','Vrouw leest op de bank tegen het leeskussen Bline, kleur Zwart')
# 10 bundels
def half(im,cx=0.5):
    im=im.resize((2048,2048),Image.LANCZOS) if im.width!=2048 else im
    x=int(2048*cx)-512; return im.crop((x,0,x+1024,2048))
def duo(a,b,name,src,alt):
    c=Image.new('RGB',(2048,2048),'white'); c.paste(a.crop((0,0,1018,2048)),(0,0)); c.paste(b.crop((6,0,1024,2048)),(1030,0))
    save(sharpen(c,0.3),name,src,'twee helften naast elkaar op 2048 x 2048 met 12 px wit ertussen',alt)
for kk,kh in [('wit','beige'),('beige','wit'),('blauw','grijs'),('grijs','blauw'),('zwart','grijs')]:
    duo(half(op(LK+f'{kk}-01.jpg'),0.5),half(op(f'bline-hoes-{kh}-packshot-01.png'),0.5),f'bline-set-{kk}-hoes-{kh}.jpg',f'{LK}{kk}-01.jpg en bline-hoes-{kh}-packshot-01.png',f'Set: leeskussen Bline in {kk} met een extra hoes in {kh}')
for kk in ['wit','beige','zwart']:
    g=tiles[kk].resize((1638,2048),Image.LANCZOS); g=g.crop((307,0,1331,2048))
    duo(half(op(LK+f'{kk}-01.jpg'),0.5),g,f'bline-set-twee-{kk}.jpg',f'{LK}{kk}-01.jpg en bline-tegel-{kk}-sfeer.jpg',f'Set van twee leeskussens Bline in {kk}')
# 11 cadeaubon
bg=fit(op(LK+'wit-packshot-01.jpg').crop((1350,0,5350,4000)),2048,2048)
d=ImageDraw.Draw(bg,'RGBA')
cw,ch=1100,700; x0=(2048-cw)//2; y0=1250
d.rectangle((x0,y0,x0+cw,y0+ch),fill=(255,255,255,246))
logo=Image.open(O+'bline-logo.png').convert('RGBA'); logo.thumbnail((440,200))
bg.paste(logo,((2048-logo.width)//2,y0+120),logo)
f=font(96); t='CADEAUBON'; tw=d.textlength(t,font=f); d.text(((2048-tw)/2,y0+380),t,font=f,fill=INK)
f2=font(58,'Regular'); t='€25, €50, €75 of €100'; tw=d.textlength(t,font=f2); d.text(((2048-tw)/2,y0+540),t,font=f2,fill=(26,26,26))
save(bg,'bline-cadeaubon-01.jpg',LK+'wit-packshot-01.jpg (echte foto) en bline-logo.png','vierkante uitsnede over de volle hoogte, 2048 x 2048, met een witte kaart (logo, CADEAUBON en de bedragen) eroverheen','Cadeaubon van Bline met het logo, op een foto van het leeskussen op bed')
# 12 maatgids tekening (bovenaanzicht)
Wc,Hc=2400,1260; c=Image.new('RGB',(Wc,Hc),'white'); d=ImageDraw.Draw(c)
sc=4.1; yb=230
fT=font(54); fS=font(40,'Regular'); fB=font(40)
d.text((80,70),'Het leeskussen op een bed van 200 cm lang (bovenaanzicht)',font=fT,fill=(26,26,26))
x=110
for bw in [140,160,180]:
    w=int(bw*sc); h=int(200*sc)
    d.rectangle((x,yb,x+w,yb+h),outline=(150,150,150),width=4,fill=(247,245,241))
    pw=int(65*sc); pd=int(45*sc); px=x+(w-pw)//2
    d.rectangle((px,yb+6,px+pw,yb+6+pd),fill=(205,191,169),outline=INK,width=4)
    t=f'{bw} x 200 cm'; d.text((x+(w-d.textlength(t,font=fB))/2,yb+h+24),t,font=fB,fill=(26,26,26))
    t='65 cm'; d.text((px+(pw-d.textlength(t,font=fB))/2,yb+6+pd/2-26),t,font=fB,fill=INK)
    vrij=str((bw-65)/2).replace('.0','').replace('.',',')+' cm'
    fv=font(36,'Regular'); ym=yb+6+pd/2-22
    d.text((x+(px-x-d.textlength(vrij,font=fv))/2,ym),vrij,font=fv,fill=(90,90,90))
    d.text((px+pw+(x+w-px-pw-d.textlength(vrij,font=fv))/2,ym),vrij,font=fv,fill=(90,90,90))
    d.text((px+(pw-d.textlength('45 cm diep',font=fv))/2,yb+pd+24),'45 cm diep',font=fv,fill=(90,90,90))
    x+=w+100
save(c,'bline-maatgids-bedden-01.jpg','eigen tekening (geen foto), maten uit de productgegevens','bovenaanzicht van drie bedden (140, 160 en 180 x 200 cm) met het kussen van 65 x 45 cm op schaal, 2400 x 1500','Tekening: het leeskussen van 65 cm breed en 45 cm diep op bedden van 140, 160 en 180 cm breed, met de ruimte die links en rechts overblijft')
json.dump(LOG,open('log1.json','w'),indent=1,ensure_ascii=False)
print(len(LOG))
