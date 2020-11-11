# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.














'''cont = str(input('Digite a expressão: '))
expressao = []
for simb in cont:
    if simb == '(':
        expressao.append('(')
    elif simb == ')':
        if len(expressao) > 0:
            expressao.pop()
        else:
            expressao.append(')')
            break
if len(expressao) == 0:
    print('Sua expressão está Correta')
else:
    print('Sua expressão está inválida')'''