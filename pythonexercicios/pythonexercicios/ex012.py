# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

'''pre = float(input('Digite o valor do produto: '))
des = pre * 5 / 100
res = pre - des
print('O preço de R$ {:.2f} com 5% de desconto é de R$ {:.2f}'.format(pre, res))'''


pre = float(input('Digite o valor do produto: R$ '))
des = (pre * 5) / 100
res = pre - des
print(f'O valor com desconto é de R$ {res}')

