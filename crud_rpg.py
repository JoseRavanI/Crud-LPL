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
    forca = int(input("Força: "))
    defesa = int(input("Defesa: "))
    vida = int(input("Vida: "))
    
    personagens.append({"nome": nome, "forca": forca, "defesa": defesa, "vida": vida})
    salvar()
    print("OK\n")

def atualizar():
    exibir()
    idx = int(input("Índice: "))
    
    if idx < 0 or idx >= len(personagens):
        print("Inválido\n")
        return
    
    p = personagens[idx]
    print(f"\n1-Nome 2-Força 3-Defesa 4-Vida 0-Sair")
    
    while True:
        op = input("Opção: ")
        if op == "1":
            p["nome"] = input("Novo nome: ")
        elif op == "2":
            p["forca"] = int(input("Nova força: "))
        elif op == "3":
            p["defesa"] = int(input("Nova defesa: "))
        elif op == "4":
            p["vida"] = int(input("Nova vida: "))
        elif op == "0":
            salvar()
            print("OK\n")
            break
        else:
            print("Inválido")

def deletar():
    exibir()
    idx = int(input("Índice: "))
    
    if idx < 0 or idx >= len(personagens):
        print("Inválido\n")
        return
    
    personagens.pop(idx)
    salvar()
    print("OK\n")

def poder(p):
    return p["forca"] * 2 + p["defesa"] + p["vida"]

def comparar():
    exibir()
    
    if len(personagens) < 2:
        print("Precisa 2+\n")
        return
    
    i1 = int(input("Primeiro: "))
    i2 = int(input("Segundo: "))
    
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
        print("1-Criar 2-Listar 3-Atualizar 4-Deletar 5-Comparar 0-Sair")
        op = input("Opção: ")
        
        if op == "1":
            criar()
        elif op == "2":
            exibir()
        elif op == "3":
            atualizar()
        elif op == "4":
            deletar()
        elif op == "5":
            comparar()
        elif op == "0":
            print("Saindo")
            break
        else:
            print("Inválido\n")

main()