import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        # O corner_radius=0 faz a sidebar ficar reta no canto da janela
        super().__init__(master, corner_radius=0, **kwargs)
        
        # --- 1. LOGO / TÍTULO ---
        self.logo_label = ctk.CTkLabel(
            self, 
            text="MINHA MARCA", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.logo_label.pack(pady=(30, 20), padx=20)

        # --- 2. BOTÕES DE NAVEGAÇÃO ---
        # No futuro, você pode passar o comando para trocar de tela no main.py
        self.btn_home = self._criar_botao_menu("Home", "home_icon")
        self.btn_example = self._criar_botao_menu("Exemplo", "star_icon")
        self.btn_form = self._criar_botao_menu("Formulário", "user_icon")
        self.btn_config = self._criar_botao_menu("Configurações", "settings_icon")

        # --- 3. ESPAÇADOR (Empurra o que vem abaixo para o rodapé) ---
        self.spacer = ctk.CTkLabel(self, text="")
        self.spacer.pack(expand=True, fill="both")

        # --- 4. SEPARADOR VISUAL (Opcional) ---
        self.linha_divisora = ctk.CTkFrame(self, height=2, fg_color=["#0a4040", "#d97925"])
        self.linha_divisora.pack(fill="x", padx=20, pady=10)

        # --- 5. CONTROLES DE RODAPÉ (Tema e Sair) ---
        self.label_tema = ctk.CTkLabel(self, text="Modo de Exibição:", font=ctk.CTkFont(size=11))
        self.label_tema.pack(padx=20, pady=(0, 5))

        self.seletor_tema = ctk.CTkOptionMenu(
            self,
            values=["Light", "Dark", "System"],
            command=self._alterar_tema
        )
        self.seletor_tema.pack(padx=20, pady=(0, 20))
        self.seletor_tema.set("System")

    def _criar_botao_menu(self, texto, icone_nome, command=None):
        """Método auxiliar para manter os botões com o mesmo estilo"""
        btn = ctk.CTkButton(
            self,
            text=texto,
            height=40,
            anchor="w",      # Alinha o texto à esquerda
            border_spacing=10,
            fg_color="transparent", # Deixa o fundo limpo, usa o hover do JSON
            command=command
        )
        btn.pack(fill="x", padx=10, pady=5)
        return btn

    def _alterar_tema(self, novo_tema):
        ctk.set_appearance_mode(novo_tema)