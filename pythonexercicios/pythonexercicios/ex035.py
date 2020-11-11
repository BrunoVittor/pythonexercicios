# Desenvola um programa que leia o comprimento de 3 retas e diga se ele forma ou não um triangulo
print('-=' * 15)
print('Analisador de triângulos ...')
print('-=' * 15)
r1 = float(input('Digite a primeira medida: '))
r2 = float(input('Digite a segunda medida: '))
r3 = float(input('Digite a terceira medida: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo !')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo !')
