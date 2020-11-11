# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
print('Sou seu computador e estou pensando em um número entre 0 e 10')
print('Consegue acertar ? ...')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?: '))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais !!!! tente mais uma vez ...')
        elif jogador > computador:
            print('Menos !!!!! tente mais uma vez ...')
print('Acertou com {} palpites. Parabéns !!!!!!!'.format(palpite))
