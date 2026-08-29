z = 1
while True:
    n = int(input("digite um número: "))
    while n <= 2:
        n = int(input("digite outro número: "))
    while z < n:
        z += 1
        print('quadrado=', z * z)

        print('cubo =', z * z * z)
