# crie um programa que leia quanto dinheiro uma pessoa têm e mostre quantos dólares ele pode comprar
# dólar a US$ = 1,00 = R$ 3,27

re = float(input('digite o valor em R$ '))
do = float(3.27)
res = re / do
print('O valor em real de R${:.2f} covertido em Dólar é de US${:.2f} dólares !'.format(re, res))

