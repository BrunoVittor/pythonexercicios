# Faça um programa que leia 3 numeros e mostre o maior e o menor .

a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terciro valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
