import PIL
from PIL import Image

basewidth = [512,152,144,120,114,76,72,58,57,50,29,16]

orginalImg = Image.open("/Users/ys_park/Desktop/TEMP/Icon-1024.png")


for r in basewidth:
	desImg = "/Users/ys_park/Desktop/TEMP/reIcon-%d.png" % r
	print desImg
	orginalImg = orginalImg.resize((r, r), PIL.Image.ANTIALIAS)
	orginalImg.save(desImg)
