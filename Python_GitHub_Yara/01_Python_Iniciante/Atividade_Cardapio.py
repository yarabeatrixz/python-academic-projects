cod_pedido = [100, 101, 102, 103, 104, 105]
nome = ["Cachorro Quente", "Bauru simples", "Bauru com Ovo", "Hamburguer", "Cheeseburguer", "Refrigerante"]
valor = [3.50, 3.80, 4.50, 4.70, 5.30, 4.00]
lista_cliente = []
total = 0

print("\nCardápio:")
for i in range(len(cod_pedido)):
    print(f"{cod_pedido[i]} - {nome[i]} - R${valor[i]: }")

resposta = input("Deseja fazer um pedido? (sim/não): ")

while True:
    codigo = int(input("\nDigite o código do produto (ou 0 para sair): "))
    if codigo == 0:
        break
    elif codigo in cod_pedido:
        quantidade = int(input("Digite a quantidade: "))
        indice = cod_pedido.index(codigo)
        preco = valor[indice] * quantidade
        total += preco
        item = f"{quantidade}x {nome[indice]} - R${preco: }"
        lista_cliente.append(item)
        print("Item adicionado ao pedido.")
    else:
        print("Código inválido. Tente novamente.")

print("\nResumo do pedido:")
for item in lista_cliente:
    print(item)
    print(f"Total a pagar: R${total: }")
else:
    print("Obrigado! Volte sempre.")
