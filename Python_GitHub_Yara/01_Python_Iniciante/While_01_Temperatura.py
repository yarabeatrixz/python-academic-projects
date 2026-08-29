while True:
    c = int(input("digite a temperatura em graus Celsius: "))
    k = c + 273.15
    f = c * 1.8 + 32
    if c <= -5:
        break
    print(f"o valor em Kelvin é igual: {k}")
    print(f"o valor em Fahrenheit é igual: {f}")
