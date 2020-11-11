# um professor quer sortear um dos seus 4 alunos para apagar o quadro
# faça um programa que leia o nome dos 4 alunos e sorteie entre eles
from random import choice

al1 = str(input('Aluno 1: '))
al2 = str(input('Aluno 2: '))
al3 = str(input('Aluno 3: '))
al4 = str(input('Aluno 4: '))
list = [al1, al2, al3, al4]
while True:

    resultado = choice(list)
    print(f'O aluno escolhido foi {resultado}')
    resp = str(input('Novamente? [S/n]: ')).strip().upper()[0]
    if resp not in 'Ss':
        break






















'''from random import choice
a1 = str(input('Nome do aluno1: '))
a2 = str(input('Nome do aluno2: '))
a3 = str(input('Nome do aluno3: '))
a4 = str(input('Nome do aluno4: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''
