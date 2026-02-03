import json
import os

ARQUIVO_JSON = "personagens.json"

def carregar_personagens():
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_personagens():
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(personagens, f, ensure_ascii=False, indent=2)

personagens = carregar_personagens()

def criar_personagem():
    while True:
        nome = input("Nome do personagem: ")
        if nome:
            break
        print("Nome não pode estar vazio.")
    
    while True:
        entrada_forca = input("Força: ")
        if entrada_forca.isdigit():
            forca = int(entrada_forca)
            break
        print("Força deve ser um número válido.")
    
    while True:
        entrada_defesa = input("Defesa: ")
        if entrada_defesa.isdigit():
            defesa = int(entrada_defesa)
            break
        print("Defesa deve ser um número válido.")
    
    while True:
        entrada_vida = input("Vida: ")
        if entrada_vida.isdigit():
            vida = int(entrada_vida)
            break
        print("Vida deve ser um número válido.")

    personagem = {
        "nome": nome,
        "forca": forca,
        "defesa": defesa,
        "vida": vida
    }

    personagens.append(personagem)
    salvar_personagens()
    print("Personagem criado com sucesso!")


def listar_personagens():
    if not personagens:
        print("Nenhum personagem cadastrado.")
        return

    for i, p in enumerate(personagens):
        print(f"""
        [{i}]
        Nome: {p['nome']}
        Força: {p['forca']}
        Defesa: {p['defesa']}
        Vida: {p['vida']}
        """)



def atualizar_personagem():
    listar_personagens()
    entrada = input("Digite o índice do personagem: ")
    if not entrada.isdigit():
        print("Por favor, digite um número válido.")
        return
    indice = int(entrada)
    if indice < 0 or indice >= len(personagens):
        print("Índice inválido")
        return
    personagem = personagens[indice]
    alterado = False
    while True:
        print("\nQual atributo deseja mudar?")
        print("1 - Nome")
        print("2 - Força")
        print("3 - Defesa")
        print("4 - Vida")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            novo_nome = input(f"Novo nome [{personagem['nome']}]: ")
            if novo_nome:
                personagem["nome"] = novo_nome
                alterado = True
        elif escolha == "2":
            nova_forca = input(f"Nova força [{personagem['forca']}]: ")
            if nova_forca.isdigit():
                personagem["forca"] = int(nova_forca)
                alterado = True
        elif escolha == "3":
            nova_defesa = input(f"Nova defesa [{personagem['defesa']}]: ")
            if nova_defesa.isdigit():
                personagem["defesa"] = int(nova_defesa)
                alterado = True
        elif escolha == "4":
            nova_vida = input(f"Nova vida [{personagem['vida']}]: ")
            if nova_vida.isdigit():
                personagem["vida"] = int(nova_vida)
                alterado = True
        elif escolha == "0":
            if alterado:
                salvar_personagens()
            print("Personagem atualizado!")
            break
        else:
            print("Opção inválida.")


def deletar_personagem():
    listar_personagens()
    entrada = input("Digite o índice do personagem: ")
    if not entrada.isdigit():
        print("Por favor, digite um número válido.")
        return
    indice = int(entrada)
    if indice < 0 or indice >= len(personagens):
        print("Índice inválido")
        return
    personagens.pop(indice)
    salvar_personagens()
    print("Personagem removido!")


def calcular_poder(personagem):
    return personagem["forca"] * 2 + personagem["defesa"] + personagem["vida"]


def comparar_personagens():
    if not personagens:
        print("Nenhum personagem cadastrado.")
        return
    
    listar_personagens()

    while True:
        entrada_i1 = input("Índice do primeiro personagem: ")
        if entrada_i1.isdigit():
            i1 = int(entrada_i1)
            if 0 <= i1 < len(personagens):
                break
            print("Índice inválido.")
        else:
            print("Por favor, digite um número válido.")
    
    while True:
        entrada_i2 = input("Índice do segundo personagem: ")
        if entrada_i2.isdigit():
            i2 = int(entrada_i2)
            if 0 <= i2 < len(personagens):
                break
            print("Índice inválido.")
        else:
            print("Por favor, digite um número válido.")
    
    if i1 == i2:
        print("Escolha personagens diferentes.")
        return

    p1 = personagens[i1]
    p2 = personagens[i2]

    poder1 = calcular_poder(p1)
    poder2 = calcular_poder(p2)

    print(f"\nBATALHA")
    print(f"{p1['nome']} (Poder: {poder1}) VS {p2['nome']} (Poder: {poder2})")

    if poder1 > poder2:
        print(f"{p1['nome']} venceu!")
    elif poder2 > poder1:
        print(f"{p2['nome']} venceu!")
    else:
        print("Empate!")


def menu():
    while True:
        print("""
=== CRUD RPG ===
1 - Criar personagem
2 - Listar personagens
3 - Atualizar personagem
4 - Deletar personagem
5 - Comparar personagens
0 - Sair
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_personagem()
        elif opcao == "2":
            listar_personagens()
        elif opcao == "3":
            atualizar_personagem()
        elif opcao == "4":
            deletar_personagem()
        elif opcao == "5":
            comparar_personagens()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida")


menu()