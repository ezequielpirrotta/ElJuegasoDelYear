import qrcode


def create_qrcode(link):
    qr_img = qrcode.make(link)
    qr_img.save("myTestQRCode.png")
    qr_img.show()

def main():
    page_link = ""
    print("Ingrese un link: ")
    input(page_link)
    create_qrcode(str(page_link))

main()