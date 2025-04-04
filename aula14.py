a = 'AAA'
b = 'B'
c = 1.1

string = 'a={1} b={0} c={nome:.2f}'

formato = string.format(a,b, nome=c)

print(formato)