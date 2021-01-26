# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(i, f, p):

    """
    -> Faz uma contagem e mostra na tela.
    :parametro i: início da contagem
    :parâmetro f: fim da contagem
    :parâmetro p: passo da contagem
    :return: sem retorno
    """

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('~' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f' {cont}', end='')
            sleep(0.5)
            cont += p
        print(' FIM')
    else:
        cont = i
        while cont >= f:
            print(f' {cont}', end='')
            sleep(0.5)
            cont -= p
        print(' FIM')
# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Contagem personalizada: ')
ini = int(input('inicio: '))
fim = int(input('fim:    '))
pas = int(input('passo:  '))
contador(ini, fim, pas)
