# faça um programa que leia um número de 0 a 9999 e mostre na tela cada número separadamente

'''n = str(input('Digite um número até 9999: '))
u = n[3]
d = n[2]
c = n[1]
m = n[0]
print('O número digitado foi {}\n Unidade {}\n Dezena {}\n Centena {}\n Milhar {}\n'.format(n, u, d, c, m))'''

# com esse cálculo matemático o programa não da erro mesmo se digitado um número menor
n = int(input('Digite um número de 0 á 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('O número digitado foi {}'.format(n))
print('A unidade é {}'.format(u))
print('A dezena é {}'.format(d))
print('A centena é {}'.format(c))
print('O milhar é {}'.format(m))
