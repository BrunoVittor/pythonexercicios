# Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)


def leiaInt(n):
    ok = False
    valor = 0
    while True:
        n = str(input(n))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro ! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
