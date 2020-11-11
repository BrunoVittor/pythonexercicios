# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''AS opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua escolha ???  '))
if jogador > 2:
    print('\033[31mJOGADA INVÁLIDA\033[m')
    quit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!!')
print('-==' * 20)
print('O computador escolheu {} !'.format(itens[comp]))
print('Você escolheu {} !'.format(itens[jogador]))
print('-==' * 20)
if comp == 0:
    if jogador == 0:
        print('\033[33mEmpate\033[m !!!')
    elif jogador == 1:
        print('\033[32mVocê Venceu\033[m !!!')
    elif jogador == 2:
        print('\033[31mVocê Perdeu\033[m !!!')
elif comp == 1:
    if jogador == 0:
        print('\033[31mVocê Perdeu\033[m !!!')
    elif jogador == 1:
        print('\033[33mEmpate\033[m !!!')
    elif jogador == 2:
        print('\033[32mVocê Venceu\033[m !!!')
elif comp == 2:
    if jogador == 0:
        print('\033[32mVocê Venceu\033[m !!!')
    elif jogador == 1:
        print('\033[31mVocê Perdeu\033[m !!!')
    elif jogador == 2:
        print('\033[33mEmpate\033[m !!!')


'''def again():
    jogador_again = input('Deseja jogar novamente ?')
    if jogador_again.upper() == 'Y':
        jogador()
    elif jogador_again.upper() == 'N':
        print('Até breve !!!')
    else:
        again()'''
