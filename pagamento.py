import qrcode
data = ''

img = qrcode.make(data)
img.save('MyQRCode3.png')
