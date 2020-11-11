# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções para conversão:
         [ 1 ] Para binário
         [ 2 ] Para octal
         [ 3 ] hexadecimal''')
opcao = int(input('Sua opção é: '))
if opcao == 1:
    print('O número {} convertido para BINÁRIO é {} !'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} convertido para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} convertido em HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    print('Você digitou uma opção \033[31mINVÁLIDA\033[m !!!! Digite novamente')
