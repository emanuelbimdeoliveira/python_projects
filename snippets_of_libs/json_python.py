"""
Biblioteca json
"""

"""
A regra de ouro é:
Sem "s" (load, dump): Interage com arquivos (precisa do open).
Com "s" (loads, dumps): Interage com strings (o "s" vem de string).
"""

"""
1. Manipulando Arquivos (load e dump)
Usado quando você quer salvar ou ler um arquivo .json no disco
"""

import json
from pathlib import Path

dados = {"nome": "Guido", "id": 123, "ativo": True}
caminho = Path("usuario.json")

# SALVAR (dump)
with open(caminho, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4) # indent=4 deixa o arquivo legível para humanos

# LER (load)
with open(caminho, "r", encoding="utf-8") as f:
    dados_lidos = json.load(f)
    
    
"""
2. Manipulando Strings (loads e dumps)
Muito comum quando você recebe dados de uma API (web) ou quer transformar um dicionário em texto para enviar para algum lugar.
"""

import json

# Transformar DICIONÁRIO em STRING (dumps - "dump string")
dicionario = {"status": 200, "msg": "Sucesso"}
texto_json = json.dumps(dicionario) 

# Transformar STRING em DICIONÁRIO (loads - "load string")
json_recebido = '{"produto": "Teclado", "preco": 150.50}'
dados_dict = json.loads(json_recebido)

print(dados_dict["produto"]) # Teclado


"""
O que mais você precisa saber?
"""

"""
A. O parâmetro indent e sort_keys
Se você salvar um JSON sem o indent, ele vira uma linha única e gigante (difícil de ler).
"""

# Gera um JSON organizado e com as chaves em ordem alfabética
json_bonito = json.dumps(dados, indent=4, sort_keys=True)


"""
B. Caracteres Especiais (Acentos)
Por padrão, o Python tenta converter acentos para códigos Unicode (ex: á vira \u00e1). Para manter os acentos normais no arquivo:
"""

json.dump(dados, f, ensure_ascii=False)


"""
C. O Problema das Datas
O JSON não entende objetos de data do Python (datetime). Se tentar salvar, vai dar erro.
"""

# Solução simples: Converta a data para string antes de salvar (str(data_hoje))