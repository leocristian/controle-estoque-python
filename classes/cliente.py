from estoque import *

class Cliente():

    _idCliente = 0
    __slots__ = ['_pessoa','_listaProdutos','_id']

    def __init__(self, _pessoa):
        self._pessoa = _pessoa
        self._listaProdutos = []
        self._id = Cliente._idCliente
        Cliente._idCliente += 1

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id = id

    @property
    def listaProdutos(self):
        return self._listaProdutos

    # @listaProdutos.setter
    # def listaProdutos(self,nomeProduto):
    #     self._listaProdutos.append(nomeProduto)
    
    def verProdutos(self):
        estoque = Estoque()
        estoque.listar()



