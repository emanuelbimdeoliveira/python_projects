def process_value(value):
    if not value:
        raise ValueError("Valor vazio...")
    return f"Processando: {value.upper()}"