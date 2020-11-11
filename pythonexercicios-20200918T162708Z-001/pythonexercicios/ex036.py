# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual é o valor da casa ? : R$ '))
salario = float(input('Qual é o seu salário ? : R$ '))
anos = int(input('Em quantos anos você pretende pagar ? : '))
mensalidade = valor / (anos * 12)
porcentagem = (salario * 30 / 100)
print('O valor da casa é de {:.2f}, o seu salário é de R$ {:.2f} e as parcelas serão em {} anos.'.format(valor, salario, anos))
if mensalidade >= porcentagem:
    print('\033[31mInfelizmente seu empréstimo nao foi aprovado.\033[m')
else:
    print('\033[32mParabéns seu salário foi aprovado!\033[m')

