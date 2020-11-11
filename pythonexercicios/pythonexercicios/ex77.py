# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('homem', 'mulher', 'gato', 'carro', 'viagem', 'hotel', 'praia', 'gasolina', 'dinossauro',
            'hospedagem', 'lua', 'estratosfera', 'videogame', 'computador')

for con in palavras:
    print(f'\nNa palavra {con.upper()} temos: ', end='')
    for letra in con:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
