import sys
from PIL import Image
out=sys.argv[1]; files=sys.argv[2:]
cols=[]
for f in files:
    im=Image.open(f); w=900 if 'desktop' in f else 300; cols.append(im.resize((w,int(im.height*w/im.width))))
H=max(c.height for c in cols); W=sum(c.width for c in cols)+20*(len(cols)-1)
S=Image.new('RGB',(W,H),'white'); x=0
for c in cols: S.paste(c,(x,0)); x+=c.width+20
S.thumbnail((2000,2000)); S.save(out,quality=80); print(S.size)
