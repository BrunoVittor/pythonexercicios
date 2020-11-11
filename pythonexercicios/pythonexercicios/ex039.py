# Faça um programa que leia o ano de nascimento de um jovem e informe:
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

'''nacimento = int(input('Digite o ano do seu nacimento: '))
if nacimento > 2002:
    diferenca = nacimento - 2002
    print('Você ainda vai se alistar ! faltam {} Anos para seu alistamento.'.format(diferenca))
elif nacimento == 2002:
    print('Você está no ano do alistamento !')
elif nacimento < 2002:
    diferenca = 2002 - nacimento
    print('Você já foi dispensado')'''

nascimento = int(input('Digite o ano de nascimento: '))
if nascimento > 2003:
    diferenca = nascimento - 2003
    print(f'Ele não têm idade para se alistar !!! e faltam {diferenca} anos')
elif nascimento == 2003:
    print('Você está no ano de alistamento !!!')
elif nascimento < 2003:
    diferenca = 2003 - nascimento
    print(f'Ele já foi dispensado á {diferenca} ano')
