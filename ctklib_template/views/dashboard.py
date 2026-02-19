import customtkinter as ctk

class Dashboard(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # O fg_color será transparente para herdar do fundo da janela principal
        self.configure(fg_color="transparent")

        self.label = ctk.CTkLabel(self, text="Painel de Controle", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)

        self.btn_logica = ctk.CTkButton(self, text="Executar Regra de Negócio", command=self.minha_logica)
        self.btn_logica.pack(pady=10)

    def minha_logica(self):
        # Aqui entra a sua validação, acesso a banco, etc.
        print("Lógica disparada!")