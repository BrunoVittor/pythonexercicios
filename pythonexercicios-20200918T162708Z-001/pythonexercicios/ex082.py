# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
par = []
impar = []
numero = []
while True:
    numero.append(int(input('Digite um valor: ')))
    resp = (str(input('Quer continuar ? [ S/N ]: '))).strip().upper()[0]
    if resp in 'Nn':
        break
    for i, v in enumerate(numero):
        if v % 2 == 0:
           par.append(v)
        elif v % 2 == 1:
            impar.append(v)
print(f'A lista completa é {numero}')
print(f'A lista de pares é {par}')
print(f'A lista de impares {impar}')
