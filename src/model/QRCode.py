import qrcode


class QRCode:
    def __init__(self):
        self.qr = qrcode.QRCode(
            version=3,
            box_size=3,
            border=5,
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )

    def save_qrcode(self, data):
        self.qr.add_data(data)

        self.qr.make(fit=True)

        img = self.qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image
        img.save("qr_code.png")

    def get_url(self, row):
        data = (
                "https://ticaramuruconstrucoes.github.io/?"
                + "&Cracha=" + str(row[0])
                + "&Nome=" + row[1].replace(" ", "%20")
                + "&CPF=" + str(row[2])
                + "&RG=" + str(row[3])
                + "&Nascimento=" + str(row[4].strftime('%Y-%m-%d'))
                + "&Sexo=" + ('Masculino' if row[5] == 'M' else 'Feminino')
        )

        return data
