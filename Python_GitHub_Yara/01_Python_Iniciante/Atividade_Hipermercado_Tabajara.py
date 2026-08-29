# Autor(a): Yara Beatriz Silva Santos

# Biblioteca importada
import math

# Título
print("\n\n*** Programa: Cálculo de promoção do Hipermercado Tabajara  ***")

# Entradas
print("1- Filé Duplo\n2- Alcatra\n3- Picanha\n")
tipo_de_carne = int(input("Digite o número correspondente ao tipo de carne escolhido do menu: "))
quantidade_de_carne = float(input("Digite a quantidade de carne comprada em Kg:  "))
print("1 - Sim, no cartão\n4 - Não")
forma_de_pagamento = int(input("A compra será efetuada no cartão Tabajara?  "))

# Processamentos
if tipo_de_carne == 1:
    nome = "File Duplo"
    if quantidade_de_carne <= 5:
        preco = quantidade_de_carne * 4.90
    else:
        preco = quantidade_de_carne * 5.80
elif tipo_de_carne == 2:
    nome = "Alcatra"
    if quantidade_de_carne <= 5:
        preco = quantidade_de_carne * 5.90
    else:
        preco = quantidade_de_carne * 6.80
elif tipo_de_carne == 3:
    nome = "Picanha"
    if quantidade_de_carne <= 5:

        preco = quantidade_de_carne * 6.90
    else:
        preco = quantidade_de_carne * 7.80

if forma_de_pagamento == 3:
    resposta = "Sim"
    desconto = preco * 0.05
    total = preco - desconto
else:
    resposta = "Não"
    desconto = 0
    total = preco - desconto
valor_arredondado = math.ceil(total)

# Saídas
print("\n--- CUPOM FISCAL---")
print(f"Tipo de Carne: {nome}")
print(f"Quantidade: {quantidade_de_carne} KG")
print(f"Preço total: R$ {preco}")
print(f"Pagamento no cartão Tabajara? {resposta}")
print(f"Desconto: R$ {desconto}")
print(f"Valor a pagar arredondado: R$ {valor_arredondado:.2f}")
