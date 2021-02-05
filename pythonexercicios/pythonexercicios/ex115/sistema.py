from lib.interface import *
from lib.arquivo import *

arq = 'cadastro.txt'

if not arquivoExiste(arq): # se o arquivo não existir
    arquivoCreate(arq) # será criado um novo arquivo

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print("Erro! Digite uma opção válida")
