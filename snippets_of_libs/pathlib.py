"""
🛠️ Snippets Essenciais: pathlib
"""

"""
1. Importação e Criação de Caminhos
O objeto principal é o Path. Ele identifica automaticamente se você está no Windows ou Linux/Mac e ajusta as barras (/ ou \).
"""

from pathlib import Path

# Criar um objeto de caminho (não cria a pasta no PC ainda, apenas o objeto)
caminho = Path("projeto") / "dados" / "relatorio.txt"

print(caminho) 
# No Windows: projeto\dados\relatorio.txt
# No Linux: projeto/dados/relatorio.txt


"""
2. Navegação e Localização
Útil para saber onde seu script está rodando ou acessar a pasta do usuário.
"""

# Onde estou agora? (Current Working Directory)
pasta_atual = Path.cwd()

# Onde está o arquivo do script?
pasta_do_script = Path(__file__).parent

# Pasta "Home" do usuário (ex: C:\Users\Voce)
home = Path.home()


"""
3. Decomposição de Caminhos (Atributos)
Imagine que você tem o caminho: /home/user/documentos/foto.png. Você pode "quebrar" ele facilmente:
"""
    
arquivo = Path("documentos/foto.png")

print(arquivo.name)      # "foto.png" (nome completo)
print(arquivo.stem)      # "foto" (nome sem extensão)
print(arquivo.suffix)    # ".png" (extensão)
print(arquivo.parent)    # "documentos" (pasta pai)


"""
4. Manipulação de Pastas e Arquivos
Comandos para verificar existência e criar estruturas.
"""

pasta = Path("nova_pasta")

# Criar pasta (parents=True cria as pastas intermediárias; exist_ok=True não dá erro se já existir)
pasta.mkdir(parents=True, exist_ok=True)

# Verificar se existe
if pasta.exists():
    print("A pasta existe!")

# Verificar se é arquivo ou pasta
print(pasta.is_file())
print(pasta.is_dir())


"""
5. Listando Conteúdo (Globbing)
Essa é uma das funções mais poderosas para o dia a dia, como listar todos os arquivos de um tipo.
"""

pasta_fotos = Path("Imagens")

# Listar todos os arquivos .jpg na pasta
for foto in pasta_fotos.glob("*.jpg"):
    print(foto.name)

# Listar tudo (incluindo subpastas) - recursivo
for item in pasta_fotos.rglob("*"):
    print(item)
    
    
"""
💡 Dica de Ouro
Evite usar open('arquivo.txt', 'r') com strings. Use o objeto Path:
"""

caminho = Path("notas.txt")
# Ler tudo de uma vez
conteudo = caminho.read_text(encoding="utf-8")
# Escrever
caminho.write_text("Novo conteúdo")


"""
Manipulação Avançada de Arquivos
"""

"""
1. Criar, Renomear e Mover (pathlib)
Você não precisa da os para isso. O próprio objeto Path tem esses métodos.
"""

from pathlib import Path

arquivo = Path("notas.txt")

# Criar um arquivo vazio (estilo 'touch' do Linux)
arquivo.touch()

# Renomear arquivo
arquivo.rename("notas_v2.txt")

# Mover arquivo (é o mesmo comando rename, mas mudando o caminho da pasta)
destino = Path("documentos") / "notas_v2.txt"
Path("notas_v2.txt").rename(destino)


"""
2. Copiar Arquivos e Pastas (shutil)
A pathlib curiosamente não tem um método nativo para copiar. Para isso, usamos a shutil (Shell Utilities).
"""

import shutil
from pathlib import Path

origem = Path("foto.png")
destino = Path("backup/foto_backup.png")

# Copiar arquivo (mantendo permissões)
shutil.copy(origem, destino)

# Copiar uma PASTA inteira com tudo dentro
shutil.copytree(Path("projeto"), Path("projeto_backup"))


"""
3. Deletar Arquivos e Pastas
Aqui é onde você deve ter cuidado.
"""

import shutil
from pathlib import Path

arquivo = Path("lixo.txt")
pasta = Path("pasta_velha")

# Deletar ARQUIVO
arquivo.unlink(missing_ok=True)  # missing_ok evita erro se o arquivo não existir

# Deletar PASTA VAZIA
pasta.rmdir()

# Deletar PASTA COM CONTEÚDO (Cuidado! Isso apaga tudo dentro)
shutil.rmtree("caminho_da_pasta")


"""
Quando usar a biblioteca os?
Hoje em dia, você usará os principalmente para interagir com variáveis de ambiente ou comandos do sistema operacional que não são estritamente caminhos de arquivos.
"""

import os

# Pegar uma variável de ambiente (ex: chave de API)
api_key = os.getenv("MINHA_API_KEY")

# Executar um comando no terminal
os.system("echo Ola Mundo")

# Listar arquivos (estilo antigo, retorna apenas strings, não objetos)
arquivos = os.listdir(".")