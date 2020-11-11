# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

data = date.today().year
totalmai = 0
totamen = 0
for pessoa in range(1, 8):
    nascimento = int(input('Digite o nascimento da {}ª pessoa: '.format(pessoa)))
    idade = data - nascimento
    if idade >= 21:
       totalmai += 1
    else:
      totamen += 1
print('Ao todo tivemos {} pessoas Mairores de idade'.format(totalmai))
print('E ao odo tivemos {} pessoas menores de idade'.format(totamen))
print('Fim')
