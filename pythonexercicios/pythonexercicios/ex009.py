# faça um programa que leia um número inteiro e mostre a sua taboada


'''t = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print('{} X {:2} = {}'.format(t, 1, t*1))
print('{} X {:2} = {}'.format(t, 2, t*2))
print('{} X {:2} = {}'.format(t, 3, t*3))
print('{} X {:2} = {}'.format(t, 4, t*4))
print('{} X {:2} = {}'.format(t, 5, t*5))
print('{} X {:2} = {}'.format(t, 6, t*6))
print('{} X {:2} = {}'.format(t, 7, t*7))
print('{} X {:2} = {}'.format(t, 8, t*8))
print('{} X {:2} = {}'.format(t, 9, t*9))
print('{} X {:2} = {}'.format(t, 10, t*10))
print('-'*12)'''

print('TABOADA V 3.0')
print('=-'*20)
while True:
    t = int(input('Digite um número para ver sua taboada: '))
    print('=-' * 20)
    for c in range(1, 11):
        n = c * t
        print(f'{t} X {c} = {n}')
    print('=-' * 20)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('=-' * 20)
    if resp not in 'Ss':
        break
print('FIM DO PROGRAMA')
