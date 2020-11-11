# O professor quer sortear a ordem de exibição dos trabalhos dos alunos
# faça um programa que leia o nome dos alunos  e mostre a ordem sorteada
from random import shuffle
a1 = str(input('Aluno: '))
a2 = str(input('Aluno: '))
a3 = str(input('Aluno: '))
a4 = str(input('Aluno: '))
lista = [a1,a2,a3,a4]
shuffle(lista)
print('A ordem dos alunos é: ')
print(lista)
