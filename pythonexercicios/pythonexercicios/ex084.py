# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

principal = []
secundaria = []
pesada = leve = 0
while True:
    secundaria.append(str(input('Nome: ')))
    secundaria.append(int(input('Peso: ')))
    if len(principal) == 0:
        pesada = leve = secundaria[1]
    else:
        if secundaria[1] > pesada:
            pesada = secundaria[1]
        if secundaria[1] < leve:
            leve = secundaria[1]
    principal.append(secundaria[:])
    secundaria.clear()
    resp = str(input('Quer continuar: [S/N]: ')).strip().upper()
    if resp in 'Nn':
        break
print(f'O maior peso foi de {pesada} Kg: ', end='')
for c in principal:
    if c[1] == pesada:
        print(f'{c[0]}')
print()
print(f'O menor peso foi de {leve} kg: ', end='')
for c in principal:
    if c[1] == leve:
        print(f'{c[0]}')

# Aula lsitas parte 2

'''galera = []
pessoa = []
for c in range(0, 3):
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('idade: ')))
    galera.append(pessoa[:])
    pessoa.clear()
for p in galera:
    if p[1] >= 20:
        print(f'A pessoa {p[0]} é mais velho')
    else:
        print(f'A pessoa {p[0]} é mais nova')
print(galera)'''
