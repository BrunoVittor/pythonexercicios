# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
# resp - soma - qaunt -média - maior - menor

resp = 'S'
soma = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar {S/N}? ')).strip().upper()[0]
media = soma / quant
print('Foram digitados {} números e a média é {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('Acabou')

'''cont = 0
acumu = 0
numero = int(input('Digite um número: '))
while numero != 0:
    cont = cont + 1
    acumu = acumu + numero
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if continuar == 'S':
        numero = int(input('Digite um número: '))
    elif continuar == 'N':
        média = acumu / cont
        print('Foram digitados {} números e a  média é {}'.format(cont, média))
    else:
        print('Erro digite S ou N')
print('Fim')'''
