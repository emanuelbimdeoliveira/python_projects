import customtkinter as ctk

class FormularioView(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        ctk.CTkLabel(self, text="Cadastro de Projeto", font=("Roboto", 20, "bold")).pack(pady=20)

        # Campo de Texto
        self.nome_projeto = ctk.CTkEntry(self, placeholder_text="Nome do Projeto", width=350)
        self.nome_projeto.pack(pady=10)

        # Switch (Interruptor) - Se der erro aqui, falta no JSON!
        self.prioridade = ctk.CTkSwitch(self, text="Projeto Prioritário")
        self.prioridade.pack(pady=10)

        # Caixa de Seleção
        self.check_termos = ctk.CTkCheckBox(self, text="Aceito os termos de uso")
        self.check_termos.pack(pady=10)

        # Botão de Ação
        self.btn_salvar = ctk.CTkButton(self, text="Salvar Projeto", command=self.salvar)
        self.btn_salvar.pack(pady=20)

    def salvar(self):
        print(f"Salvando: {self.nome_projeto.get()}")