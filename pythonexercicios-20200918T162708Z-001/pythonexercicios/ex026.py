# Faça um programa que leia um frase e mostre:
# Quantas vezes aparece a letra a
# Em que posição ela parece a primeria vez
# em que posição ela aperec a ultima vez

x = str(input('Escreva uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(x.count('A')))
print('A letra A aperece na posicção {}'.format(x.find('A')))
print('A ultima vez que a letra A aperce é na posição {}'.format(x.rfind('A')))

