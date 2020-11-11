# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome santo
# Eu fiz dessa forma porém ele não identifica maiscúlas de minuscúlas
'''cidade = str(input('Digite o nome da cidade : ')).strip()
print('Santo' in cidade)'''

# Resolução do professor:

cid = str(input('Digite o nome da cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
