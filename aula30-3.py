nome = input("Digite seu nome: ")

if len(nome) <= 4:
    print("Nome curto")
elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome e normal")
else:
    print("Seu nome e grande")
