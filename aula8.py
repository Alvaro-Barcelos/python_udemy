nome           = input(str('Qual o seu nome? '))
idade          = int(input('Qual a sua idade? '))
maior_de_idade = True if idade >= 18 else False
ano_nascimento = int(input('Qual o seu ano de nascimento? '))
altura         = float(input('Qual a sua altura? '))

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f"Maior de idade: {'Sim' if maior_de_idade else 'Não'}")
print(f'Ano de nascimento: {ano_nascimento}')
print(f'Altura: {altura}')