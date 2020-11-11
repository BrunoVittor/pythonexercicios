# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primerio e o segundo nome separadamente
# Ex: Ana Maria Souza
# primeiro = Ana
# ultimo = Souza

'''nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('O seu primeiro nome é {}'.format(n[0]))
print('O seu ultimo nome é {}'.format(n[len(n)-1]))'''


# o split faz o fatiamneto da string, separa por palavras e atribui números a elas:
# Bruno = 0 Vittor = 1


while True:
    nome = str(input('Digite um nome: '))
    nome = nome.split()
    print('O 1º nome é {}'.format(nome[0]))
    print('O 2º nome é {}'.format(nome[len(nome)-1]))
    resp = str(input('Continuar?: ')).strip().upper()
    if resp not in 'Ss':
        break
