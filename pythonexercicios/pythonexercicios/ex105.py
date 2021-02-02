#  Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
#  e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*n, sit=False):
    """

    @param n: várias notas
    @param sit: situação de acordo com as médias
    @return: dicionário contendo os campos apresentados
    """
    calc = dict()
    calc['total'] = len(n)
    calc['maior'] = max(n)
    calc['menor'] = min(n)
    calc['media'] = sum(n) / len(n)
    if sit:
        if calc['media'] >= 7:
            calc['situação'] = str('BOA')
        elif calc['media'] >= 5:
            calc['situação'] = str('REGULAR')
        else:
            calc['situação'] = str('RUIM')
    return calc


# programa principal

resposta = notas(5, 3, 2, sit=True)
print(resposta)
