# Linguagem de Programação II
# Atividade Contínua 02 - Classes e Herança
#
# e-mail: nome.sobrenome@aluno.faculdadeimpacta.com.br


"""
Implementar aqui as cinco classes filhas de Mamifero ou Reptil,
de acordo com o caso, conforme dado no diagrama apresentado no padrão UML.

Os atributos específicos de cada classe filha devem ser recebidos
como parâmetros no momento da criação, a única exceção é o número de vidas
do gato, que sempre começa em 7.

Os métodos de cada classe filha devem sempre RETORNAR uma string
no seguinte formato '<nome do animal> <método em questão no gerúndio>'
Sem nenhuma pontuação, conforme os exemplos a seguir.

Exemplo:
método trocar_pele() retorna '<nome> trocando de pele'
método dormir() retorna '<nome> dormindo'
método miar() retorna '<nome> miando'
Onde <nome> é o nome dado para cada animal (o valor atributo nome de
cada instância, não o nome da classe)

"""


class Reptil:
    """
    Classe mãe - não deve ser editada
    """
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return '{} ainda não atingiu maturidade sexual'.format(self.nome)


class Mamifero:
    """
    Classe mãe - não deve ser editada
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata

    def correr(self):
        return '{} correndo'.format(self.nome)

    def mamar(self):
        if self.idade <= 1:
            return '{} mamando'.format(self.nome)
        else:
            return '{} já desmamou'.format(self.nome)


class Camaleao(Reptil):
    """
    Exemplo de solução do exercício:

    Além dos atributos da classe mãe, possui o atributo:
    inseto_favorito, do tipo string.

    Implementa os métodos específicos:
    mudar_de_cor() e comer_inseto()
    """
    def __init__(self, nome, cor, idade, inseto_favorito):
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)


class Cavalo(<classe_mae>):
    """
    Além dos atributos da classe mãe, possui o atributo:
    cor_crina, do tipo string.

    Implementa os métodos específicos:
    galopar() e relinchar()
    """
    pass


class Cobra(<classe_mae>):
    """
    Além dos atributos da classe mãe, possui o atributo:
    veneno, do tipo booleano.

    Implementa os métodos específicos:
    rastejar() e trocar_pele()
    """
    pass


class Cachorro(<classe_mae>):
    """
    Além dos atributos da classe mãe, possui o atributo:
    raca, do tipo string. (raça, porém sem o ç)

    Implementa os métodos específicos:
    latir() e rosnar()
    """
    pass


class Jacare(<classe_mae>):
    """
    Além dos atributos da classe mãe, possui o atributo:
    num_dentes, do tipo inteiro.

    Implementa os métodos específicos:
    atacar() e dormir()
    """
    pass


class Gato(<classe_mae>):
    """
    Além dos atributos da classe mãe, possui o atributo:
    vidas, do tipo inteiro.

    Implementa os métodos específicos:
    miar() e morrer()

    No método morrer, você deve verificar quantas vidas o gato ainda
    tem sobrando, se for igual a zero, retornar:
    '<nome> morreu'
    se ainda houver vidas sobrando, retirar uma vida (que começa em 7),
    e retornar:
    '<nome> tem <vidas> vidas sobrando'
    Onde <vidas> é o número de vidas restantes do gato em questão.
    """
    pass
