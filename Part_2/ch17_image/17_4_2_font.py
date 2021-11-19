from PIL import Image, ImageDraw, ImageFont
import os, sys

currentPath = os.path.dirname(sys.argv[0])
img = Image.new('RGBA', (200,200), 'white')
draw = ImageDraw.Draw(img)
draw.text((20,150), 'Hello', fill='purple')
fontsPath = 'C:\\Windows\\Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsPath, 'arial.ttf'), 32)
draw.text((100,150), 'Howdy', fill='gray', font=arialFont)
img.save(os.path.join(currentPath, '17_4_2_text.png'))