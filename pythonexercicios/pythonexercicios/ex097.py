# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    tam = len(msg) + 6
    print('~' * tam)
    print(f'   {msg}')
    print('~' * tam)

escre = str(input('Digite um nome: '))
escreva(escre)
