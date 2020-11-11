# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

'''print('{:=^40}'.format(' LOJAS KAMILA '))
preco = float(input('Digite o valor das compras: R$ '))
print(''''''Formas de pagamento:
[ 1 ] Dinheiro ou Cheque
[ 2 ] á vista no cartão
[ 3 ] em até cartão 2x 
[ 4 ] cartão 3x ou mais'''''')
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
print('O valor das compras foi de R$ {:.2f} e vai custar R$ {:.2f} no final !'.format(preco, total))'''

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal
# – 3x ou mais no cartão: 20% de juros

'''while True:
    try:
        produto = float(input('Dgite o valor do produto: R$ '))
        try:
            condicao = int(input(''''''Qual a condição de pagamento?
        [1] á vista dinheiro/cheque
        [2] á vista no cartão
        [3] em até 2x no cartão
        [4] em 3x ou mais no cartão
        Condição de pagamento:''' '''))

            if condicao == 1:
                desconto = produto - ((produto * 10) / 100)
                print(f'O produto custa R$ {produto} e com o desconto de 10% custa R$ {desconto}')
            elif condicao == 2:
                desconto = produto - ((produto * 5) / 100)
                print(f'O pruduto custa R$ {produto} e com o desconto de 5% custa R$ {desconto}')
            elif condicao == 3:
                parcelas = produto / 2
                print(f'O produto custa R$ {produto} e parcelado em 2x as parcelas são de R$ {parcelas}')
            elif condicao == 4:
                juros = ((produto * 20) / 100) + produto
                print(f'O produto custa R$ {produto} e parcelado em 3x custa R$ {juros} com 20% de juros')
            else:
                print('\033[31m opção inválida!!! \33[m')
            resp = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
            if resp not in 'Ss':
                break
        except:
            print('Favor escolher a condição correta')
    except:
        print('Favor digitar um valor em reais')'''

esta_rodando = True
while esta_rodando:
    try:
        produto = float(input('Dgite o valor do produto: R$ '))

        try:
            condicao = int(input('''Qual a condição de pagamento?
[1] á vista dinheiro/cheque
[2] á vista no cartão
[3] em até 2x no cartão
[4] em 3x ou mais no cartão
Condição de pagamento: '''))
            if condicao == 1:
                desconto = produto - (
                        (produto * 10) / 100)  # Você pode também fazer a % assim --> produto * 0.9 #vai dar 10% de desc
                print(f'O produto custa R$ {produto} e com o desconto de 10% custa R$ {desconto}')
            elif condicao == 2:
                desconto = produto - ((produto * 5) / 100)
                print(f'O pruduto custa R$ {produto} e com o desconto de 5% custa R$ {desconto}')
            elif condicao == 3:
                parcelas = produto / 2
                print(f'O produto custa R$ {produto} e parcelado em 2x as parcelas são de R$ {parcelas}')
            elif condicao == 4:
                juros = ((produto * 20) / 100) + produto
                print(f'O produto custa R$ {produto} e parcelado em 3x custa R$ {juros} com 20% de juros')
            else:
                print('\033[31m opção inválida!!! \33[m')
            resp = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
            if resp not in 'Ss':
                esta_rodando = False
        except ValueError:
            print('Digite uma condição válida')
    except ValueError:
        print('Digite um Valor válido')


