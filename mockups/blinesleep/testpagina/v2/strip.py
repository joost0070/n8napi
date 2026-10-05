import sys
from PIL import Image
src,out,ph=sys.argv[1],sys.argv[2],int(sys.argv[3])
im=Image.open(src); W,H=im.size; n=(H+ph-1)//ph
S=Image.new('RGB',(W*n+20*(n-1),ph),'white')
for i in range(n): S.paste(im.crop((0,i*ph,W,min(H,(i+1)*ph))),(i*(W+20),0))
S.thumbnail((2600,2600)); S.save(out,quality=80); print(im.size,S.size)
