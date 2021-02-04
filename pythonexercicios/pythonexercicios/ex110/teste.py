# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.


from moeda import *

valor = float(input('Digite o valor: R$ '))
taxa = int(input('Digite  a taxa: '))
print(resumo(valor, taxa))
