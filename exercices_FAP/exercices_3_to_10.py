""" 3. Escreva um programa que leia um número inteiro e informe o seu antecessor e o seu sucessor. """

"""
numero = int(input("Escreva um número inteiro:"))
antecessor = numero - 1
sucessor = numero + 1

print(f"Número: {numero}; Antecessor: {antecessor}; Sucessor: {sucessor}")
"""

# --------------------------------------------------------

"""4. Escreva um programa que leia os valores de dois ângulos internos de um triângulo e calcule o valor do terceiro ângulo."""

"""
primeiro_angulo = int(input("Escreva o valor do primeiro ângulo:"))
segundo_angulo = int(input("Escreva o valor do segundo ângulo:"))

terceiro_angulo = 180 - (primeiro_angulo + segundo_angulo)
print(f"O valor do terceiro ângulo é: {terceiro_angulo}")
"""
# --------------------------------------------------------

"""5. Escreva um programa que leia um valor em real, a cotação atual do dólar e calcule o valor informado pelo usuário em
dólares"""

"""
valor_reais = int(input("Escreva um valor em reais"))
cotacao_dolar = float(input("Escreva o valor da cotação atual do dólar"))

valor_dolares = valor_reais * cotacao_dolar

print(f"Valor em reais: {valor_reais}; Valor em dólares: {valor_dolares}")
"""

# --------------------------------------------------------


"""6. Escreva um programa que leia um valor em KB e calcule o seu valor correspondente em bits, bytes, MB e GB."""

"""
valor_kb = int(input("Escreva um valor em KB:"))

valor_bytes = valor_kb * 1000
valor_bits = valor_bytes * 8
valor_Mb = valor_bytes * 0.001
valor_Gb = valor_bytes * 0.000001

print(f"Valor kb: {valor_kb}; Valor bytes: {valor_bytes}; Valor bits: {valor_bits}; Valor Mb: {valor_Mb}; Valor Gb: {valor_Gb}")
"""
# --------------------------------------------------------

"""7. Escreva um programa que leia uma palavra e um número inteiro k e identifique a k-ésima letra da palavra informada
pelo usuário"""

"""
palavra = input("Escreva uma palavra:")
indice = int(input("Escreva o número relacionado a letra da palavra que quer encontrar:"))
letra = palavra[indice-1]

print(f"Palavra: {palavra}; Letra: {letra}")
"""

# --------------------------------------------------------
"""8. Escreva um programa que leia uma letra minúscula e imprima a sua letra maiúscula correspondente"""

"""
letra = input("Escreva uma letra qualquer:")
maiuscula = letra.upper()
print(f"Letra: {letra}; Letra convertida: {maiuscula}")
"""

# --------------------------------------------------------
"""9. Escreva um programa que leia um número inteiro N e imprima dos 10 primeiros elementos da sua tabuada. A saída do
programa deve seguir o formato abaixo, que mostra os 5 primeiros elementos da tabuada do 2"""

"""
numero = int(input("Escreva um número inteiro:"))
inicio = int(input("Por qual valor deseja iniciar a contagem da tabuada?"))
fim = int(input("Por qual valor deseja terminar a contagem da tabuada?")) + 1
print(f"Tabuada do {inicio} ao {fim} de: {numero}")

for i in range(inicio, fim):
    resultado = numero * i
    print(f"{numero} x {i}: {resultado}")
"""

"""
numero = int(input("Escreva um número inteiro:"))

tabuada_2 = numero * 2
tabuada_3 = numero * 3
tabuada_4 = numero * 4
tabuada_5 = numero * 5
tabuada_6 = numero * 6
tabuada_7 = numero * 7
tabuada_8 = numero * 8
tabuada_9 = numero * 9
tabuada_10 = numero * 10

print(f"Número: {numero}")
print(f"{numero} * 2: {tabuada_2}")
print(f"{numero} * 3: {tabuada_3}")
print(f"{numero} * 4: {tabuada_4}")
print(f"{numero} * 5: {tabuada_5}")
print(f"{numero} * 6: {tabuada_6}")
print(f"{numero} * 7: {tabuada_7}")
print(f"{numero} * 8: {tabuada_8}")
print(f"{numero} * 9: {tabuada_9}")
print(f"{numero} * 10: {tabuada_10}")
"""

# --------------------------------------------------------
"""10. Escreva um programa que leia a quantidade de horas trabalhadas por um funcionário de uma empresa durante um mês
e o valor de cada hora trabalhada e determine o seu pagamento. O programa deve considerar que a carga-horária
mensal do funcionário é de 160 horas e que o valor de cada hora extra corresponde ao valor da hora trabalhada
acrescido de uma taxa de 50%. Para resolver a questão, considere que a quantidade de horas trabalhadas nunca será
inferior a 160"""

"""
horas_diarias = int(input("Escreva o número de horas trabalhadas por dia:"))
dias_trabalhados = int(input("Escreva o número de dias trabalhados no mês:"))
valor_hora = int(input("Escreva o valor recebido por hora:"))
valor_hora_extra = valor_hora + valor_hora * 0.5

horas_mes = horas_diarias * dias_trabalhados
horas_extras = horas_mes - 160 if horas_mes > 160 else 0

if horas_mes > 160:
    pagamento_normal = 160 * valor_hora
    pagamento_horas_extras = horas_extras * valor_hora_extra
    pagamento = pagamento_normal + pagamento_horas_extras
    print(f"Horas trabalhadas no mês: {horas_mes}; O valor do pagamento é de: {pagamento:.2f} reais")
else:
    pagamento = horas_mes * valor_hora
    print(f"Horas trabalhadas no mês: {horas_mes}; O valor do pagamento é de: {pagamento:.2f} reais")
"""

