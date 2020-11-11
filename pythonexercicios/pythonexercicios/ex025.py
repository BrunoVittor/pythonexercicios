# Crie um programa que leia o nome de uma pessoa e diga se tem silva no nome

nome = str(input('Digite um nome: ')).strip()
print('Seu nome têm silva ({}) ?'.format('silva' in nome.lower()))


