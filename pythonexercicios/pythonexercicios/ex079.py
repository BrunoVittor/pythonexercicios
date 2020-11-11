# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


# del lanche[3] >>> elimina o indeice incdicado na lista
# lanche.pop(3) >>> mesma coisa
# lanche.remove('pizza') >>> elimina pelo conteúdo do índice e reṕosiciona


list = []
x = 0
while x < 20:
    x += 1
    n = int(input('Digite um valor: '))
    if n not in list:
        list.append(n)
        list.sort()
    else:
        print('Número já existe')
    resp = str(input('Voce quer continuar? [S/N]'))
    if resp not in 'Ss':
        break

print(f'Os números digitados foram: {list}')











'''

numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso !')
    else:
        print('Valor repetido ! não será dicionado.')
    resp = str(input('Deseja continuar [ S / N ]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
numeros.sort()
print(f'Os valores digitados são {numeros}')
'''