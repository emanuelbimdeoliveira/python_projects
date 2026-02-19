import customtkinter as ctk

class PreviewScreen(ctk.CTkFrame):
    def __init__(self, master, data, on_confirm, on_back):
        super().__init__(master)

        self.on_confirm = on_confirm
        self.on_back = on_back

        label = ctk.CTkLabel(self, text="Preview changes", font=("Arial", 16, "bold"))
        label.pack(pady=10)
    
        textbox = ctk.CTkTextbox(self, height=150)
        textbox.pack(padx=20, pady=10, fill="both", expand=True)
        
        for item in data:
            textbox.insert("end", f"{item}\n")
        
        buttons = ctk.CTkFrame(self)
        buttons.pack(pady=10)

        back = ctk.CTkButton(buttons, text="Back", command=self.on_back)
        back.pack(side="left", padx=10)
        
        confirm = ctk.CTkButton(buttons, text="Confirm", command=self.on_confirm)
        confirm.pack(side="left", padx=10)
