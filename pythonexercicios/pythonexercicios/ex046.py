# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import emoji
from time import sleep
botao = input('''!!!!!!! Pressione 10 para começar a contagem !!!!!!!!!
                        ''')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print(emoji.emojize(':fireworks:' * 20, use_aliases=True))
