import customtkinter as ctk

# =================================================================
# CONFIGURAÇÕES DE IDENTIDADE VISUAL (Dicionário Central)
# =================================================================
# O Formato é: ("COR_PARA_LIGHT", "COR_PARA_DARK")
CORES = {
    "primaria": ("#0a4040", "#126161"),      # Verde Petróleo
    "primaria_light": ("#0a4f4f", "#1a7575"),
    "fundo_janela": ("#f2ebdc", "#0d0d0d"),  # Creme / Preto
    "texto": ("#0d0d0d", "#f2ebdc"),         # Inversão de contraste
    "accent": ("#d97925", "#d97925"),        # Laranja (fixo para ambos)
    "texto_on_accent": "#f2ebdc"             # Texto claro sobre fundo escuro
}

class TemplateDefinitivo(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuração da Janela ---
        self.title("CTK Master Template")
        self.geometry("1000x600")
        self.configure(fg_color=CORES["fundo_janela"])

        # Grid 1x2 (Sidebar x Conteúdo)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR ---
        self.sidebar = ctk.CTkFrame(self, fg_color=CORES["primaria"], corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo = ctk.CTkLabel(self.sidebar, text="MINHA MARCA", 
                                 text_color=CORES["texto_on_accent"],
                                 font=ctk.CTkFont(size=22, weight="bold"))
        self.logo.pack(pady=30, padx=20)

        # Botões de Navegação (Exemplo)
        self.nav_1 = self.criar_botao_nav("Dashboard")
        self.nav_2 = self.criar_botao_nav("Configurações")

        # --- SELETOR DE TEMA (Na parte inferior da sidebar) ---
        self.label_tema = ctk.CTkLabel(self.sidebar, text="Modo do Sistema:", 
                                       text_color=CORES["texto_on_accent"], font=("Arial", 12))
        self.label_tema.pack(side="bottom", pady=(10, 5))
        
        self.seletor_tema = ctk.CTkOptionMenu(
            self.sidebar, 
            values=["Light", "Dark", "System"],
            command=self.mudar_tema,
            fg_color=CORES["accent"],
            button_color=CORES["accent"],
            button_hover_color=CORES["primaria_light"],
            dropdown_fg_color=CORES["primaria_light"]
        )
        self.seletor_tema.pack(side="bottom", pady=(0, 20), padx=20)
        self.seletor_tema.set("Light") # Valor padrão inicial

        # --- ÁREA DE CONTEÚDO PRINCIPAL ---
        self.conteudo = ctk.CTkFrame(self, fg_color="transparent")
        self.conteudo.grid(row=0, column=1, padx=30, pady=30, sticky="nsew")

        self.titulo_pagina = ctk.CTkLabel(self.conteudo, text="Página Inicial", 
                                          text_color=CORES["texto"], 
                                          font=ctk.CTkFont(size=28, weight="bold"))
        self.titulo_pagina.pack(anchor="w", pady=(0, 20))

        # Card de Exemplo
        self.card = ctk.CTkFrame(self.conteudo, fg_color=("white", "#1e1e1e"), border_width=1, border_color=CORES["primaria"])
        self.card.pack(fill="x", pady=10, padx=5)
        
        self.info_label = ctk.CTkLabel(self.card, text="Este é um card de exemplo para seus dados.", text_color=CORES["texto"])
        self.info_label.pack(pady=20)

        # Input e Botão de Ação
        self.input_demo = ctk.CTkEntry(self.conteudo, placeholder_text="Digite aqui...", 
                                       width=400, border_color=CORES["primaria"])
        self.input_demo.pack(pady=10)

        self.btn_main = ctk.CTkButton(self.conteudo, text="Salvar Alterações", 
                                      fg_color=CORES["accent"], 
                                      hover_color=CORES["primaria_light"],
                                      text_color=CORES["texto_on_accent"])
        self.btn_main.pack(pady=10)

    # --- MÉTODOS AUXILIARES ---
    def criar_botao_nav(self, texto):
        btn = ctk.CTkButton(
            self.sidebar, 
            text=texto, 
            fg_color="transparent", 
            text_color=CORES["texto_on_accent"],
            hover_color=CORES["primaria_light"],
            anchor="w"
        )
        btn.pack(fill="x", padx=10, pady=5)
        return btn

    def mudar_tema(self, novo_tema: str):
        ctk.set_appearance_mode(novo_tema)

if __name__ == "__main__":
    # Inicializa o modo light por padrão (combinando com suas cores principais)
    ctk.set_appearance_mode("light") 
    app = TemplateDefinitivo()
    app.mainloop()