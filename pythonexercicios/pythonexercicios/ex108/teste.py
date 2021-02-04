# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from moeda import aumentar, diminuir, dobro, metade, moeda

valor = float(input('Digite o valor: R$ '))
taxa = int(input('Digite  a taxa: '))
resultado_com_aumento = aumentar(valor, taxa)
resultado_com_desconto = diminuir(valor, taxa)
resultado_com_dobro = dobro(valor)
resultado_com_metade = metade(valor)

print(f'O valor {moeda(valor)} com um aumento de {taxa}% fica {moeda(resultado_com_aumento)}.')
print(f'O valor {moeda(valor)} com um desconto de {taxa}% fica {moeda(resultado_com_desconto)}.')
print(f'O dobro do valor {moeda(valor)} é de {moeda(resultado_com_dobro)}.')
print(f'A metade do valor {moeda(valor)} é de {moeda(resultado_com_metade)}.')
