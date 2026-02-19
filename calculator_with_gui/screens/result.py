import customtkinter as ctk

class ResultScreen(ctk.CTkFrame):
    def __init__(self, master, data, on_restart):
        super().__init__(master)

        self.data = data
        self.on_restart = on_restart

        textbox = ctk.CTkTextbox(self, height=150)
        textbox.pack(padx=20, pady=10, fill="both", expand=True)
     
        textbox.insert("end", f"Resultado: {self.data}\n")

        button = ctk.CTkButton(self, text="Reiniciar?", command=on_restart)
        button.pack(pady=20)


