# faça um programa que leia a altura e a largura de uma parede, calcule sua area e quanto de tinta será nescessario
# para pintar a parede

'''al = float(input('Digite a altura da parede: '))
la = float(input('digite a largura da parede: '))
ar = al * la
lts = ar / 2
print('A área total da parede é de {}m² e serão nescessários {} lts de tinta'.format(ar, lts))'''


al = float(input('Digite a altura: '))
la = float(input('Digite a Largura: '))
ar = al * la
lts = ar / 2
print(f'A área da parede é de {ar}mt² e serão necessários {lts}lts de tinta')
