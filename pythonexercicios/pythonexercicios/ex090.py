# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.


estudante = dict()
estudante['Nome'] = str(input('Nome: '))
estudante['Média'] = float(input('Média: '))
if estudante['Média'] >= 7:
    estudante['Situação'] = 'Aprovado'
elif 5<= estudante['Média'] < 7:
    estudante['Situação'] = 'Recuperação'
else:
    estudante['Situação'] = 'Reprovado'
for k, v in estudante.items():
    print(f'{k} é igual a {v}')













