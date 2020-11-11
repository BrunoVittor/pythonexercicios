# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O computador deverá escreve na tela se o usuário venceu ou perdeu.

# Essa foi a minha resolução
'''from random import choice
n1 = int(0)
n2 = int(1)
n3 = int(2)
n4 = int(3)
n5 = int(4)
n6 = int(5)
lista = [n1, n2, n3, n4, n5, n6]
escolhido = (choice(lista))
numero = int(input('Adivinhe o número que o compuatdor irá escolher: '))
if numero == escolhido:
    print('O número escolhido pelo computador foi {} voçê venceu !!!!'.format(escolhido))
else:
    print('O número escolhido pelo computador foi {} voçê perdeu ...'.format(escolhido))'''

# essa é a resolução do professor

'''from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinha...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('Processando ... ')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))'''












# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O computador deverá escreve na tela se o usuário venceu ou perdeu.

from random import randint # randint randomiza números inseridos

while True:
    comp = randint(0, 5)
    usuario = int(input('Adivinhe o número de 0 a 5: '))

    print('O computador escolheu {}'.format(comp))
    if usuario == comp:
        print('PARABENS você venceu !!!!!!')
    else:
        print('VOCÊ PERDEU !!!!!')
    resp = str(input('Continuar?: ')).strip().upper()[0]
    if resp not in 'Ss':
        break