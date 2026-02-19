import customtkinter as ctk
from screens.home import HomeScreen
from screens.result import ResultScreen

class App(ctk.CTk):
    def __init__(self, handle_execute):
        super().__init__()           
        self.handle_execute = handle_execute
                    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("Calculadora em Python")

        self.geometry("500x350")
        self.resizable(False, False)

        self.current_screen = None
        self.show_home()     

    def clear_screen(self):
        if self.current_screen:
            self.current_screen.destroy()  

    def show_home(self):
        self.clear_screen()
        self.current_screen = HomeScreen(self, on_execute=self.show_result)
        self.current_screen.pack(fill="both", expand=True)

    def show_result(self, data):
        self.clear_screen()
        result = self.handle_execute(data)        
        self.current_screen = ResultScreen(self, data=result, on_restart=self.show_home)
        self.current_screen.pack(fill="both", expand=True)
               
