# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = menor = 0
for c in range(1, 6):
    peso = int(input('Digite o peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso foi {maior} kg e o menor peso foi {menor} kg')
print('É isso')


#estrutura salva na evernote
'''mai = men = 0

if len(princ) == 0:
    mai = men = temp[1]
else:
    if temp[1] > mai:
        mai = temp[1]
    if temp[1] < men:
        men = temp[1]'''
