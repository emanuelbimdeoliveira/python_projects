import customtkinter as ctk
import os
import sys
from views.home import HomeView
from views.exemplo import ExemploView
from views.form import FormularioView
from components.sidebar import Sidebar

# Garante que o Python encontre as pastas 'components' e 'views'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Configuração do Tema (Caminho absoluto para evitar erros)
        caminho_base = os.path.dirname(os.path.abspath(__file__))
        caminho_tema = os.path.join(caminho_base, "theme_config.json")
        
        try:
            ctk.set_default_color_theme(caminho_tema)
        except Exception as e:
            print(f"Aviso: Não foi possível carregar o JSON. Erro: {e}")

        # 2. Configurações da Janela
        self.title("Meu Template CustomTkinter")
        self.geometry("1100x600")

        # 3. Layout Principal (Grid 1x2)
        # Coluna 0 (Sidebar) não expande, Coluna 1 (Conteúdo) expande.
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 4. Instanciando a Sidebar
        self.sidebar = Sidebar(master=self, width=220)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.sidebar.btn_home.configure(command=lambda: self.mudar_tela(HomeView))
        self.sidebar.btn_example.configure(command=lambda: self.mudar_tela(ExemploView))
        self.sidebar.btn_form.configure(command=lambda: self.mudar_tela(FormularioView))

        # 5. Container Principal (Onde as Telas/Views entrarão)
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Variável para controlar a tela que está sendo exibida
        self.tela_atual = None
        self.mudar_tela(HomeView)

    def mudar_tela(self, nova_tela_classe):
        """
        Recebe uma classe de tela (View), limpa o container e a exibe.
        """
        if self.tela_atual is not None:
            self.tela_atual.destroy()
        
        # Cria a nova tela dentro do container
        self.tela_atual = nova_tela_classe(master=self.container)
        self.tela_atual.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()