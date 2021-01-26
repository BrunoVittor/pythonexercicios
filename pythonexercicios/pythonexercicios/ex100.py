# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import *
from time import sleep


def sorteio(lista):
    print('Sorteando a lista: ', end='')
    for c in range(1, 6):
        x = randint(1, 10)
        lista.append(x)
        print(f'{x} ', end='')
        sleep(0.3)
    print('FIM')


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando dos valores pares de {lista}, temos {soma}')


numeros = list()
sorteio(numeros)
somaPar(numeros)
