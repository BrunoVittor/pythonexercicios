# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não informar o valor.\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não informar o valor.\033[m')
            continue
        else:
            return n


num1 = leiaInt('Digite um inteiro: ')
num2 = leiaFloat('Digite um float: ')
print(f'O valor inteiro digitado foi {num1}')
print(f'O valor float digitado foi {num2}')
