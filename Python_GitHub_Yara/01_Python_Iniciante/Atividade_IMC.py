# Programa de Cálculo - Índice de Massa Corporal (IMC)
# Apresente o IMC e classifique de acordo com a tabela
# Autor(a): Yara Beatriz Silva Santos


# Variável para armazenar a escolha do usuário em continuar o programa
escolha = ""

# Laço Principal - looping utilizado para manter o programa até a escolha de sair do usuário
while (True):

    escolha = ""                    # Reseta a escolha armazenada a cada repetição
    print("\n\n Programa de Cálculo - Índice de Massa Corporal (IMC)")  # Título
    nome = input("Digite seu nome : ")                            # Entrada
    idade = int(input("Digite sua idade: "))                      # Entrada
    peso = float(input("Digite seu peso (kg): "))                 # Entrada
    altura = float(input("Digite sua altura (m): "))               # Entrada

    imc = peso / ((altura) * (altura))          # Processamento - Cálculo do IMC

    # Avalia o valor do IMC e imprimi a categoria correspondente
    if (imc < 18.5):
        print(f"\nNome: {nome}, idade: {idade} anos. Seu Índice de Massa Corporal (IMC) é {imc:.2f} e você está abaixo do peso")
    else:
        if (18.5 <= imc <= 24.9):
            print(f"\nNome: {nome}, idade: {idade} anos. Seu Índice de Massa Corporal (IMC) é {imc:.2f} e você está com peso normal")
        else:
            if (25 <= imc <= 29.9):
                print(f"\nNome: {nome}, idade: {idade} anos. Seu Índice de Massa Corporal (IMC) é {imc:.2f} e você está com sobrepeso")
            else:
                if (30 <= imc <= 34.9):
                    print(f"\nNome: {nome}, idade: {idade} anos. Seu Índice de Massa Corporal (IMC) é {imc:.2f} e você está com obesidade grau 1")
                else:
                    if (35 <= imc <= 39.9):
                        print(f"\nNome: {nome}, idade: {idade} anos. Seu Índice de Massa Corporal (IMC) é {imc:.2f} e você está com obesidade grau 2")
                    else:
                        if (imc >= 40):
                            print(f"\nNome: {nome}, idade: {idade} anos. Seu Índice de Massa Corporal (IMC) é {imc:.2f} e você está com obesidade grau 3")

    # Laço secundário - looping para validar a resposta do usuário em continuar ou sair
    # Lower - utilizado para converte a string digitada em letras minúsculas
    # Strip - utilizado para remover espaços vazios
    while not ((escolha == "n") or (escolha == "não") or (escolha == "s") or (escolha == "sim")):
        escolha = input("\n\n Deseja executar o cálculo novamente? (s)im ou (n)ão?").lower().strip()

    # Avalia se a escolha do usuário foi "n" ou "não" e exibe a mensagem de encerramento
    if ((escolha == "n") or (escolha == "não")):
        print("\n Cálculo encerrado!")
        break                                       # Encerra o programa

    else:
        print("\n Cálculo continua...")
