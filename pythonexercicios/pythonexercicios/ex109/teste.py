# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


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
