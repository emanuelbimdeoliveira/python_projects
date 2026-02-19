import customtkinter as ctk

class HomeScreen(ctk.CTkFrame):
    def __init__(self, master, on_execute):
        super().__init__(master)
               
        self.on_execute = on_execute
        
        title = ctk.CTkLabel(self, text="Calculadora em Python", font=("Arial", 20, "bold"))
        title.pack(pady=20)      
        
        inputs = ctk.CTkFrame(self)
        inputs.pack(pady=10)

        self.first_factor = ctk.CTkEntry(inputs, placeholder_text="Primeiro Fator")
        self.first_factor.pack(side="left", pady=10, fill="x")

        self.operation = ctk.CTkEntry(inputs, placeholder_text="Operação")
        self.operation.pack(side="left", pady=10, fill="x")

        self.last_factor = ctk.CTkEntry(inputs, placeholder_text="Segundo Fator")
        self.last_factor.pack(side="left", pady=10, fill="x")

        self.error_label = ctk.CTkLabel(self, text="", text_color="red")
        self.error_label.pack(pady=5)
        
        button = ctk.CTkButton(self, text="Avançar", command=self.handle_execute)
        button.pack(side="left", padx=10)

    def handle_execute(self):
        self.error_label.configure(text="")

        try:
            data = {
                "first_factor": float(self.first_factor.get()),
                "operation": self.operation.get().strip(),
                "last_factor": float(self.last_factor.get())
            }
        except ValueError:
            self.error_label.configure(
                text="Digite números válidos."
            )
            return
        
        if not data["operation"]:
            self.error_label.configure(
                text="Informe a operação."
            )
            return

        self.on_execute(data)
