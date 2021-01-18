from .estoque import Estoque

__author__ = "Lucas Vinicius, Rubenilson de Sousa, Leonardo Cristian"
__licence__= "GPL"
__email__= "vinicius.lucas@ufpi.edu.br"
__version__= "1.0.0.1"

'''
    A Classe Cliente cria um objeto do tipo Cliente
'''

class Cliente():

    _idCliente = 0
    __slots__ = ['_pessoa','_listaProdutos','_id']

    def __init__(self, _pessoa):
        self._pessoa = _pessoa
        self._listaProdutos = []
        self._id = Cliente._idCliente
        Cliente._idCliente += 1

    '''
        Atributos
        ____
        _pessoa: variavel do tipo Pessoa
        _listaProdutos: lista de produtos
        _id: variavel do tipo inteiro
    '''

    @property
    def id(self):
        return self._id

    @property
    def pessoa(self):
        return self._pessoa

    @id.setter
    def id(self,id):
        self._id = id

    @property
    def listaProdutos(self):
        return self._listaProdutos
    
    def verProdutos(self):
        estoque = Estoque()
        estoque.listar()

    '''
        Funcao verProdutos mostra na tela a lista de produtos cadastrados no Estoque

        Parametros
        ____
        sem parametros alem do self
        ____
        Variaveis
        ____
        estoque: Objeto do tipo Estoque
    '''



