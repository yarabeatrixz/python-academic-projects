string = str(input("Digite uma string: "))
string_invertida = string[::-1]
if string_invertida == string:
    print("A string é um palíndromo")
else:
    print("A string não é um palíndromo")
