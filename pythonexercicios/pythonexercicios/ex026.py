# Faça um programa que leia um frase e mostre:
# Quantas vezes aparece a letra a
# Em que posição ela parece a primeria vez
# em que posição ela aperec a ultima vez

'''x = str(input('Escreva uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(x.count('A'))) # count mostra quantas vezes aparece a letra selecionda
print('A letra A aperece na posicção {}'.format(x.find('A'))) # find mostra a posição
print('A ultima vez que a letra A aperce é na posição {}'.format(x.rfind('A'))) # rfind procura das direita para a esquerda'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aperece pela primeira vez na posição {}'.format(frase.find('A')))
print('A letra A parece pela ultima vez na posição {}'.format(frase.rfind('A')))


