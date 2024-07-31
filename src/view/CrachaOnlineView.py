# View/CrachaOnlineView.py
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class CrachaOnlineView:
    def __init__(self, root, view_model):
        self.view_model = view_model
        self.root = root
        self.root.title("Crachá Online - QRcode")
        self.root.configure(bg='#09933E')  # Definir a cor de fundo da janela principal

        base_dir = os.path.dirname(__file__)
        assets_dir = os.path.abspath(os.path.join(base_dir, '..', '..', 'assets'))
        self.icon_path = os.path.join(assets_dir, "COIcon.ico")

        if os.path.exists(self.icon_path):
            root.iconbitmap(self.icon_path)
        else:
            messagebox.showwarning("Aviso", "Ícone não encontrado. Usando ícone padrão.")

        # Definir a fonte padrão
        font_name = "Montserrat"
        font_size_label = 12
        font_size_entry = 14
        font_size_button = 12

        # Criação dos widgets
        self.label = tk.Label(root,
                              text="Digite o RE/Crachá do Funcionário:",
                              bg='#09933E',
                              fg='white',
                              font=(font_name, font_size_label))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root,
                              width=30,
                              font=(font_name, font_size_entry))
        self.entry.pack(padx=20,
                        pady=10)

        self.generate_button = tk.Button(root,
                                         text="Gerar QRCode",
                                         command=self.generate_qrcode,
                                         bg='gray',
                                         fg='white',
                                         font=(font_name, font_size_button))
        self.generate_button.pack(pady=10)

        self.image_label = tk.Label(root,
                                    bg='#09933E')
        self.image_label.pack(pady=10)

    def generate_qrcode(self):
        code_to_search = self.entry.get()
        self.view_model.generate_qr_code(code_to_search)
        if self.view_model.error_message:
            messagebox.showwarning("Erro", self.view_model.error_message)
        else:
            self.show_qr_code_image()

    def show_qr_code_image(self):
        # Caminho para a imagem
        image_path = "qr_code.png"

        if os.path.exists(image_path):
            # Abrir a imagem usando Pillow
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)

            # Atualizar o rótulo com a imagem
            self.image_label.config(image=photo)
            self.image_label.image = photo
        else:
            messagebox.showerror("Erro", "Imagem QR code não encontrada.")
