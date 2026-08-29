y = h = acima = abaixo = 0
while True:
    n = int(input("digite um número: "))
    if n == 100:
        break
    if n > 80:
        acima += 1
    else:
        if n < 10:
            abaixo +=1
    y +=1
    h += n
    media = h / y
print(f"a média dos valores foi igual a: {media}")
print(f"a quantidade de números acima de 80 foi igual: {acima} ")
print(f"a quantidade de números abaixo de 10 foi igual: {abaixo} ")
