idade = input("Qual a sua idade? ")
nome  = input("Qual o seu nome? ")

if nome and idade:
    print(f'Olá {nome}, você tem {idade} anos.')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'Seu nome contem espaços? {"Sim" if " " in nome else "Não"}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print("Você não digitou nada!")
    print("Tente novamente!")
    print("Até mais!")
