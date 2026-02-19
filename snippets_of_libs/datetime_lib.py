#  Essa é a lib do datetime e o seu uso mais comum

from datetime import datetime

# 1. Pegar agora (Igual ao new Date())
agora = datetime.now()
print(agora) # 2026-01-14 15:30:45.123

# 2. Formatar para String (strftime - "string from time")
# Útil para dar nome a arquivos com a data de hoje
data_formatada = agora.strftime("%d-%m-%Y_%H-%M")
print(data_formatada) # "14-01-2026_15-30"

# 3. Criar uma data específica
aniversario = datetime(2026, 5, 20)

# 4. Operações de tempo (Precisa do timedelta)
from datetime import timedelta
amanha = agora + timedelta(days=1)