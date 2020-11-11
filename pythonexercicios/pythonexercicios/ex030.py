# Crie um número inteiro e mostre se ele é par ou ímpar

'''num = int(input('Digite um número: '))
par = num % 2
if par > 0:
    print('Esse número {} é impar'.format(num))
else:
    print('Esse número é par'.format(num))'''


while True:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        print('Par')
    else:
        print('Impar')
    resp = str(input('Continuar?: ')).strip().upper()[0]
    if resp not in 'Ss':
        break