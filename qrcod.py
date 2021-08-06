import qrcode
url = "https://www.linkedin.com/in/luiz-daniel-ba1519199/"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit = True)

img = qr.make_image(fill_color="black", back_color="white")
img.show()