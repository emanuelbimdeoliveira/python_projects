import customtkinter as ctk
from views.logs import ProcessadorView

class HomeView(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Como o JSON já define o fundo do Frame, 
        # aqui focamos apenas em organizar os elementos.
        self.configure(fg_color="transparent") # Para herdar a cor do fundo principal

        # Título de Boas-Vindas
        self.titulo = ctk.CTkLabel(
            self, 
            text="Bem-vindo ao Sistema", 
            font=ctk.CTkFont(size=28, weight="bold")
        )
        self.titulo.pack(pady=(40, 10))

        # Descrição
        self.descricao = ctk.CTkLabel(
            self, 
            text="Este é o seu template profissional utilizando CustomTkinter.\n"
                 "Aqui você pode adicionar uma visão geral do seu software.",
            font=ctk.CTkFont(size=14),
            justify="center"
        )
        self.descricao.pack(pady=10)

        # Card de Destaque (Exemplo de como agrupar informações)
        self.card_info = ctk.CTkFrame(self)
        self.card_info.pack(pady=30, padx=50, fill="x")

        self.card_titulo = ctk.CTkLabel(
            self.card_info, 
            text="Dica de Uso", 
            font=ctk.CTkFont(weight="bold")
        )
        self.card_titulo.pack(pady=(10, 5))

        self.card_texto = ctk.CTkLabel(
            self.card_info, 
            text="Para trocar de tela, basta usar o método 'mudar_tela' no arquivo main.py.\n"
                 "Toda a estilização é controlada pelo arquivo meu_tema.json."
        )
        self.card_texto.pack(pady=(0, 15))

        self.logs = ProcessadorView(self)
        self.logs.pack()