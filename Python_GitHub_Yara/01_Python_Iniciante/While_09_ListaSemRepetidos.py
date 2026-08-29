lista = list()
for c in range(0,15):
    n = int(input("digite um número: "))
    if n not in lista:
        lista.append(n)

print(lista)
