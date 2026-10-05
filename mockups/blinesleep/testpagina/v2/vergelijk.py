from PIL import Image, ImageDraw, ImageFont
import sys
B='/home/user/n8napi/research_notes/Bline Sleep risicos en voorbeelden/env_screens/'
def font(sz):
    f=ImageFont.truetype('NunitoSans.ttf',sz); f.set_variation_by_name('Bold'); return f
def zij(a,b,la,lb,out,w=700):
    A=Image.open(a).convert('RGB'); Bm=Image.open(b).convert('RGB')
    A=A.resize((w,int(A.height*w/A.width))); Bm=Bm.resize((w,int(Bm.height*w/Bm.width)))
    H=max(A.height,Bm.height)+50; S=Image.new('RGB',(2*w+30,H),'white'); d=ImageDraw.Draw(S)
    d.text((5,10),la,font=font(26),fill='black'); d.text((w+35,10),lb,font=font(26),fill='black')
    S.paste(A,(0,50)); S.paste(Bm,(w+30,50)); S.save(out,quality=75)
zij(B+'benchmark_yumeko_home.jpg',sys.argv[1]+'/home_desktop_volledig.jpg','Yumeko (benchmark)','Bline v2 (testpagina)',sys.argv[1]+'/vergelijk_home_yumeko.jpg')
zij(B+'productpaginas_mobiel.jpg',sys.argv[1]+'/product_mobiel_eerste_scherm.jpg','ENV-stores productpagina mobiel','Bline v2 product mobiel',sys.argv[1]+'/vergelijk_product_mobiel_env.jpg')
zij(B+'homepages_env_stores.jpg',sys.argv[1]+'/home_desktop_eerste_scherm.jpg','ENV-stores homepages','Bline v2 home desktop',sys.argv[1]+'/vergelijk_home_env.jpg')
