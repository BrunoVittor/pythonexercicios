# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


num = (int(input('Digite o primeiro valor: ')),
       int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')),
       int(input('Digite o quarto valor: ')))

print(f'Voce digitou os valores {num}')
if 9 in num:
       print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
       print(f'O número 3 aparece na posição {num.index(3)+1}')
print(f'Os números pares digitados foram: ', end='')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')

