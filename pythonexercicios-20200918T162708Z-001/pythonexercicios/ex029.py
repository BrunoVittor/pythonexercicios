# Escreva um programa que leia a velocidade de um carro, se ele passar de 80 km/h, mostre uma mensagem dizendo que
# ele foi multado, a multa vai custar R$7,00 por cada km acima do limite

vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    mul = (vel - 80) * 7.00
    print('Você foi MULTADO !!! A sua velocidade foi de {} km/h você foi multado em R$ {}'.format(vel, mul))
else:
    print('Boa viagem!, siga em segurança')
