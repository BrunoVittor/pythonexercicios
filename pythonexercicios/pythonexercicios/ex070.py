# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

gasto = mais = barato = quanti = 0
maisbarato = ' '
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$ '))
    gasto += preco
    resp = ' '
    quanti += 1
    if preco > 1000:
        mais += 1
    if quanti == 1 or preco < barato:
        barato = preco
        maisbarato = nome
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? [S/N] : ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total gasto foi de R$ {gasto:.2f}')
print(f'{mais} Produtos custam mais de R$ 1000,00')
print(f'O produto {maisbarato} é o mais barato')