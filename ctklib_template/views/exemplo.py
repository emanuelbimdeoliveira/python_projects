import customtkinter as ctk

class ExemploView(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        self.label = ctk.CTkLabel(self, text="Exemplos de Componentes", font=("Roboto", 20, "bold"))
        self.label.pack(pady=20)

        # Campo de Entrada
        self.entrada = ctk.CTkEntry(self, placeholder_text="Digite algo aqui...", width=300)
        self.entrada.pack(pady=10)

        # Checkbox
        self.check = ctk.CTkCheckBox(self, text="Habilitar funcionalidade X")
        self.check.pack(pady=10)

        # Botão com a cor de destaque (Accent)
        self.btn_executar = ctk.CTkButton(
            self, 
            text="Executar Ação Principal",
            command=self.acao_exemplo
        )
        self.btn_executar.pack(pady=20)

    def acao_exemplo(self):
        valor = self.entrada.get()
        print(f"Ação executada com o valor: {valor}")