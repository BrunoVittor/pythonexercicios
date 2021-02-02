# aça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome='Desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gols !!!')


n = str(input('Digite o nome do jogador: '))
g = str(input('Digite quantos gols ele fez: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
