# Faça um programa qu eleia o nome completo de uma pessoa, mostrando em seguida o primerio e o segundo nome separadamente
# Ex: Ana Maria Souza
# primeiro = Ana
# ultimo = Souza
nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('O seu primeiro nome é {}'.format(n[0]))
print('O seu ultimo nome é {}'.format(n[len(n)-1]))