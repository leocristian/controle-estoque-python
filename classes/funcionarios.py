from produto import Produto
from pessoa import Pessoa
from estoque import Estoque
from cliente import Cliente

class Funcionario():

    _idFuncionario = 0
    __slots__ = ['_pessoa']
    _listaClientes = []

    def __init__(self, _pessoa):
        self._pessoa = _pessoa
        Funcionario._idFuncionario += 1

    def cadastroProduto(self, nome, descricao, preco):
        qtd = 1
        produto = Produto(nome, descricao, preco, qtd)
        estoque = Estoque()
        estoque.armazenar(produto)
        #estoque.listar()
    
    def cadastrarCliente(self, cliente):
        Funcionario._listaClientes.append(cliente)

    def venderProduto(self, cliente, produto):
        print("venda:")
        cliente._listaProdutos.append(produto)
        print(cliente._listaProdutos[0].nome)
        estoque = Estoque()
        estoque.remover(produto.nome, 1)

    def listarClientes(self):
        print("Lista de clientes:")
        for cliente in Funcionario._listaClientes:
            print(cliente._pessoa.nome)

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
f1.cadastrarCliente(c1)

f1.listarClientes()

f1.venderProduto(c1, prod1)

# f1.getAtributos()
# f2.getAtributos()


