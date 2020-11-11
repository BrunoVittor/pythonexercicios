# Crie um número inteiro e mostre se ele é par ou ímpar

num = int(input('Digite um número: '))
par = num % 2
if par > 0:
    print('Esse número {} é impar'.format(num))
else:
    print('Esse número é par'.format(num))