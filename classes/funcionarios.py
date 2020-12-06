import produto, pessoa
from produto import *
from pessoa import *

class Funcionario():
    def __init__(self, pessoa, id):
        self.usuario = pessoa
        self.id = id

    def cadastroProdutos(self, nome, descricao, preco):
        idProduto = qtd = 1
        produto = Produto(idProduto, nome, descricao, preco, qtd)
        listaProdutos.append(produto)
        print(produto.nome)


