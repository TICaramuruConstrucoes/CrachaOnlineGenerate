# CrachaOnline

Aplicativo para gerar códigos QR para crachás de funcionários usando python.

## Estrutura do Projeto :wrench:

```plaintext
src/
│
├── model/
│   ├── CrachaOnlineFacade.py    # Facade para gerar o QR Code.
│   ├── ExcelTable.py            # Manipulação de dados a partir de uma planilha Excel.
│   └── QRCode.py                # Geração e salvamento do QR Code.
│
├── view/
│   └── CrachaOnlineView.py      # Interface gráfica para entrada e exibição de QR Codes.
│
├── viewModel/
│   └── CrachaOnlineViewModel.py # Lógica para geração de QR Code e tratamento de erros.
│
└── CrachaOnlineClient.py        # Arquivo principal que inicia a aplicação.
│
resources/
│   └── Crachas.xlsx             # Arquivo de planilha com dados dos funcionários.
│
assets/
    └── COIcon.ico               # Ícone do aplicativo.
````

## Requisitos :mag:

Certifique-se de ter os seguintes pacotes instalados:

- `tkinter`
- `pillow`
- `pandas`
- `qrcode`

## Uso no Desktop :computer:

Para criar um executável do aplicativo que pode ser executado diretamente no seu desktop, você pode usar o `pyinstaller`. Siga os passos abaixo:

### 1. Instale o PyInstaller

Certifique-se de ter o `pyinstaller` instalado. Você pode instalá-lo usando o pip:

```bash
pip install pyinstaller
```

### 2. Gere o Executável

Execute o seguinte comando para criar um arquivo executável único (.exe) que inclui um ícone personalizado e não exibe um terminal ao ser executado:

```bash
pyinstaller --onefile --windowed --icon=assets/COIcon.ico src/CrachaOnlineClient.py
```

Após a execução do comando, o executável será gerado na pasta `dist/.` Você pode distribuir este arquivo e executá-lo diretamente em qualquer máquina que tenha o sistema operacional compatível.

![image](https://github.com/user-attachments/assets/c2298ed5-c03b-4dfe-a46d-b4f06a6b8d84)

