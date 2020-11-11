# Desenvolva um programa que pergunte o distância de uma viagem em km, calcule o preço da passagem cobrando
# 0,50 centavos por km para viagem até 200 km e 0,45 para viagens mais longas

distancia = float(input('Digite a distância em km: '))

if distancia <= 200:
    passagem = distancia * 0.50
    print('A distãncia percorrida foi {} km e o valor da viagem é {}'.format(distancia,passagem))
else:
    passagem = distancia * 0.45
    print('A distância percorrida foi {} km e o valor da passagem é {}'.format(distancia,passagem))
