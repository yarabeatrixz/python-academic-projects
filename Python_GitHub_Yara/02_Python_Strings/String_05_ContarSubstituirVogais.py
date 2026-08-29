cont_vogais = 0
palavra = input("Digite seu nome: ")
lista = []

for letra in palavra:
    lista.append(letra)
    if letra.lower() in "aeiou":
        cont_vogais += 1

print(cont_vogais)

while True:
    caracter = input("Digite um caracter (vogal ou consoante): ")
    if len(caracter) == 1 and caracter.isalpha():
        palavra_caracter = caracter * len(palavra)
        print(palavra_caracter)
        break
    else:
        print("Digite um caracter válido.")
