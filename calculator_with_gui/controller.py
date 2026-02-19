def controller(result):
    first_factor = result["first_factor"]
    operation = result["operation"]
    last_factor = result["last_factor"]

    match (operation):
        case "+":
            result = first_factor + last_factor
        case "-":
            result = first_factor - last_factor
        case "*":
            result = first_factor * last_factor
        case "/":
            if last_factor == 0: 
                result = "Infelizmente você tentou dividir por 0..."
            else: result = first_factor / last_factor
        case _:
            result = "Parece que a operação é inválida..."

    if result is float: return f"{result:.0}"
    else: return result