
# variável composta = Tuplas
'''filme = {'titulo': 'Star wars', 'ano': 1977, 'diretor': 'George Lucas'}
for k, v in filme.items():
    print(f'O {k} é {v}')'''

# função
'''def soma (a, b):
    valora = int(input('Digite o 1º valor: '))
    valorb= int(input('Digite o 2º valor: '))
    s = valora + valorb
    print(s)'''

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

# estrutura quer continuar ?
''' resp = str(input('Quer continuar [ S/N ]: ')).strip().upper()[0]
    if resp in 'Nn':
        break'''

# estrutura maio e menor

'''mai = men = 0

if len(princ) == 0:
    mai = men = temp[1]
else:
    if temp[1] > mai:
        mai = temp[1]
    if temp[1] < men:
        men = temp[1]'''

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

