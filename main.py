import qrcode

link = input("Enter the link: ")

qr = qrcode.make(link)

qr.save("qrcode.png")

print("QR code created successfully!")
