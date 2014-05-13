import PIL
from PIL import Image

basewidth = 300
img = Image.open("/Users/ys_park/Desktop/TEMP/Icon-1024.png")
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save("/Users/ys_park/Desktop/TEMP/Icon-300.png")
