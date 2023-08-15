import qrcode


def generate_qr_code():
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=50, border=10)
    try:
        data = input("Write down the URL or text, that you would like to convert into a QR Code.\n")
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qr_codes/qrcode.png")
    except:
        print("Something went wrong.")
    generate_qr_code()


generate_qr_code()
