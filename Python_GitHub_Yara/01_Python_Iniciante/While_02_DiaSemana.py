while True:
    n = int(input("digite um número: "))
    if n > 7:
        break
    if n < 1:
        break
    if n == 1:
        print("Domingo")
    elif n == 2:
        print("Segunda")
    elif n == 3:
        print("Terça")
    elif n == 4:
        print("Quarta")
    elif n == 5:
        print("Quinta")
    elif n == 6:
        print("Sexta")
    elif n == 7:
        print("Sábado")
print("Valor inválido")
