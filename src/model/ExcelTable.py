import pandas as pd


class ExcelTable:
    def __init__(self, excel_file, sheet_name):
        # Ler o arquivo Excel
        self.df = pd.read_excel(r'\resources\' + excel_file,
                           sheet_name=sheet_name)

    def get_row(self, code_to_search):
        # Verificar se a coluna 'CODIGO' existe
        if 'NUMEROFUNC' not in self.df.columns:
            raise ValueError("A coluna 'NUMEROFUNC' não foi encontrada no DataFrame.")

        # Converter a coluna e o código de pesquisa para strings e remover espaços extras
        self.df['NUMEROFUNC'] = self.df['NUMEROFUNC'].astype(str).str.strip()
        code_to_search = str(code_to_search).strip()

        # Encontrar as linhas onde o código está presente
        matching_rows = self.df[self.df['NUMEROFUNC'] == code_to_search]

        # Converter as linhas correspondentes para uma lista simples
        if not matching_rows.empty:
            result = matching_rows.values.flatten().tolist()
            return result
        else:
            return []

