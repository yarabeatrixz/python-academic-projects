# Programa: Cálculo de Hospedagem em Hotel
# Autor(a): Yara Beatriz Silva Santos

# Título
print("\n\n*** Programa: Cálculo de Hospedagem em Hotel ***")

# Entradas
nome_hospede = input("Digite o seu nome: ")
print("1-Tipo apto A (R$ 85.00)\n2-Tipo apto B (R$ 170.00)\n3-Tipo apto C (R$ 255.00)\n4-Tipo apto D (R$ 340.00)\n")
tipo_apartamento = int(input("Digite o tipo de apartamento escolhido: "))
numero_diarias_utilizados = int(input("Digite o número de diária utilizadas: "))
valor_consumo_interno = int(input("Digite o valor do consumo interno: "))

# Processamento
if tipo_apartamento == 1:
    nome = "Tipo apto A"
    valor_diaria = 85.00
    valor_total_diaria = valor_diaria * numero_diarias_utilizados

elif tipo_apartamento == 2:
    nome = "Tipo apto B"
    valor_diaria = 170.00
    valor_total_diaria = valor_diaria * numero_diarias_utilizados

elif tipo_apartamento == 3:
    nome = "Tipo apto C"
    valor_diaria = 255.00
    valor_total_diaria = valor_diaria * numero_diarias_utilizados

elif tipo_apartamento == 4:
    nome = "Tipo apto D"
    valor_diaria = 340.00

valor_total_diaria = valor_diaria * numero_diarias_utilizados
subtotal = valor_total_diaria + valor_consumo_interno
taxa_servico = subtotal * 0.10
total_geral_hospedagem = subtotal + taxa_servico

# Saídas
print("\n--- CUSTO HOSPEDAGEM ---")
print(f"Nome: {nome_hospede}")
print(f"Tipo de apartamento escolhido: {tipo_apartamento}-{nome}")
print(f"Número de diária utilizadas: {numero_diarias_utilizados}")
print(f"Valor da diária por tipo de quarto: {valor_diaria}")
print(f"Valor do consumo interno: R$ {valor_consumo_interno}")
print(f"Valor subtotal: R$ {subtotal}")
print(f"Valor da taxa de serviço: R$ {taxa_servico}")
print(f"Valor total geral da hospedagem: R$ {total_geral_hospedagem}")
