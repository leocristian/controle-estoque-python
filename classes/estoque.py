import datetime
from produto import Produto

class Estoque():
    _qtdProdutos = 0
    _produtos = []

    def __init__(self,):
        self._data_abertura = datetime.datetime.today()
        self._historico = []

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
        achou = False
        for p in Estoque._produtos:
            if(p.nome == produtoName.upper()):
                achou = True
                if(qtdRetirar <= p.qtd):
                    p.qtd -= qtdRetirar
                    self._historico.append("Remoção de {} efetuada. quantidade atual: {}".format(p.nome,p.qtd))
                else:
                    print("não foi possivel efetuar operação estoque do protudo em falta")

    def buscar(self,produtoName):
        achou = False
        for p in Estoque._produtos:
            if(p.nome == produtoName.upper() and p.qtd > 0):
                return p

        if(not achou):
            return False



# e1 = Estoque()

# p1 = Produto('nescau','um pote de nescau',12.5,2)
# e1.armazenar(p1)

# p2 = Produto('nescau','um pote de nescau',12.5,2)
# e1.armazenar(p2)

# p3 = Produto('farinha','um pote de farinha',12.5,1)
# e1.armazenar(p3)


# e1.remover('nescau',2)
# e1.listar()

# e1.mostraHistorico()