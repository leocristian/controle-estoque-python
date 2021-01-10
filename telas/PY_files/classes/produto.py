from random import randint


class Produto():

    _idNum = randint(0,60000)
    __slots__ = ['_id','_nome','_descricao','_preco','_qtd']
    def __init__(self,nome,descricao,preco,qtd):
        self._id = Produto._idNum
        self._nome = nome.upper()
        self._descricao = descricao
        self._preco = preco
        self._qtd = qtd 
        Produto._idNum+=1

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id = id

    @property
    def nome(self):
        return self._nome 

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def descriao(self):
        return self._descricao

    @descriao.setter
    def descricao(self,descriao):
        self._descricao = descriao

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self,preco):
        self._preco = preco

    @property
    def qtd(self):
        return self._qtd

    @qtd.setter
    def qtd(self,qtd):
        self._qtd = qtd
