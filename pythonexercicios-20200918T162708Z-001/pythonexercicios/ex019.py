# um professor quer sortear um dos seus 4 alunos para apagar o quadro
# faça um programa que leia o nome dos 4 alunos e sorteie entre eles

from random import choice
a1 = str(input('Nome do aluno1: '))
a2 = str(input('Nome do aluno2: '))
a3 = str(input('Nome do aluno3: '))
a4 = str(input('Nome do aluno4: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
