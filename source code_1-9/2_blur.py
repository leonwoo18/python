#导库可以轻松实现对照片的模糊
from PIL import Image,ImageFilter

before = Image.open("bridge.bmp")
after = before.filter(ImageFilter.BLUR)
after.save("out.bmp")