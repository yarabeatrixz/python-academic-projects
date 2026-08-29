string = str(input("Digite uma string: "))
for letra in string:
    if letra.lower() not in "aeiou":
        print(letra, end = "")
