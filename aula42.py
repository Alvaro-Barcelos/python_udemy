frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum. '.lower()

i = 0
letra_repetidas = ''
qtd_apareceu    = 0

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_atual = frase.count(letra_atual)

    if qtd_apareceu < qtd_apareceu_atual:
        qtd_apareceu = qtd_apareceu_atual
        letra_repetidas = letra_atual
    i += 1
    
print(letra_repetidas, ' -- ', qtd_apareceu  )