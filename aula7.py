def func_idade(idade):
    if idade >= 18:
        return True
    else:
        return False

nome = 'Alvaro'
idade = 20
maior_de_idade = func_idade(idade)

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Maior de idade: {maior_de_idade}')
