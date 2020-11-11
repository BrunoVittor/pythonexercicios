# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS KAMILA '))
preco = float(input('Digite o valor das compras: R$ '))
print('''Formas de pagamento:
[ 1 ] Dinheiro ou Cheque
[ 2 ] á vista no cartão
[ 3 ] em até cartão 2x 
[ 4 ] cartão 3x ou mais''')
opcao = int(input('Qual é a opção ? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcelas = preco / 2
    print('O valor das compras de R$ {:.2f} será em 2x de R$ {:.2f} SEM JUROS !'.format(preco, parcelas))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parc = int(input('Qual a quantidade de parcelas: '))
    totparc = total / parc
    print('As compras serão parceçadas em {}X de R$ {:.2f} COM JUROS !'.format(parc, totparc))
else:
    total = preco
    print('\033[31mOPÇÂO INVÁLIDA\033[m : tente novamente !')
print('O valor das compras foi de R$ {:.2f} e vai custar R$ {:.2f} no final !'.format(preco, total))

