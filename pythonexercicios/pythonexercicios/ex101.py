# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 18:
        return f'Com a idade de {idade} anos, não vota !!!'
    elif idade >= 18 or idade > 65:
        return f'Com idade de {idade}anos, já pode votar !!!'
    else:
        return f'Com idade de {idade} anos, O voto é opcional !!!'


#programa principal !!!
votacao = int(input(f'Qual o ano do seu nascimento ? : '))
print(voto(votacao))
