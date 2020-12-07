import produto
from produto import *
import pessoa
from pessoa import *
import estoque
from estoque import *
import cliente
from cliente import *

class Funcionario():

    _idFuncionario = 0
    __slots__ = ['_pessoa']

    def __init__(self, _pessoa):
        self._pessoa = _pessoa
        Funcionario._idFuncionario += 1

    def cadastroProduto(self, nome, descricao, preco):
        qtd = 1
        produto = Produto(nome, descricao, preco, qtd)
        estoque = Estoque()
        estoque.armazenar(produto)
        #estoque.listar()
    
    def cadastrarCliente(self, nome, cpf, end, tel, idade, email):
        listaCliente = []
        pessoa = Pessoa(nome, cpf, end, tel, idade, email)
        cliente = Cliente(pessoa)
        listaCliente.append(cliente)

    def venderProduto(self, produto):
        pass

    def listarClientes(self, listaCliente):
        pass

    def getAtributos(self):
        print("-" * 10)
        print(f"Nome: {self._pessoa.nome}")
        print(f"CPF: {self._pessoa.cpf}")
        print("-" * 10)

p1 = Pessoa("leonardo", '123', 'aaa', '234', 21, 'leo@gmail.com')
f1 = Funcionario(p1)

p2 = Pessoa("Cristian", '321', 'bbb', '84756', 24, 'cc@gmail.com')
f2 = Funcionario(p2)

f1.cadastroProduto('arroz', 'branco', 2.90)
f1.cadastroProduto('miojo', 'um miojo', 1.75)

prod1 = Produto('arroz', 'branco', 2.90, 2)

p3 = Pessoa('joao', '567', 'dfdf', '53656', 23, 'joao@gmail.com')
c1 = Cliente(p3)

c1.verProdutos()

#f1.venderProduto(p1)

# f1.getAtributos()
# f2.getAtributos()


