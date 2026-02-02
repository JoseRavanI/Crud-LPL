personagens = []


def criar_personagem():
    nome = input("Nome do personagem: ")
    forca = int(input("Força: "))
    defesa = int(input("Defesa: "))
    vida = int(input("Vida: "))

    personagem = {
        "nome": nome,
        "forca": forca,
        "defesa": defesa,
        "vida": vida
    }

    personagens.append(personagem)
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
        elif escolha == "2":
            nova_forca = input(f"Nova força [{personagem['forca']}]: ")
            if nova_forca.isdigit():
                personagem["forca"] = int(nova_forca)
        elif escolha == "3":
            nova_defesa = input(f"Nova defesa [{personagem['defesa']}]: ")
            if nova_defesa.isdigit():
                personagem["defesa"] = int(nova_defesa)
        elif escolha == "4":
            nova_vida = input(f"Nova vida [{personagem['vida']}]: ")
            if nova_vida.isdigit():
                personagem["vida"] = int(nova_vida)
        elif escolha == "0":
            print("Personagem atualizado!")
            break
        else:
            print("Opção inválida.")


def deletar_personagem():
    listar_personagens()
    entrada = input("Digite o índice do personagem: (se quiser sair clique em qualquer letra) ")
    if not entrada.isdigit():
        print("Por favor, digite um número válido.")
        return
    indice = int(entrada)
    if indice < 0 or indice >= len(personagens):
        print("Índice inválido")
        return
    personagens.pop(indice)
    print("Personagem removido!")


def calcular_poder(personagem):
    return personagem["forca"] * 2 + personagem["defesa"] + personagem["vida"]


def comparar_personagens():
    listar_personagens()

    i1 = int(input("Índice do primeiro personagem: "))
    i2 = int(input("Índice do segundo personagem: "))

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