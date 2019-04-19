import numpy as np
import string
from PIL import Image, ImageFont, ImageDraw
def genIMG(t, f, fn, s = (128, 128), o = (16, 0)):
	img = Image.new('RGB', s, "black")
	print(t);
	draw = ImageDraw.Draw(img)
	draw.text(OFS, t, (255, 255, 255), font = f)
	img.save(fn)
CS = list(string.ascii_letters) + list(string.digits)
RTS = list(np.random.randint(10, 64, size = 100)) + [64]
S = [''.join(np.random.choice(CS, i)) for i in RTS]
font = ImageFont.truetype("/Library/Fonts/arial.ttf", 18)
MS = max(font.getsize(Si) for Si in S)
OFS = ((640 - MS[0]) // 2, (32 - MS[1]) // 2)
MS = (640, 32)
Y = []
for i, Si in enumerate(S):
    genIMG(Si, font, str(i) + '.png', MS, OFS)
    Y.append(str(i) + '.png,' + Si)
with open('Train.csv', 'w') as F:
    F.write('\n'.join(Y))
if(__name__=='__main__'):
	genIMG('j', font, 'jGen.png')
