import qrcode
img=qrcode.make('welcome to python language')
img.save('qr.png')
print('qr code generated')
