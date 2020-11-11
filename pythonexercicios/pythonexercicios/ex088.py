# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


from random import randint

for x in range(int(input("Digite quantidade de jogos: "))):
    print([randint(1, 61) for i in range(6)])


'''lista = []
jogos = []
quant = int(input('Quantos jogos?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('Sorteando jogos')
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
'''


'''importar a biblioteca de sorteio

lista principal
lista temporária

dentro o loop executar as tarefas abaixo
perguntar qual o máximo de jogos serão sorteados
sortear no máximo 6 jogos
sortear números de 1 á 60
adicionar os números em uma lista temporária
criar uma cópia da lista temporária em uma lista pricipal
excluir as informações da lista temporária cada vez que o loop rodar na quantidade determinada
mostar a quantidade de jogos com os números sorteados'''
