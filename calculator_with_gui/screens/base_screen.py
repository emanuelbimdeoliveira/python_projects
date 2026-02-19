import customtkinter as ctk

class BaseScreen(ctk.CTkFrame):
    def __init__(self, master, title=None):
        super().__init__(master)

        self.pack(fill="both", expand=True, padx=20, pady=20)

        if title:
            self.title_label = ctk.CTkLabel(
                self,
                text=title,
                font=("Arial", 20, "bold")
            )
            self.title_label.pack(pady=(0, 20))

        self.error_label = ctk.CTkLabel(
            self,
            text="",
            text_color="red"
        )
        self.error_label.pack(pady=5)

    def show_error(self, message):
        self.error_label.configure(text=message)

    def clear_error(self):
        self.error_label.configure(text="")
