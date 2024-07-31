from src.model.CrachaOnlineFacade import CrachaOnlineFacade


class CrachaOnlineViewModel:
    def __init__(self):
        self.error_message = None

    def generate_qr_code(self, code_to_search):
        if not code_to_search:
            self.error_message = "Por favor, insira um código."
            return

        try:
            # Substitua pelo caminho correto do arquivo e a aba
            facade = CrachaOnlineFacade('Crachas.xlsx', 'Sheet1')
            facade.generate_qrcode(code_to_search, 'CRACHA')
            self.error_message = None
        except Exception as e:
            self.error_message = str(e)
