import random
cont = 0
computador = random.randint(0,10)
while True:
    tentativas = int(input("Digite um número entre 1 e 10: "))
    if tentativas == computador:
        break
    if tentativas != computador:
        cont += 1
        print("Você errou!")
print(f"Você acertou! O total de tentativas foi {cont + 1}!")
