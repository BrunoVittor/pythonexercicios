# Refaça o DESAFIO 51
# lendo o primeiro termo e a razão de uma PA
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('Gerador de PA')
print('='*7)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo = termo + razão
    cont = cont + 1
print('Fim')
