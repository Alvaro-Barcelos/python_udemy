hora = input("Qual e a hora? ")

try:
    hora = int(hora)
    if(hora >= 0 and hora <= 11):
        print("Bom dia! ")
    elif(hora >= 12 and hora <= 17):
        print("Boa tarde!")
    else:
        print("Boa noite! ")
except:
    print("Por favor digite uma hora. ")