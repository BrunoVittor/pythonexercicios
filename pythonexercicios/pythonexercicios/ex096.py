#  Faça um programa que tenha uma função chamada área(),
#  que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    r = larg * comp
    print(f'A área do terreno com {larg} X {comp} é de: {r}m²')


print('Cálculo de terreno')
print('-' * 30)
l = float(input('Largura do terreno: '))
c = float(input('Comprimento do terreno: '))
area(l, c)








