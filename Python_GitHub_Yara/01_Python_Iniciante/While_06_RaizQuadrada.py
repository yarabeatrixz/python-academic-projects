import math
n = int(input("digite um número: "))
while n < 10:
    n = int(input("Entrada inválida! digite outro número: "))
while n > 15:
    n = int(input("Entrada inválida! digite outro número: "))
quadrado = math.sqrt(n)
print(quadrado)
