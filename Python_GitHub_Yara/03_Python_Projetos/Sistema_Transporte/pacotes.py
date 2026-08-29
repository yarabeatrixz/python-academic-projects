# =========================================================
# Projeto: Express Log - Sistema de Entregas (CRUD)
# Módulo: pacotes.py - regras de negócio das entregas
# Autoras: Yara Beatriz Silva Santos e Laura Duarte da Silva
# UMC - Universidade de Mogi das Cruzes
# =========================================================

motoristas = [
    {"codigo": "M1", "nome": "Carlos Silva", "preco": 25.0, "prazo": "5 horas", "regiao": "Bairros de Mogi das Cruzes"},
    {"codigo": "M2", "nome": "Ana Costa", "preco": 60.0, "prazo": "24 horas", "regiao": "Cidades da Região Metropolitana de São Paulo"},
    {"codigo": "M3", "nome": "João Pereira", "preco": 120.0, "prazo": "7 dias", "regiao": "Estados do Brasil"}
]

pacotes_padrao = [
    {"codigo": "P1", "descricao": "Eletrônicos"},
    {"codigo": "P2", "descricao": "Itens frágeis"},
    {"codigo": "P3", "descricao": "Outro (item personalizado)"}
]

entregas = []

def mostrar_motoristas():
    print("\nMotoristas Disponíveis para Contratação\n")
    for m in motoristas:
        print(f"{m['codigo']} | {m['nome']} | Região: {m['regiao']} | Preço Base: R${m['preco']:.2f} | Prazo Base: {m['prazo']}")

def selecionar_motorista():
    while True:
        mostrar_motoristas()
        codigo = input("\nInforme o código do motorista desejado: ").strip().upper()
        for m in motoristas:
            if m["codigo"] == codigo:
                return m
        print("Código de motorista inválido. Por favor, tente novamente.")

def mostrar_pacotes():
    print("\nTipos de Pacotes Disponíveis\n")
    for p in pacotes_padrao:
        print(f"{p['codigo']} - {p['descricao']}")

def selecionar_pacote():
    while True:
        mostrar_pacotes()
        codigo = input("\nInforme o código do tipo de pacote: ").strip().upper()
        for p in pacotes_padrao:
            if p["codigo"] == codigo:
                return p
        print("Código de pacote inválido. Por favor, tente novamente.")

def cadastrar_entrega():
    print("\nCadastro de Nova Entrega\n")
    codigo = input("Informe o código identificador da entrega: ").strip()
    usuario = input("Nome completo do destinatário: ").strip()

    pacote = selecionar_pacote()

    origem = input("Informe o local de origem da entrega: ").strip()
    destino = input("Informe o local de destino da entrega: ").strip()
    trajeto = origem + " → " + destino

    motorista = selecionar_motorista()

    entrega = {
        "codigo": codigo,
        "usuario": usuario,
        "pacote": pacote["descricao"],
        "trajeto": trajeto,
        "motorista": motorista
    }
    entregas.append(entrega)
    print("\nEntrega cadastrada com sucesso!\n")

def alterar_entrega():
    print("\nAlteração de Entrega Cadastrada\n")
    codigo = input("Informe o código identificador da entrega que deseja alterar: ").strip()
    for entrega in entregas:
        if entrega["codigo"] == codigo:
            print("\nEntrega localizada com sucesso:")
            print(f"Código: {entrega['codigo']}")
            print(f"Destinatário: {entrega['usuario']}")
            print(f"Tipo de pacote: {entrega['pacote']}")

            if input("Deseja alterar o nome do destinatário? (S/N): ").strip().upper() == "S":
                entrega["usuario"] = input("Informe o novo nome do destinatário: ").strip()

            if input("Deseja alterar o tipo de pacote? (S/N): ").strip().upper() == "S":
                pacote = selecionar_pacote()
                entrega["pacote"] = pacote["descricao"]

            if input("Deseja alterar o trajeto da entrega? (S/N): ").strip().upper() == "S":
                origem = input("Informe o novo local de origem: ").strip()
                destino = input("Informe o novo local de destino: ").strip()
                entrega["trajeto"] = origem + " → " + destino

            if input("Deseja alterar o motorista responsável? (S/N): ").strip().upper() == "S":
                motorista = selecionar_motorista()
                entrega["motorista"] = motorista

            print("\nEntrega alterada com sucesso!\n")
            return
    print("Entrega não localizada. Verifique o código informado.")

def consultar_entrega():
    print("\nConsulta de Entrega\n")
    codigo = input("Informe o código identificador da entrega para consulta: ").strip()
    for entrega in entregas:
        if entrega["codigo"] == codigo:
            print("\nDetalhes da Entrega")
            print(f"Código: {entrega['codigo']}")
            print(f"Destinatário: {entrega['usuario']}")
            print(f"Tipo de pacote: {entrega['pacote']}")
            print(f"Trajeto: {entrega['trajeto']}")
            m = entrega["motorista"]
            print(f"Motorista responsável: {m['nome']} | Região de atendimento: {m['regiao']} | Preço Base: R${m['preco']:.2f} | Prazo Base: {m['prazo']}")
            return
    print("Entrega não localizada. Verifique o código informado.")

def excluir_entrega():
    print("\nExclusão de Entrega\n")
    codigo = input("Informe o código identificador da entrega que deseja excluir: ").strip()
    for i, entrega in enumerate(entregas):
        if entrega["codigo"] == codigo:
            print("\nEntrega localizada:")
            print(f"Código: {entrega['codigo']}")
            print(f"Destinatário: {entrega['usuario']}")
            print(f"Tipo de pacote: {entrega['pacote']}")
            print(f"Trajeto: {entrega['trajeto']}")
            m = entrega["motorista"]
            print(f"Motorista responsável: {m['nome']} | Região de atendimento: {m['regiao']} | Preço Base: R${m['preco']:.2f} | Prazo Base: {m['prazo']}")

            confirmacao = input("Confirma a exclusão desta entrega? (S/N): ").strip().upper()
            if confirmacao == "S":
                del entregas[i]
                print("\nEntrega excluída.\n")
            else:
                print("Exclusão cancelada.")
            return
    print("Entrega não localizada. Verifique o código informado.")
