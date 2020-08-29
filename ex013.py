# faça um algoritmo que leia o salário de um funcionário e mostre um aumento de 15%

sal = float(input('Digite o salário: R$ '))
aum = sal + (sal * 15 / 100)
print('O salário com o aumento de 15% é de R${}'.format(aum))
