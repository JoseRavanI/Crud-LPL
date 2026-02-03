import json
import os

ARQUIVO = "personagens.json"
personagens = []

def salvar():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(personagens, f, ensure_ascii=False, indent=2)

def carregar():
    global personagens
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            personagens = json.load(f)

def exibir():
    if not personagens:
        print("Vazio\n")
        return
    for i, p in enumerate(personagens):
        print(f"[{i}] {p['nome']} - F:{p['forca']} D:{p['defesa']} V:{p['vida']}")
    print()

def criar():
    nome = input("Nome: ")
    
    while True:
        try:
            forca = int(input("Força: "))
            break
        except ValueError:
            print("Digite um número válido.\n")
    
    while True:
        try:
            defesa = int(input("Defesa: "))
            break
        except ValueError:
            print("Digite um número válido.\n")
    
    while True:
        try:
            vida = int(input("Vida: "))
            break
        except ValueError:
            print("Digite um número válido.\n")
    
    personagens.append({"nome": nome, "forca": forca, "defesa": defesa, "vida": vida})
    salvar()
    print("OK\n")

def atualizar():
    exibir()
    
    while True:
        try:
            idx = int(input("Índice: "))
            break
        except ValueError:
            print("Digite um número válido.\n")
    
    if not existe(idx):
        print("Inválido\n")
        return
    
    p = personagens[idx]
    print(f"\n1-Nome 2-Força 3-Defesa 4-Vida 0-Sair")
    
    while True:
        op = input("Opção: ")
        if op == "1":
            p["nome"] = input("Novo nome: ")
            salvar()
        elif op == "2":
            while True:
                try:
                    p["forca"] = int(input("Nova força: "))
                    break
                except ValueError:
                    print("Digite um número válido.")
            salvar()
        elif op == "3":
            while True:
                try:
                    p["defesa"] = int(input("Nova defesa: "))
                    break
                except ValueError:
                    print("Digite um número válido.")
            salvar()
        elif op == "4":
            while True:
                try:
                    p["vida"] = int(input("Nova vida: "))
                    break
                except ValueError:
                    print("Digite um número válido.")
            salvar()
        elif op == "0":
            print("OK\n")
            break
        else:
            print("Inválido")

def deletar():
    exibir()
    
    while True:
        try:
            idx = int(input("Índice: "))
            break
        except ValueError:
            print("Digite um número válido.\n")
    
    if not existe(idx):
        print("Inválido\n")
        return
    
    personagens.pop(idx)
    salvar()
    print("OK\n")

def existe(idx):
    return 0 <= idx < len(personagens)

def buscar():
    nome = input("Nome para buscar: ").lower()
    encontrados = [i for i, p in enumerate(personagens) if nome in p["nome"].lower()]
    
    if not encontrados:
        print("Nenhum personagem encontrado.\n")
        return
    
    print()
    for i in encontrados:
        p = personagens[i]
        print(f"[{i}] {p['nome']} - F:{p['forca']} D:{p['defesa']} V:{p['vida']}")
    print()

def poder(p):
    return p["forca"] * 2 + p["defesa"] + p["vida"]

def comparar():
    exibir()
    
    if len(personagens) < 2:
        print("Precisa 2+\n")
        return
    
    while True:
        try:
            i1 = int(input("Primeiro: "))
            break
        except ValueError:
            print("Digite um número válido.\n")
    
    while True:
        try:
            i2 = int(input("Segundo: "))
            break
        except ValueError:
            print("Digite um número válido.\n")
    
    if i1 < 0 or i1 >= len(personagens) or i2 < 0 or i2 >= len(personagens) or i1 == i2:
        print("Inválido\n")
        return
    
    p1, p2 = personagens[i1], personagens[i2]
    pot1, pot2 = poder(p1), poder(p2)
    
    print(f"\n{p1['nome']} ({pot1}) VS {p2['nome']} ({pot2})")
    if pot1 > pot2:
        print(f"{p1['nome']} venceu\n")
    elif pot2 > pot1:
        print(f"{p2['nome']} venceu\n")
    else:
        print("Empate\n")

def main():
    carregar()
    
    while True:
        print("\n" + "="*50)
        print(" "*15 + "CRUD RPG")
        print("="*50)
        print("1 - Criar personagem")
        print("2 - Listar personagens")
        print("3 - Buscar personagem")
        print("4 - Atualizar personagem")
        print("5 - Deletar personagem")
        print("6 - Comparar personagens")
        print("0 - Sair")
        print("="*50)
        
        op = input("Escolha uma opção: ")
        
        if op == "1":
            criar()
        elif op == "2":
            exibir()
        elif op == "3":
            buscar()
        elif op == "4":
            atualizar()
        elif op == "5":
            deletar()
        elif op == "6":
            comparar()
        elif op == "0":
            print("\nSaindo...")
            break
        else:
            print("Opção inválida.\n")

main()