# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# NO final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
mai = men = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print('=-' * 30)
print(f'o valores digitados foram {valores}')
print(f'O maior valor é {mai} nas posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor é {men} nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}... ', end='')
print()
print('=-' * 30)
