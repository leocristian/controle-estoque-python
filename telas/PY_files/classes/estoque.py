import datetime
from .produto import Produto

class Estoque():
    _qtdProdutos = 0
    _produtos = []

    def __init__(self,):
        self._data_abertura = datetime.datetime.today()
        self._historico = []

    @property
    def produtos(self):
        return Estoque._produtos

    def mostraHistorico(self):
        print("A data de abertuda do estoque é: {}".format(self._data_abertura))
        for t in self._historico:
            print('- ',t)

    def armazenar(self,produto):
        achou = False
        for p in Estoque._produtos:
            if(p.nome == produto.nome.upper()):
                p.qtd += produto.qtd
                achou = True
                self._historico.append("Armazenamento de {} recebido. quantidade atual: {}".format(p.nome,p.qtd))
        if(not achou):
            Estoque._produtos.append(produto)
            self._historico.append("Novo produto armazenado, {} recebido. quantidade atual: {}".format(produto.nome.upper(),produto.qtd))

    def listar(self):
        for p in Estoque._produtos:
            if(p.qtd > 0):
                print("-----------------")
                print("Id: ",p.id)
                print("Nome: ",p.nome)
                print("quantidade: ",p.qtd)

    def remover(self,produtoName,qtdRetirar):
        verif = 0
        for p in Estoque._produtos:
            if(p.nome == produtoName.upper()):
                if(qtdRetirar <= p.qtd):
                    p.qtd -= qtdRetirar
                    self._historico.append("Remoção de {} efetuada. quantidade atual: {}".format(p.nome,p.qtd))
                    verif = 1
                else:
                    print("não foi possivel efetuar operação, quantidade no estoque inferior a solicitada")
        return verif
