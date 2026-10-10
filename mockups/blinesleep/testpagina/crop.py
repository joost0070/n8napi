"""Knipt een lange screenshot in stukken van max 1800 px hoog (voor bekijken). python3 crop.py bestand.png"""
import sys
from PIL import Image
f=sys.argv[1]; im=Image.open(f); w,h=im.size; step=int(sys.argv[2]) if len(sys.argv)>2 else 1800
scale = 1
for i,y in enumerate(range(0,h,step)):
    im.crop((0,y,w,min(h,y+step))).save(f.replace('.png',f'_deel{i+1}.png'))
print(w,h,(h+step-1)//step)
