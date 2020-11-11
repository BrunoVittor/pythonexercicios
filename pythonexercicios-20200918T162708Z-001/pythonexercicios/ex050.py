# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
cont = 0
soma = 0
for c in range(1, 7):
    valor = int(input('Digite o {}º número: '.format(c)))
    if valor % 2 == 0:
        cont = cont + 1
        soma = soma + c
print('Você informou {} numeros pares e a soma foi {}'.format(cont, soma))
print('Fim')
