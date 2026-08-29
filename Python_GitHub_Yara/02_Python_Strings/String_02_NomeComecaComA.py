nome = str(input("Digite um nome: "))
lista = []
for letra in nome:
    lista.append(letra)
if lista[0] == "a" or lista[0] == "A":
    for letra in lista:
        print(letra,end='')
else:
    print("o nome não começa com 'a'")
