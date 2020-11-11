# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
# calcule e mostre o comprimento da ipotenusa


# Essa é a forma matemática de fazer o calculp
'''co = float(input('Digite o cateto opposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

# Essa é a forma com importação de bibliotecas de fazer o cálculo
import math
co = float(input('Digite o cateto opposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

