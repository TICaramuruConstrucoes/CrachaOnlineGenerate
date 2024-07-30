from src.model.ExcelTable import ExcelTable
from src.model.QRCode import QRCode


class ModelFacade:

    def __init__(self, excel_file, sheet_name):
        self.qr = None
        self.__excel_table = ExcelTable(excel_file, sheet_name)

    def generate_qrcode(self, code_to_search):
        row = self.__excel_table.get_row(code_to_search)

        self.qr = QRCode()

        data = self.qr.get_url(row)

        self.qr.save_qrcode(data)

        return data


