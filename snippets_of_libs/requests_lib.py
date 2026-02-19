"""
Biblioteca requests
Para usar, primeiro você precisa instalar (pip install requests).
"""

"""
1. O básico: GET (Igual ao fetch)
Usado para buscar informações.
"""

import requests

url = "https://api.exemplo.com/usuarios"
resposta = requests.get(url)

# Verificar se a requisição deu certo (Status 200)
if resposta.status_code == 200:
    # Transformar o JSON recebido em um Dicionário Python
    dados = resposta.json()
    print(dados)
else:
    print(f"Erro: {resposta.status_code}")
    

"""
2. Enviando dados: POST
Usado para criar algo novo no servidor.
"""

novo_usuario = {"nome": "Dev Python", "email": "python@teste.com"}

# Enviando o dicionário como JSON
resposta = requests.post(url, json=novo_usuario)

print(resposta.status_code) # Geralmente 201 para 'Criado'


"""
3. Passando Parâmetros e Headers
Muitas APIs exigem uma Chave de API (Token) para segurança ou parâmetros de busca.
"""

url_clima = "https://api.clima.com/v1"
meus_parametros = {"cidade": "Sao Paulo", "unidade": "metrica"}
meus_headers = {"Authorization": "Bearer SEU_TOKEN_AQUI"}

resposta = requests.get(url_clima, params=meus_parametros, headers=meus_headers)