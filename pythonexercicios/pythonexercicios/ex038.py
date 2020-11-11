# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

'''num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))
if num1 > num2 :
    print('O primeiro número é maior! {}'.format(num1))
elif num1 < num2 :
    print('O segundo número é maior'.format(num2))
else:
    print('Não existe valor maior, os dois são iguais')'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('O primeiro valor é maior')
elif num1 < num2:
    print('O segundo valor é maior')
else:
    print('Não existe maior, são iguais')
