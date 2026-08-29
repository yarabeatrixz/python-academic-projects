lista = []
for c in range(0,25):
    n = lista.append(float(input("digite um número: ")))
x = int(input("digite um número que será a posição na lista: "))
y = int(input("digite outro número que será a posição na lista: "))
while lista[x] not in lista:
    x = int(input("digite um número que será a posição na lista: "))
while lista[y] not in lista:
    y = int(input("digite outro número que será a posição na lista: "))
soma = lista[x] + lista[y]
print(f"a soma é {soma}")
