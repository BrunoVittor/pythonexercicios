# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes


print('-=' * 15)
print('Analisador de triângulos ...')
print('-=' * 15)
r1 = float(input('Digite a primeira medida: '))
r2 = float(input('Digite a segunda medida: '))
r3 = float(input('Digite a terceira medida: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo !')
    if r1 == r2 == r3:
        print('EQUILÀTERO: todos os lados iguais !')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO: todos os lados diferentes')
    else:
        print('ISÓCELES: dois lados iguais, um diferente')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo !')
