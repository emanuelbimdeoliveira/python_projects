import customtkinter as ctk

class ProcessadorView(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        # --- Entrada de Dados ---
        self.label = ctk.CTkLabel(self, text="Insira os dados para processar:", font=("Roboto", 14, "bold"))
        self.label.pack(pady=(10, 5))

        self.entrada = ctk.CTkEntry(self, placeholder_text="Ex: Nome do cliente", width=400)
        self.entrada.pack(pady=10)

        # --- Botão de Ação ---
        self.btn_rodar = ctk.CTkButton(self, text="🚀 Iniciar Processamento", command=self.executar_logica)
        self.btn_rodar.pack(pady=10)

        # --- CAIXA DE LOG (O Feedback do Usuário) ---
        self.log_titulo = ctk.CTkLabel(self, text="Status do Sistema:", font=("Roboto", 12))
        self.log_titulo.pack(pady=(20, 0), anchor="w", padx=40)

        self.caixa_log = ctk.CTkTextbox(self, width=500, height=150, state="disabled")
        self.caixa_log.pack(pady=(5, 10), padx=40)

    def escrever_no_log(self, mensagem):
        """Função simples para adicionar texto ao log"""
        self.caixa_log.configure(state="normal") # Habilita para escrever
        self.caixa_log.insert("end", f" -> {mensagem}\n") # Adiciona o texto
        self.caixa_log.configure(state="disabled") # Trava para o usuário não apagar
        self.caixa_log.see("end") # Faz o scroll automático para o final

    def executar_logica(self):
        """Aqui entra o seu Python de Alto Nível"""
        dado = self.entrada.get()
        
        if not dado:
            self.escrever_no_log("ERRO: O campo de entrada está vazio!")
            return

        # Simulando uma lógica de freelancer
        self.escrever_no_log(f"Iniciando busca para: {dado}...")
        self.escrever_no_log("Conectando ao banco de dados...")
        self.escrever_no_log("✅ Sucesso: Dados salvos com sucesso!")