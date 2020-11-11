# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# NO final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# del lanche[3] >>> elimina o indeice incdicado na lista
# lanche.pop(3) >>> mesma coisa
# lanche.remove('pizza') >>> elimina pelo conteúdo do índice e reṕosiciona os índices


mai = 0
men = 0
list = []
for c in range(0, 5):
    list.append(int(input(f'Digite o número {c}: ')))
    if c == 0:
        mai = men = list[c]
    else:
        if list[c] > mai:
            mai = list[c]
        if list[c] < men:
            men = list[c]
print(f' Os valores digitados foram {list}')
print(f'O maior número foi {mai} na posição: ', end='')
for i, c in enumerate(list):
    if c == mai:
        print(f'{i}...', end='')
print()
print(f'O menor número foi {men} na posição: ', end='')
for i, c in enumerate(list):
    if c == men:
        print(f'{i}...', end='')








'''mai = men = 0
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
'''
