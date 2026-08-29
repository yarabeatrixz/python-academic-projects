y = z= 0
while True:
    n = int(input("digite um número: "))
    if n == 0:
        break
    y += n
    z += 1
    m = y / z
print (f"A soma é igual a : {y} ")
print (f"A média é igual a : {m} ")
