"""
Biblioteca csv
Arquivos CSV (Comma Separated Values) são a base de quase tudo que envolve dados e planilhas (Excel). Em Python, a gente trata eles basicamente como listas ou dicionários.
"""


"""
1. Lendo um CSV (como Dicionário)
Esta é a forma mais prática, porque você acessa os dados pelo nome da coluna.
"""

import csv
from pathlib import Path

caminho = Path("produtos.csv")

with open(caminho, "r", encoding="utf-8") as f:
    # DictReader transforma cada linha em um dicionário
    leitor = csv.DictReader(f)
    
    for linha in leitor:
        print(f"Produto: {linha['nome']} - Preço: {linha['preco']}")

        
"""
2. Escrevendo um CSV
Para salvar dados de forma organizada.
"""

import csv
from pathlib import Path

cabecalho = ["nome", "pontuacao"]
dados = [
    {"nome": "Alice", "pontuacao": 95},
    {"nome": "Bob", "pontuacao": 87}
]

caminho = Path("ranking.csv")

with open(caminho, "w", encoding="utf-8", newline="") as f:
    escritor = csv.DictWriter(f, fieldnames=cabecalho)
    
    escritor.writeheader() # Escreve o nome das colunas
    escritor.writerows(dados) # Escreve todas as linhas de uma vez
    

"""
O detalhe que todo mundo esquece: newline=""
Sempre que for escrever um CSV em Python, use newline="" dentro do open(). Sem isso, o Windows costuma pular uma linha em branco entre cada linha de dados, estragando sua planilha
"""