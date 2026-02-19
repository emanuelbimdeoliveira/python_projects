import customtkinter as ctk
from ui.screens import HomeScreen
from ui.screens import PreviewScreen
from ui.screens import ResultScreen
from controller.controller import handle_execute
from controller.controller import handle_preview

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
                
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("Python Tool")
        self.geometry("500x350")
        self.resizable(False, False)

        self.current_screen = None
        self.show_home()    
    
    def clear_screen(self):
        if self.current_screen():
            self.current_screen.destroy()
    
    def show_home(self):
        self.clear_screen()
        self.current_screen = HomeScreen(self, self.show_preview, self.execute_preview)
        self.current_screen.pack(fill="both", expand=True)

    def show_preview(self, path):
        data = [f"Example rename from {path}"]
        self.clear_screen()
        self.current_screen = PreviewScreen(self, data=data, on_confirm=self.show_result, on_back=self.show_home)
        self.current_screen.pack(fill="both", expand=True)

    def show_result(self):
        self.clear_screen()
        self.current_screen = ResultScreen(self, "Operation completed successfully!", self.quit)
        self.current_screen.pack(fill="both", expand=True)

    def execute_preview(self, path):
        try:
            handle_preview(path)

        except Exception as e:
            self.show_error(str(e))

    def execute(self):
        path = self.path_input.get()
        
        try: 
            result = handle_execute(path)
            self.show_result(result)
        except Exception as e:
            self.show_error(str(e))