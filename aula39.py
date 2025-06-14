nome = 'Alvaro Barcelos'
nome_clone = ''
i = 0

while i < len(nome):
    letra = nome[i]
    nome_clone += '*' + letra
    i += 1
print(nome_clone)
