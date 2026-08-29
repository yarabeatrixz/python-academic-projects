lista = list()
while True:
    n = int(input("digite um número: "))
    if n % 2 == 0:
        lista.append(n)
    if n == 1:
        break
print(lista)
