while True:
    numero_um   = input("Digite o primeiro numero: ")
    numero_dois = input("Digite o numero dois: ")
    operador    = input("Qual operação deseja realizar: "
    "[+]"
    "[-]"
    "[*]"
    "[/]")

    parametro_invalido = None
    resultado = 0
    numero_um_float = 0
    numero_dois_float = 0

    try:
        numero_um_float   = float(numero_um)
        numero_dois_float = float(numero_dois)
        parametro_invalido = None
    except:
        print("Insira numeros validos! ")
        parametro_invalido = True
    
    if parametro_invalido is True:
        print("Numero ou operação digitada invalida.")

    if parametro_invalido is None:
        if operador == '+':
            resultado = numero_um_float + numero_dois_float
        elif operador == '-':
            resultado = numero_um_float - numero_dois_float
        elif operador == '*':
            resultado = numero_um_float * numero_dois_float
        else:
            resultado = numero_um_float / numero_dois_float
        
    print(f"{numero_um_float} {operador} {numero_dois_float} = {resultado}")

    sair = input('Deseja sair? (s/n):').lower().startswith('s')
    print(sair)
    if sair is True:
        break
