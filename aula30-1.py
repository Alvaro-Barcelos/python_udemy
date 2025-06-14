numero = input("Digite um numero: ")

try:
    numero = float(numero)
    if numero % 2 == 0:
        print(f"O numero {numero:.0f} e par! ")
except:
    print("O numero nao e par")
