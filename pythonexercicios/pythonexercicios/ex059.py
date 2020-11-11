# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
print('=' * 15)
opcao = 0
while opcao != 5:
    print('''O que deseja fazer:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior número
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>>>selecione a opção: '''))
    if opcao == 1:
        soma = primeiro + segundo
        print('{} + {} = {}'.format(primeiro, segundo, soma))
    elif opcao == 2:
        multi = primeiro * segundo
        print('{} * {} = {}'.format(primeiro, segundo, multi))
    elif opcao == 3:
        if primeiro > segundo:
            print('O maior numero é {}'.format(primeiro))
        else:
            print('o maior número é {}'.format(segundo))
    elif opcao == 4:
        print('Informe os números novamente')
        primeiro = int(input('Digite o primeiro valor: '))
        segundo = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando ...')
    else:
        print('Opção inválida, tente novamente !!!!')
print('=' * 15)
print('Fim')
