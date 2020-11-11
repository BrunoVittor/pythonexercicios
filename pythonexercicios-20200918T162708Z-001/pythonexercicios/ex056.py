# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
idademaisvelho = 0
media = 0
maisvelho = ''
menor = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = int(input('Digite o sexo da {}ª pessoa: [1] Masculino [2] Feminino: '.format(c)))
    media = media + idade
    if sexo == 1:
        if idade > idademaisvelho:
            idademaisvelho = idade
            maisvelho = nome
    else:
        if idade < 20:
            menor = menor + 1
print('A média de idade do grupo é de {}'.format(media))
print('O homem mais velho se chama {}'.format(maisvelho))
print('Existem {} mulheres com menos de 20 anos'.format(menor))




'''media = 0
idademaisvelho = 0
maisvelho = ''
menor = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = int(input('Digite o sexo da {}ª pessoa: [ 1 ] masculino ou [ 2 ] feminino: '.format(c)))
    media = media + idade
    if sexo == 1:
        if idade > idademaisvelho:
            idademaisvelho = idade
            maisvelho = nome
    else:
        if idade < 20:
            menor = menor + 1
print('A idade média do grupo é {} anos'.format(media / c))
print('O homem mais velho é {}'.format(maisvelho))
print('existem {} mulheres com menos de 20 anos'.format(menor))'''
