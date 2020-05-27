import qrcode
#生成二维码
image = qrcode.make("https://github.com/leonwoo18/cs50")
image.save("qr.png", "PNG")