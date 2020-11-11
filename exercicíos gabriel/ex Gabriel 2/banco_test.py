from banco import Cliente, Banco, Conta


def test_cria_cliente():
    try:
        c = Cliente('nome', 99999999, 'email@mail.com')
    except Exception:
        assert False, 'Erro ao criar o cliente'
    else:
        assert not hasattr(c, 'nome'), 'nome deve ser um atributo privado'
        assert not hasattr(c, 'telefone'), 'telefone deve ser um atributo privado'
        assert not hasattr(c, 'email'), 'email deve ser um atributo privado'


def test_nao_cria_cliente_tel():
    try:
        Cliente('nome', 'não é número', 'email@mail.com')
    except TypeError:
        assert True
    except Exception:
        assert False, 'Não lançou TypeError para telefone inválido'


def test_nao_cria_cliente_mail():
    try:
        Cliente('nome', 99999999, 'não é email')
    except ValueError:
        assert True
    except Exception:
        assert False, 'Não lançou ValueError para email inválido'


def test_get_nome():
    c = Cliente('nome', 99999999, 'email@mail.com')
    assert c.get_nome() == 'nome', 'Erro no getter de nome'


def test_get_telefone():
    c = Cliente('nome', 99999999, 'email@mail.com')
    assert c.get_telefone() == 99999999, 'Erro no getter de telefone'


def test_get_mail():
    c = Cliente('nome', 99999999, 'email@mail.com')
    assert c.get_email() == 'email@mail.com', 'Erro no getter de email'


def test_set_telefone():
    c = Cliente('nome', 99999999, 'email@mail.com')
    c.set_telefone(88888888)
    assert c.get_telefone() == 88888888, 'Erro no setter de telefone'


def test_set_telefone_erro():
    c = Cliente('nome', 99999999, 'email@mail.com')
    try:
        c.set_telefone('não é telefone')
    except TypeError:
        assert True
    except Exception:
        assert False, 'Não lançou um TypeError para telefone inválido'
    else:
        assert c.get_telefone() == 99999999


def test_set_email():
    c = Cliente('nome', 99999999, 'email@mail.com')
    c.set_email('outro@mail.com')
    assert c.get_email() == 'outro@mail.com', 'Erro no setter de email'


def test_set_email_erro():
    c = Cliente('nome', 99999999, 'email@mail.com')
    try:
        c.set_email('não é email')
    except ValueError:
        assert True
    except Exception:
        assert False, 'Não lançou um ValueError para email inválido'
    else:
        assert c.get_email() == 'email@email.com'


def test_cria_banco():
    try:
        b = Banco('nome')
    except Exception:
        assert False, 'Erro ao criar o Banco'
    else:
        assert not hasattr(b, 'nome'), 'nome deve ser um atributo privado'


def test_get_nome_banco():
    b = Banco('nome')
    assert b.get_nome() == 'nome', 'Erro getter de nome do banco'


def lista_contas_vazio():
    b = Banco('nome')
    assert len(b.lista_contas()) == 0, 'O banco deve começar sem nenhuma conta'


def lista_contas_com_contas():
    b = Banco('nome')
    c = Cliente('nome', 99999999, 'email@mail.com')
    b.abre_conta([c], 200)
    b.abre_conta([c], 300)
    assert len(b.lista_contas()) == 2, 'O banco deveria ter 2 contas'
    for cc in b.lista_contas():
        assert type(cc) == Conta, 'Deveria retornar uma lista de contas'


def test_abre_conta():
    b = Banco('nome')
    c = Cliente('nome', 99999999, 'email@mail.com')
    b.abre_conta([c], 100)
    ccs = b.lista_contas()
    assert len(ccs) == 1, 'O banco deveria ter 1 conta'
    assert type(ccs[0]) == Conta, 'Deveria retornar um objeto do tipo Conta'
    assert ccs[0].get_numero() == 1, 'A primeira conta deve ser a numero 1'


def test_abre_conta_2():
    b = Banco('nome')
    c = Cliente('nome', 99999999, 'email@mail.com')
    b.abre_conta([c], 100)
    b.abre_conta([c], 500)
    ccs = b.lista_contas()
    assert len(ccs) == 2, 'O banco deveria ter 2 contas'
    assert type(ccs[1]) == Conta, 'Deveria retornar um objeto do tipo Conta'
    assert ccs[1].get_numero() == 2, 'A segunda conta deve ser a numero 2'


def test_n_abre_conta():
    b = Banco('nome')
    c = Cliente('nome', 99999999, 'email@mail.com')
    try:
        b.abre_conta([c], -100)
    except ValueError:
        assert True
    except Exception:
        assert False, 'Não lançou um ValueError'
    ccs = b.lista_contas()
    assert len(ccs) == 0, 'Não deveria ter aberto a conta pois saldo_inical < 0'


def test_cria_conta():
    try:
        c = Cliente('nome', 99999999, 'email@mail.com')
        cc = Conta([c], 1, 0)
    except Exception:
        assert False, 'Erro ao criar conta'
    else:
        assert not hasattr(cc, 'clientes'), 'clientes deve ser privado'
        assert not hasattr(cc, 'numero'), 'numero deve ser privado'
        assert not hasattr(cc, 'saldo'), 'saldo deve ser privado'


def test_nao_cria_conta():
    try:
        c = Cliente('nome', 99999999, 'email@mail.com')
        Conta([c], 1, -1)
    except ValueError:
        assert True
    except Exception:
        assert False, 'Não lançou ValueError para saldo inválido'


def test_get_clientes():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 0)
    lista = cc.get_clientes()
    assert len(lista) == 1, 'Esta conta deveria ter apenas 1 cliente'
    assert lista[0].get_nome() == 'nome', 'Nome do cliente incorreto'
    assert lista[0].get_email() == 'email@mail.com', 'Email do cliente incorreto'
    assert lista[0].get_telefone() == 99999999, 'Telefone do cliente incorreto'


def test_get_numero():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 0)
    assert cc.get_numero() == 1, 'Número da conta incorreto'


def test_get_saldo():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    assert cc.get_saldo() == 100, 'Saldo da conta incorreto'


def teste_deposito():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    cc.deposito(200)
    assert cc.get_saldo() == 300, 'Saldo da conta incorreto'
    assert ('deposito', 200) in cc.extrato(), 'Depósito não registrado no extrato'


def teste_saque():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    cc.saque(50)
    assert cc.get_saldo() == 50, 'Saldo da conta incorreto'
    assert ('saque', 50) in cc.extrato(), 'Saque não registrado no extrato'


def teste_saque_err():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    try:
        cc.saque(150)
    except ValueError:
        assert cc.get_saldo() == 100, 'O saldo não deve ser alterado quando o saque for inválido'
        assert ('saque', 150) not in cc.extrato(), 'Um saque inválido não deve ser registrado no extrato'
    except Exception:
        assert False, 'Não lançou um ValueError para saque inválido'


def test_extrato():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    extrato = cc.extrato()
    assert type(extrato) == list, 'O extrato deve ser uma lista'
    assert len(extrato) == 1, 'O extrato deve conter apenas uma entrada para esse teste'
    assert ('saldo_inicial', 100) in extrato, 'Saque inicial não registrado no extrato'


def test_extrato_2():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 200)
    cc.saque(150)
    extrato = cc.extrato()
    assert len(extrato) == 2, 'O extrato deve conter duas entradas para esse teste'
    assert extrato[0] == ('saldo_inicial', 200), 'A primeira entrada está incorreta'
    assert extrato[1] == ('saque', 150), 'A segunda entrada está incorreta'
