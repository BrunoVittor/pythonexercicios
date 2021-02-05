from pythonexercicios.ex115.lib.interface import cabecalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # se o arquivo existir será lido
        a.close()  # e depois fechado
    except FileNotFoundError:
        return False
    else:
        return True


def arquivoCreate(nome):
    try:
        a = open(nome, 'wt+')  # wt+ é o comando para a criação de um novo arquivo
        a.close()
    except:
        print('Ouve um erro na criação do arquivo.')
    else:
        print('Arquivo criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao cadastrar')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
