senha = input('Senha: ')

if not senha:
    print("Digite a senha por favor.")
elif senha != '123':
    print('Senha incorreta')
else:
    print('Entrou')