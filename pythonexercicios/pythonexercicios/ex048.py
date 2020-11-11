# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for cal in range(1, 500, 2):
    if cal % 3 == 0:
        cont = cont + 1
        soma = soma + cal
print('A soma dos {} valores é de {}'.format(cont, soma, end=' '))

