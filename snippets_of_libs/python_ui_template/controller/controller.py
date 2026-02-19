from core.example import process_value
from tkinter import messagebox

def handle_preview(value):
    try:
        result = process_value(value)
        messagebox.showinfo("Resultado do preview: ", result)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def handle_execute(value):
    try:
        result = process_value(value)
        messagebox.showinfo("Resultado", result)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


