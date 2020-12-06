import produto
from produto import *
import pessoa
from pessoa import *

class Funcionario():

    _idFuncionario = 0
    __slots__ = ['_pessoa']

    def __init__(self, pessoa):
        self._pessoa = pessoa
        Funcionario._idFuncionario += 1

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
f1 = Funcionario(p1)

p2 = Pessoa("Cristian", '321', 'bbb', '84756', 24, 'cc@gmail.com')
f2 = Funcionario(p2)

f1.getAtributos()
f2.getAtributos()


