import customtkinter as ctk

class HomeScreen(ctk.CTkFrame):
    def __init__(self, master, on_next, on_execute_preview):
        super().__init__(master)

        self.on_next = on_next
        self.on_execute_preview = on_execute_preview
                
        title = ctk.CTkLabel(self, text="File Renamer", font=("Arial", 20, "bold"))
        title.pack(pady=20)

        self.entry = ctk.CTkEntry(self, placeholder_text="Path da pasta")
        self.entry.pack(padx=40, pady=10, fill="x")

        button = ctk.CTkButton(self, text="Next", command=self.handle_next)
        button.pack(pady=20)

    def handle_next(self):
        path = self.entry.get()
        self.on_execute_preview(path)
        self.on_next(path)        