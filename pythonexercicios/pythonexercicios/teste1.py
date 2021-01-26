'''filme = {'titulo': 'Star wars', 'ano': 1977, 'diretor': 'George Lucas'}
for k, v in filme.items():
    print(f'O {k} é {v}')'''

# função
"""
    Parâmetros opcionais:
    
    def soma(a=0, b=0, c=0): -> dessa forma não é nescessário informar todos os parâmetros exigidos pela função !
"""
'''
def soma (a, b):
    valora = int(input('Digite o 1º valor: '))
    valorb= int(input('Digite o 2º valor: '))
    s = valora + valorb
    print(s)
'''

# Escopo de variáveis:
"""
    No python escopo é onde variável vai existir e onde vai deixar de existir:
"""


# variável composta = Tuplas
'''filme = {'titulo': 'Star wars', 'ano': 1977, 'diretor': 'George Lucas'}
for k, v in filme.items():
    print(f'O {k} é {v}')'''

# lista dentro de lista
'''galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')'''

# Estrutura criada em lista para definir maior e menor idade
'''for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')'''


# Função para somar valores pares em uma lista
'''
def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
'''

# estrutura quer continuar ?
''' resp = str(input('Quer continuar [ S/N ]: ')).strip().upper()[0]
    if resp in 'Nn':
        break'''

# estrutura maior e menor
'''
mai = men = 0

if len(princ) == 0:
    mai = men = temp[1]
else:
    if temp[1] > mai:
        mai = temp[1]
    if temp[1] < men:
        men = temp[1]'''

# estrutura maior e menor 2.0
'''
def maior(*num):
    cont = maior = 0
    for valor in num:
        print(f'{valor} ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
'''

# Dicionários são identificados com { }
'''dados = dict()
ou
dados = {'nome':'Pedro', 'idade':25   } O : adiciona valor ao identificador
print(dados['nome']) Pedro
para adicionar um elemento : dados['sexo'] = 'm'
del dados['idade'] O del remove o elemento
values vai selecionar apenas os valores inseridos, ex;
print(filme.values()) ... star wars
keys vai selecionar apenas o tipo da informação, ex:
print(filme.keys()) ... filme
intens seleciona a iformção total, ex:
print(filme.itens()) ... filme, star wars
esses conceitos podem ser utilizados no laços, ex:
for k (keys), v (value) in filme.items():
print(f'O (k) é (v)')  ... O titulo é star wars
na hora de referẽnciar os elementos se [] na hora de declarar de usa {}'''

# estrutura para criação e declaração de dicionários
'''pessoas = {'nome': 'Bruno', 'idade':22, 'sexo': 'masculino'}
print(f'O {pessoas["nome"]} têm {pessoas["idade"]} anos.')
ou
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k) vai aparecer pessoas, idade, sexo
for k in pessoas.values():
    print(k) vai aparecer Bruno, 33, masculino
for k in pessoas.items()
    print(f'{k} = {v}') vai aparecer nome = bruno, idade = 33, sexo = masculino

para substituição no dicionário:
pessoas['nome'] = 'Leandro' 
para adicionar funciona da mesma forma;
pessoas['peso'] = 89,5
'''

# Algoritimo listas/dicionário

'''estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativo: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) # no caso do dicionário se tuiliza copy() para copiara  lista
    for e in brasil:
        for v in e.values(): # aqui é definido o tipo de informação no caso values
            print(v, end=' ')
        print()'''

# Calculadora criada para realizar operações aritiméticas em Binário.
'''
def calcular():
    # input para receber os operadores.
    operacao = input(''''''
    Por favor, selecione o operador desejado:
    ( + ) Para Soma
    ( - ) Para Subtração
    ( * ) Para Multiplição
    ( / ) Para Dvivisão 
    ( % ) Para Porcentagem 
    '''
'''
    # Bloco criado para receber o input do primeiro número Binário.
    while True:

        if operacao == '%':
            binario1 = int(input('Por favor, digite a porcentagem desejada: '))
            b1 = str(binario1)
            numero1 = int(b1, 2)

        if operacao != '%':
            binario1 = int(input('Por favor, digite o primeiro número binário entre 0 e 255: '))
            b1 = str(binario1)
            numero1 = int(b1, 2)

        if numero1 < 0 or numero1 > 255:
            print('Você digitou o numero {}, por favor digite um numero entre 0 e 255.'.format(numero1))

        else:
            break

    # Bloco criado para receber o input do segundo número Binário.
    while True:
        binario2 = int(input('Por favor, digite o segundo número binário ente 0 - 255: '))
        b2 = str(binario2)
        numero2 = int(b2, 2)

        if numero2 < 0 or numero2 > 255:
            print('Você digitou o número {} '.format(numero2))
            print('Por favor, digite um número em binário entre 0 - 255 ')

        else:
            break

    # Bloco contendo as fórmulas definidas pelos operadores aritiméticos.
    if operacao == '+':
        resultado = numero1 + numero2
        resultadoFinal = (bin(resultado)[2:])
        print('{} + {} ='.format(binario1, binario2), resultadoFinal.zfill(8))

    elif operacao == '-':
        resultado = numero1 - numero2
        resultadoFinal = (bin(resultado)[2:])
        print('{} - {} ='.format(binario1, binario2), resultadoFinal.zfill(8))

    elif operacao == '*':
        resultado = numero1 * numero2
        resultadoFinal = (bin(resultado)[2:])
        print('{} * {} ='.format(binario1, binario2), resultadoFinal.zfill(8))

    elif operacao == '/':
        resultado = numero1 / numero2
        d = int(resultado)
        resultadoFinal = (bin(d)[2:])
        print('{} / {} ='.format(binario1, binario2), resultadoFinal.zfill(8))

    elif operacao == '%':
        resultado = (numero1 * numero2 / 100)
        p = int(resultado)
        resultadoFinal = (bin(p)[2:])
        print('{} % de {} ='.format(binario1, binario2), resultadoFinal.zfill(8))

    # Mensgem exibida ao digitar um operador inválido.
    else:
        print('Você não escolheu um operador válido, por favor escolha novamente.')

    again()


# Função criada para dar continuidade ao programa caso seja solicitado sim ou não.
def again():
    calc_again = input(''''''
Você deseja calcular novamente ?
Por favor aperte Y para sim ou N para não.'''
''')

    if calc_again.upper() == 'Y':
        calcular()
    elif calc_again.upper() == 'N':
        print('Até breve!.')
    else:
        again()


calcular()'''

'''
Calculo de idade:

from datetime import datetime

idade = datetime.now().year - nascimento

'''

'''
# Estrutura básica de função

def linha(msg): # msg é o parametro da função, ou seja, o conteúdo que será inserido quando a função for chamada
    print('+-'*30)
    print(msg)
    print('+-'*30)


linha('        Alunos         ') # conteúdo do parâmetro
linha('        Professores       ')
linha('        Funcionários        ')

'''


'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')


soma(5, 5)
soma(9, 1)'''

'''
def cont(*valores): # desempacotamento
    print(valores)


cont(4, 8, 8, 4)
cont(9, 6)
'''

