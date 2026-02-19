import customtkinter as ctk

class BaseScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

    def show(self):
        self.pack(fill="both", expand=True)
        
    def hide(self):
        self.pack_forget()