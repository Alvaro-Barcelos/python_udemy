numero = input("Digite um número: ")

try:
    print("STR:", numero)
    numero_float = float(numero)
    print(f"O dobro de {numero} é {numero_float * 2}")
except:
    print("Isto não é um numero")