# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote
# e mantenha tudo funcionando.


from moeda import resumo
from dado import leiaDinheiro


valor = leiaDinheiro('Digite o valor: R$ ')
taxa = int(input('Digite  a taxa: '))
print(resumo(valor, taxa))
