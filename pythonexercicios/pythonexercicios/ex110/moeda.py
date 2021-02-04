# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumentar(preco=0, taxa=0, formato=False):
    a = preco + (preco * taxa / 100)
    return a if not formato else moeda(a)


def diminuir(preco=0, taxa=0, formato=False):
    a = preco - (preco * taxa / 100)
    return a if not formato else moeda(a)


def dobro(preco=0, formato=False):
    a = preco * 2
    return a if not formato else moeda(a)


def metade(preco=0, formato=False):
    a = preco / 2
    return a if not formato else moeda(a)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxa=0):
    print('~' * 35)
    print('Analisando Valores'.center(35))
    print('~' * 35)
    return f'Valores analisados: \t{moeda(preco)}\n' \
           f'O dobro do valor é: \t{dobro(preco, True)}\n' \
           f'A metade do valor é: \t{metade(preco, True)}\n' \
           f'Aumento de {taxa}% é de: \t{aumentar(preco, taxa, True)}\n' \
           f'Desconto de {taxa}% é de: \t{diminuir(preco, taxa, True)}'