# --------------------------------------------------------
"""11. Um banco está realizando uma grande promoção em seus financiamentos. Ele financia qualquer valor em 5 prestações.
O valor da primeira prestação corresponde à 20% do valor do empréstimo. Os valores das demais prestações
correspondem ao valor da parcela anterior acrescido de uma taxa de juros de 7%. Com base nestas informações,
escreva um programa que leia o valor a ser financiado por um cliente e calcule: o valor de cada prestação, o valor total
que o cliente vai pagar pelo empréstimo e o total de juros que o cliente vai pagar pelo empréstimo"""

"""
valor_financiado = int(input("Escreva o valor a ser financiado:"))

primeira_prestacao = valor_financiado * 0.2
proximas_prestacoes = primeira_prestacao + primeira_prestacao * 0.07

valor_total = primeira_prestacao + proximas_prestacoes * 4
total_juros = valor_total - valor_financiado

print(f"Valor financiado: {valor_financiado}; Primeira prestação: {primeira_prestacao}; Valor da 2° a 5° prestações: {proximas_prestacoes}; Valor do total a ser pago: {valor_total}; Valor dos juros: {total_juros}")
"""

# --------------------------------------------------------
"""12. Uma revendedora de veículos resolveu fazer uma promoção em seus veículos. Nesta revendedora, o preço de um
veículo é calculado através do seu preço de compra, mais uma taxa de 20% de IPI, 17% de ICMS e uma margem de lucro
de 20%. Nesta promoção, a revendedora resolveu tirar o valor do IPI. Com base nestas informações, escreva um
programa que leia o preço atual de um veículo e calcule qual deve ser o seu preço na promoção"""

"""
preco_de_compra = int(input("Escreva o valor do preço de compra do carro:"))
taxa_ipi = preco_de_compra * 0.2
taxa_icms = preco_de_compra * 0.17
margem_de_lucro = preco_de_compra * 0.2

valor_atual = preco_de_compra + taxa_ipi + taxa_icms + margem_de_lucro
valor_promocao = valor_atual - taxa_ipi

print(f"Valor de compra: {preco_de_compra}; Valor atual: {valor_atual}; Valor na promoção: {valor_promocao}")
"""

# --------------------------------------------------------
"""13. Um provedor de internet oferece um plano promocional para os seus clientes. Neste plano, ele paga uma mensalidade
de R$ 80,00 e pode acessar até 100 GB de dados. Caso a quantidade de dados acessados seja superior a este limite, ele
deve pagar uma taxa adicional de R$ 5,00 por cada GB extra acessado. Com base nestas informações, escreva um
programa que leia a quantidade de dados acessados pelo cliente durante um mês (em GB) e calcule o valor da sua
conta, considerando que esta quantidade nunca é inferior a 100 GB."""

"""
dados_acessados_mes = int(input("Digite o a quantidade de dados acessados no mês, em GB:"))

valor_mensalidade = 80
dados_excedentes = dados_acessados_mes - 100 if dados_acessados_mes > 100 else 0

if dados_acessados_mes > 100:
    valor_a_pagar = valor_mensalidade + dados_excedentes * 5
    print(f"Valor a ser pago: {valor_a_pagar:.2f} reais")
else:
    print(f"Valor a ser pago: {valor_mensalidade:.2f} reais")
"""

# --------------------------------------------------------
"""14. Lázaro está muito feliz por ter enfim conseguido construir a sua casa própria. Sabendo-se que a construção durou 180
dias de trabalho, escreva um programa que leia o número de pedreiros que trabalhavam na obra, o número de
ajudantes e o valor da diária do pedreiro e calcule o gasto de Lázaro com a mão de obra. Para resolver este programa,
considere que todos os pedreiros e ajudantes trabalharam todos os dias da obra e que o valor da diária de cada
ajudante corresponde à metade do valor da diária do pedreiro."""

"""
dias_da_construcao = 180

pedreiros = int(input("Escreva o número de pedreiros que trabalharam na obra:"))
ajudantes = int(input("Escreva o número de ajudantes que trabalharam na obra:"))
valor_diaria_pedreiro = int(input("Escreva o valor da diária de cada pedreiro:"))
valor_diaria_ajudante = valor_diaria_pedreiro * 0.5

valor_pedreiros = dias_da_construcao * valor_diaria_pedreiro * pedreiros
valor_ajudantes = dias_da_construcao * valor_diaria_ajudante * ajudantes
valor_total = valor_ajudantes + valor_pedreiros

print(f"Lázaro gastou {valor_pedreiros} para pagar os pedreiros, {valor_ajudantes} para pagar os ajudantes e no total {valor_total} para pagar todos.")
"""

# --------------------------------------------------------
"""15. Escreva um programa que leia o valor de uma passagem em reais e em milhas e, em seguida, leia o valor da passagem
(em reais) que Caio deseja comprar e calcule quantas milhas ele precisa juntar para que ele não precise pagar pela
passagem. Para resolver este programa, considere que a proporção entre o valor da milha e o valor em reais é o mesmo
para todos os voos da companhia aérea."""

"""
valor_passagem = int(input("Escreva o valor da passagem:"))
valor_milhas = int(input("Escreva o valor da passagem em milhas:"))
valor_passagem_caio = int(input("Escreva o valor da passagem do Caio:"))

conversao_valor_milhas = valor_milhas / valor_passagem
valor_passagem_caio_em_milhas = valor_passagem_caio * conversao_valor_milhas 

print(f"O valor da passagem do Caio é: {valor_passagem_caio}; Ele deve percorrer: {valor_passagem_caio_em_milhas} milhas para não precisar pagar pela passagem.")
"""