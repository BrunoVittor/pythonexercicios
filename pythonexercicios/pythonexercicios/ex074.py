# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

n = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os números gerados foram: ', end='')
for c in n:
    print(f'{c} ', end='')
print(f'\nMenor número {min(n)}')
print(f'maior número {max(n)}')






'''numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'os numeros sorteados foram: ', end='')
for c in numeros:
    print(f'{c} ', end='')
print(f'\nO menor número sorteado foi {min(numeros)}')
print(f'O maior número sorteado foi {max(numeros)}')
'''
