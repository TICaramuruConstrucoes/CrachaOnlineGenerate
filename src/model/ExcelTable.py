import os
import pandas as pd


class ExcelTable:
    def __init__(self, excel_file, sheet_name):

        base_dir = os.path.dirname(__file__)

        resources_dir = os.path.abspath(os.path.join(base_dir, '..', '..', 'resources'))
        file_path = os.path.join(resources_dir, excel_file)

        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

        self.df = pd.read_excel(file_path, sheet_name=sheet_name)

    def get_row(self, code_to_search, table):
        # Verificar se a coluna 'CODIGO' existe
        if table not in self.df.columns:
            raise ValueError(f"A coluna {table} não foi encontrada no DataFrame.")

        # Converter a coluna e o código de pesquisa para strings e remover espaços extras
        self.df[table] = self.df[table].astype(str).str.strip()
        code_to_search = str(code_to_search).strip()

        # Encontrar as linhas onde o código está presente
        matching_rows = self.df[self.df[table] == code_to_search]

        # Converter as linhas correspondentes para uma lista simples
        if not matching_rows.empty:
            result = matching_rows.values.flatten().tolist()
            return result
        else:
            return []
