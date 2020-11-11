# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


ficha = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('digite a 1ª nota: '))
    nota2 = float(input('Dogote a 2ª nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        print('Finalizando ...')
        break
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 40)
for i, c in enumerate(ficha):
    print(f'{i:<4}{c[0]:<10}{c[2]:>8}')
while True:
    print('-' * 40)
    aluno = int(input('Nota de qual aluno? Digite p para parar: '))
    if aluno == 'p':
        print('Fim do programa !')
        break
    if aluno <= len(ficha) - 1:
        print(f'Notas de {ficha[aluno][0]} são {ficha[aluno][1]}')
print('Obrigado !!!')
