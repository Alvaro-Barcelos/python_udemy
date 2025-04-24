velocidade  = 61
local_carro = 101

RADAR1      = 60
LOCAL_1     = 100
RADAR_RANGE = 1

carro_multado = local_carro >= LOCAL_1 - RADAR_RANGE and local_carro <= LOCAL_1 + RADAR_RANGE

if velocidade > RADAR1:
    if carro_multado:
        print('Carro multado')
    else:
        print('Carro não multado')
