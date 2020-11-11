# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

'''while True:
    n = int(input('Digite um número entre 0 e 20: '))
    resp = ' '
    if 0 <= n <= 20:
        print(f'O número digitado foi {numero[n]}')
        while resp not in 'SN':
            resp = str(input('Deseja continuar ? [S/N] : ')).strip().upper()[0]
        if resp == 'N':
            print('fim')'''

while True:
    n = int(input('Digite um número: '))
    resp = ' '
    if 0 <= n <= 20:
        print(f'O numero digitado foi {numero[n]}')
        while resp not in 'SN':
            resp = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()[0]
        if resp == 'N':
            print('Fim')
            break
    else:
        print('Erro')