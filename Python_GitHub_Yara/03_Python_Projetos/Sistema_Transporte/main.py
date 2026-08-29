# =========================================================
# Projeto: Express Log - Sistema de Entregas (CRUD)
# Autoras: Yara Beatriz Silva Santos
# UMC - Universidade de Mogi das Cruzes
# =========================================================

import os
import pacotes  # Importando o módulo pacotes (todos os procedimentos de entrega)

def menu():  # Função para exibir o menu principal
    print("\033[44m\n\nSistema de Entregas\033[m")
    print("1. Cadastro de Entrega")
    print("2. Alterar")
    print("3. Consultar")
    print("4. Excluir")
    print("5. Sair")

def executar(comando):  # Função para executar o comando selecionado
    if comando == 1:
        pacotes.cadastrar_entrega()
    elif comando == 2:
        pacotes.alterar_entrega()
    elif comando == 3:
        pacotes.consultar_entrega()
    elif comando == 4:
        pacotes.excluir_entrega()
    elif comando == 5:
        print("\n\033[1;31mEncerrando o sistema.\033[m")
    else:
        print("Opção inválida. Tente novamente.")

comando = 0
while (comando != 5):
    os.system('cls')  # Limpa a tela no Windows
    menu()  # Exibe o menu
    try:
        comando = int(input("Escolha uma opção: ").strip())
    except ValueError:
        print("Digite um número válido.")
        input("Pressione Enter para continuar...")
        continue
    executar(comando)
    if comando != 5:
        input("\nPressione qualquer tecla para continuar...\n")
