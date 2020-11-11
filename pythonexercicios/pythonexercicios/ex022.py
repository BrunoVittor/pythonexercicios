# Crie um programa que leia o nome completo de uma pessoa e mostre :
# O nome com todas a sletras maiúsculas
# O nome com todas a sletras minúsculas
# Quantas letras ao todos sem considerar espaços
# Quantas letras têm o primeiro nome

''''nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome ...')
print('Seu nome em letras maiúsclas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome têm ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome têm {} letras'.format(nome.find(' ')))'''

nome = str(input('Digite seu nome completo: ')).strip()
print('seu nome com letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com as letras minúsculas é {}'.format(nome.lower()))
print('Seu nome têm {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome têm {} letras'.format(nome.find(' '))) # find() vai buscar a letra desejada e mostrar uma antes, no caso buscou 'espaço' e mostrou 'o'

