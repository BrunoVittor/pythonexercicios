# Escreva um programa que leia o salário de um funcionário e calcule o valor do seu aumento, para salários superiores a
# R$ 1250,00 o aumento é de 10%, para inferiores ou iguais o aumento é de 15%.

salário = float(input('Digite um salário: R$ '))
if salário > 1250:
    aumento = salário + (salário * 10 / 100)
    print('O salário de R$ {} subiu para R$ {}'.format(salário, aumento))
else:
    salário <= 1250
    aumento = salário + (salário * 15 / 100)
    print('O salário de R$ {} subiu para R$ {}'.format(salário, aumento))
