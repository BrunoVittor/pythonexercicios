# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
V = 0
while True:
    jogador = int(input('Digite um valor: '))
    comp = randint(0, 10)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Digite par ou ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {comp}. Total de {total}', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPÁR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            V += 1
        else:
            print('VOcê PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU')
            V += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente ?')
print(f'Você tentou {V} vezes!')
