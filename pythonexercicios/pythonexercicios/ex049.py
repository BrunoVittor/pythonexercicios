# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

'''n = int(input('Digite um número para ver sua tabuada: '))
print('=' * 12)
for tab in range(1, 11):
    res = n * tab
    print(' {} X {} = {}'.format(n, tab, res))
print('=' * 12)'''

while True:
    num = int(input('Qual tabuada?: '))
    for tab in range(1, 11):
        res = num * tab
        print(f'{num} X {tab} = {res}')
