from PIL import Image, ImageDraw, ImageFont
import random

# size = (400, 400) # x, y

# img = Image.new('RGB', size, color = color)

bg = Image.open("bg.jpg")
bg = bg.convert('L')
bg.save("bgc.jpg")

img = Image.open("bgc.jpg")
img = img.convert("RGBA")
size = img.size

textsize = round(size[0] / 10)
fnt = ImageFont.truetype("italic font.ttf", textsize)
text = "tika"
color = '#00000000'

txtlayer = Image.new('RGBA', size, color = color)

d = ImageDraw.Draw(txtlayer)
tw, th = d.textsize(text, font = fnt)

textarea = ((size[0]-tw)/2, (size[1]-th)/2)
bluearea = (((size[0]-tw)/2) + 2, (size[1]-th)/2)
pinkarea = (((size[0]-tw)/2) - 2, (size[1]-th)/2)

d.text(bluearea, text, font=fnt, fill='#1CE9DC')
d.text(pinkarea, text, font=fnt, fill='#E000B6')
d.text(textarea, text, font=fnt, fill='white')

# top y and bottom y
minY = round((size[1] - th) / 2)
maxY = round((size[1] + th) / 2)

for x in range(3):
	movement = random.randint(-15, 15)
	width = random.randint(2, 5)
	y = random.randint(minY, maxY)

	# box=(left, upper, right, lower)
	region = txtlayer.crop((0, y, size[0]-movement, y+width))
	txtlayer.paste(region, (movement, y, size[0], y+width))

img.paste(txtlayer, (0, 0), txtlayer)

img.save("out.png", optimize=True)