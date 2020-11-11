# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('digite o primeiro número: ')),
       int(input('digite o segundo número: ')),
       int(input('digite o terceiro número: ')),
       int(input('digite o quarto número: ')))
print(f'Você digitou os valores{num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
# index mostra a posição do objeto dentro dos ( ) 
    print(f'O valor primeiro valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado')
