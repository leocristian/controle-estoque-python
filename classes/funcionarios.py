import produto
from produto import *
import pessoa
from pessoa import *

class Funcionario():

    _idFuncionario = 0
    __slots__ = ['_pessoa', '_username', '_senha']

    def __init__(self, _pessoa, _username, _senha):
        self._pessoa = _pessoa
        Funcionario._idFuncionario += 1
        self._username = _username
        self._senha = _senha

    def cadastroProdutos(self, nome, descricao, preco):
        listaProdutos = []
        idProduto = qtd = 1
        produto = Produto(idProduto, nome, descricao, preco, qtd)
        listaProdutos.append(produto)

    def getAtributos(self):
        print("-" * 10)
        print(f"Nome: {self._pessoa.nome}")
        print(f"CPF: {self._pessoa.cpf}")
        print("-" * 10)

p1 = Pessoa("leonardo", '123', 'aaa', '234', 21, 'leo@gmail.com')
f1 = Funcionario(p1, 'leo123', '1234')

p2 = Pessoa("Cristian", '321', 'bbb', '84756', 24, 'cc@gmail.com')
f2 = Funcionario(p2, 'cris123', '2345')

f1.getAtributos()
f2.getAtributos()


