# Faça um programa que leia o ano de nascimento de um jovem e informe:
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nacimento = int(input('Digite o ano do seu nacimento: '))
if nacimento > 2002:
    diferenca = nacimento - 2002
    print('Você ainda vai se alistar ! faltam {} Anos para seu alistamento.'.format(diferenca))
elif nacimento == 2002:
    print('Você está no ano do alistamento !')
elif nacimento < 2002:
    diferenca = 2002 - nacimento
    print('Você já foi dispensado')

