import datetime
from .produto import Produto

__author__ = "Lucas Vinicius, Rubenilson de Sousa, Leonardo Cristian"
__licence__= "GPL"
__email__= "vinicius.lucas@ufpi.edu.br"
__version__= "1.0.0.1"

'''
    A Classe Estoque cria um objeto do tipo Estoque
'''

class Estoque():
    _qtdProdutos = 0
    _produtos = []

    def __init__(self,):
        self._data_abertura = datetime.datetime.today()
        self._historico = []
        self._historico.append("A data de abertuda do estoque e: {}".format(self._data_abertura))

        '''
           Atributos
           ____
           data_abertura: variavel do tipo time
           _historico: lista de operacoes realizadas 
        '''  

    @property
    def produtos(self):
        return Estoque._produtos
    
    @property
    def historico(self):
        return self._historico


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
    '''
        Funcao armazenar objetos produtos dentro da lista de produtos e atualiza a operacao feita no historico

        Parametros
        ____
        produto: Objeto do tipo produto
        ____
        Variaveis
        ____
        achou: Variavel do tipo Boolena
        ____
        Retorno
        ____
        Sem Retornos
    '''    

    def listar(self):
        for p in Estoque._produtos:
            if(p.qtd > 0):
                print("-----------------")
                print("Id: ",p.id)
                print("Nome: ",p.nome)
                print("quantidade: ",p.qtd)

        '''
            Funcao listar mostra na tela as informacoes de cada produto armazado no estoque

            Parametros
            ____
            sem parametros alem do self
            ____
            Variaveis
            ____
            p: variavel do tipo Produto
        '''

    def remover(self,produtoName,qtdRetirar):
        '''
            Funcao remover da lista um produto da lista com sua quantidade a ser retirada

            Parametros
            ____
            produtoName: variavel do tipo String
            qtdRetirar: variavel do tipo inteiro
            ____
            Variaveis
            ____
            p: variavel do tipo Produto
        '''
        verif = 0
        for p in Estoque._produtos:
            if(p.nome == produtoName.upper()):
                if(qtdRetirar <= p.qtd):
                    p.qtd -= qtdRetirar
                    self._historico.append("Remocao de {} efetuada. quantidade atual: {}".format(p.nome,p.qtd))
                    verif = 1
                else:
                    print("Nao foi possivel efetuar operacao, quantidade no estoque inferior a solicitada")
        return verif