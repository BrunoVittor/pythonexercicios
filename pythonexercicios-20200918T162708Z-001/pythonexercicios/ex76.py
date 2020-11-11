# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('caneta', 12.00, 'caderno', 20.00, 'cola', 7.00, 'batata', 5.00,
            'inseticida', 10.00, 'margarina', 8.00, 'queijo', 15.00, 'cerveja', 45.00,
            'danone', 8.00, 'pão', 4.00, 'café', 7.00)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f' R$ {listagem[pos]:<7.2f}')
print('-' * 40)
