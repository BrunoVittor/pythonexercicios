# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.


def ajuda(com):
    help(com)


def linhas(msg):
    comp = len(msg) + 4
    print('~' * comp)
    print(f'  {msg}')
    print('~' * comp)


# programa principal
while True:
    linhas('SIETMA DE AJUDA PYHELP')
    comando = str(input('função ou lib: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
linhas('VOLTE SEMPRE !')
