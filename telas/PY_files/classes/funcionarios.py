from .produto import Produto
from .pessoa import Pessoa
from .estoque import Estoque
from .cliente import Cliente

class Funcionario():

    _idFuncionario = 0
    __slots__ = ['_pessoa','_id']
    _listaClientes = []

    def __init__(self, _pessoa):
        self._pessoa = _pessoa
        self._id = Funcionario._idFuncionario
        Funcionario._idFuncionario += 1
    
    # @property
    # def listaclientes(self):
    #     return Funcionario._listaClientes

    @property
    def pessoa(self):
        return self._pessoa

    @pessoa.setter
    def pessoa(self, pessoa):
        self._pessoa = pessoa
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def cadastroProduto(self, nome, descricao, preco, qtd, estoque):
        produto = Produto(nome, descricao, preco, qtd)
        estoque.armazenar(produto)
        #estoque.listar()
    
    def cadastrarCliente(self, cliente):
        Funcionario._listaClientes.append(cliente)

    def venderProduto(self, produto, qtd, estoque, idCliente):
        
        for cliente in Funcionario._listaClientes:
            if(cliente.id == idCliente):
                cliente.listaProdutos.append(produto)
                print(f"{produto} vendido para: {cliente.pessoa.nome}")
        estoque.remover(produto, qtd)

    @property
    def listaClientes(self):
        return Funcionario._listaClientes

    
    def listarClientes(self):
        print("Lista de clientes:")
        for cliente in Funcionario._listaClientes:
            print(f"ID: {cliente.id} -- Nome: {cliente._pessoa.nome}")

    def getAtributos(self):
        print("-" * 10)
        print(f"Nome: {self._pessoa.nome}")
        print(f"CPF: {self._pessoa.cpf}")
        print("-" * 10)

