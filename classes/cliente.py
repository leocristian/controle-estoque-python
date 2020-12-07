import estoque
from estoque import *

class Cliente():

    _idCliente = 0
    __slots__ = ['_pessoa']

    def __init__(self, _pessoa):
        self._pessoa = _pessoa
        Cliente._idCliente += 1
    
    def verProdutos(self):
        estoque = Estoque()
        estoque.listar()



