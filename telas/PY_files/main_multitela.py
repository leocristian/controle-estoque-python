import sys
import os
import socket
import json

import classes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from cadastrar_funcionario import Cadastrar_Funcionario

from funcionarios_tela import Funcionarios_Tela
from tela_inicial import Tela_Inicial
from menufuncionario import MenuFuncionario
from cadastrar_cliente_tela import cadastrar_cliente
from cadastrar_produto_tela import cadastroProduto
from listar_clientes_tela import listarClientes
from listar_produtos_tela import listarProdutos
from vender_produto_tela import venderProduto
from historico_estoque_tela import Historico

from classes.cliente import Cliente
from classes.funcionarios import Funcionario
from classes.pessoa import Pessoa
from classes.estoque import Estoque
from classes.produto import Produto

__author__ = "Lucas Vinicius, Rubenilson de Sousa, Leonardo Cristian"
__licence__= "GPL"
__email__= "leonardosclopes@gmail.com"
__version__= "1.0.0.1"

HOST, PORT = "localhost", 5000
sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

'''
    A classe Ui_main eh responsavel por fazer o gerenciamento de todas as telas
'''

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)
        
        '''
            Atributos
            ____
            QtStack: Uma pilha contendo todas as telas do sistema
            
        '''
        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.cadastrar_funcionario = Cadastrar_Funcionario()
        self.cadastrar_funcionario.setupUi(self.stack1)

        self.funcionarios_tela = Funcionarios_Tela()
        self.funcionarios_tela.setupUi(self.stack2)

        self.menufuncionario = MenuFuncionario()
        self.menufuncionario.setupUi(self.stack3)

        self.cadastrar_cliente_tela = cadastrar_cliente()
        self.cadastrar_cliente_tela.setupUi(self.stack4)

        self.listar_clientes_tela = listarClientes()
        self.listar_clientes_tela.setupUi(self.stack5)

        self.cadastrar_produto_tela = cadastroProduto()
        self.cadastrar_produto_tela.setupUi(self.stack6)

        self.listar_produtos_tela = listarProdutos()
        self.listar_produtos_tela.setupUi(self.stack7)

        self.vender_produto_tela = venderProduto()
        self.vender_produto_tela.setupUi(self.stack8)

        self.historico_estoque = Historico()
        self.historico_estoque.setupUi(self.stack9)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)

'''
    A classe main é responsável pelo controle dos botões,
    dos dados que serão mostrados em cada tela 
'''
class Main(QMainWindow, Ui_Main):
    sockObj.connect((HOST, PORT))
    print("Conexao estabelecida.")
    def __init__(self, parent=None):

        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.funcList = []
        self.clientList = []
        self.estoque = Estoque()

        '''
            Atributos
            ____
            funcList: Uma lista de todos os funcionários
            clientList: Uma lista de todos os clientes
            estoque: Objeto do tipo estoque que ira armazenar os produtos cadastrados
        '''

        self.tela_inicial.btnEntrar.clicked.connect(self.abrirTelaEntrar)
        self.tela_inicial.btnCadastrar.clicked.connect(self.abrirTelaCadastrarFuncionario)

        self.funcionarios_tela.btnVoltar.clicked.connect(self.voltarTelaFuncionarios)

        self.cadastrar_funcionario.cadastrarVoltar.clicked.connect(self.voltarTelaCadastro)
        self.cadastrar_funcionario.cadastrarFuncionario.clicked.connect(self.CadastrorDeFuncionario)

        self.menufuncionario.pushButton_7.clicked.connect(self.abrirTelaEntrar)
        
        self.cadastrar_cliente_tela.cadastrarFuncionario.clicked.connect(self.cadastrodeCliente)
        self.listar_clientes_tela.btnVoltar.clicked.connect(self.voltarMenuFuncionario)

        self.menufuncionario.btnCadCliente.clicked.connect(self.abrirTelaCadastrarCliente)
        self.menufuncionario.btnListarClientes.clicked.connect(self.telaClientes)
        self.menufuncionario.btnCadProduto.clicked.connect(self.telaCadastroProduto)
        self.menufuncionario.btnListarProduto.clicked.connect(self.telaProdutos)
        self.menufuncionario.btnVender.clicked.connect(self.telaVenderProduto)
        self.menufuncionario.btnHistorico.clicked.connect(self.telaVerHistorico)
        self.historico_estoque.btnVoltar.clicked.connect(self.voltarMenuFuncionarios)
        

        self.cadastrar_produto_tela.cadastrarFuncionario.clicked.connect(self.cadastroDeProduto)


    def cadPessoa(self):
        '''
            Metodo responsavel por cadastrar um objeto do tipo pessoa
            com os atributos digitados pelo usuario na tela de cadastrar funcionarios

            Retorno
            ____
            p: Objeto da classe Pessoa
        '''
        nome = self.cadastrar_funcionario.lineEdit.text()
        cpf = self.cadastrar_funcionario.lineEdit_2.text()
        end = self.cadastrar_funcionario.lineEdit_3.text()
        telefone = self.cadastrar_funcionario.lineEdit_4.text()
        idade = self.cadastrar_funcionario.lineEdit_5.text()
        email = self.cadastrar_funcionario.lineEdit_6.text()
        p = None
        if not(nome == '' or cpf == '' or end == '' or telefone == '' or idade == '' or email == ''):

            dadoEnviar = {"tipo": "funcionario", "nome": nome, "cpf": cpf, "end": end, "tel": telefone, "idade": idade, "email": email}

            dataJson = json.dumps(dadoEnviar)
            sockObj.sendall(bytes(dataJson, encoding="utf-8"))

            p = Pessoa(nome,cpf,end,telefone,idade,email)

            dadoRecebido = sockObj.recv(1024)

            print("dado recebido (cadPessoa): ", dadoRecebido.decode())
        
            QMessageBox.information(None,'POO2','Cadastro Realizado com Sucesso!!')
            self.cadastrar_funcionario.lineEdit.setText('')
            self.cadastrar_funcionario.lineEdit_2.setText('')
            self.cadastrar_funcionario.lineEdit_3.setText('')
            self.cadastrar_funcionario.lineEdit_4.setText('')
            self.cadastrar_funcionario.lineEdit_5.setText('')
            self.cadastrar_funcionario.lineEdit_6.setText('')        

        return p
    def cadPessoaCliente(self):
        '''
            Metodo responsavel por cadastrar um objeto do tipo pessoa
            com os atributos da classe Pessoa digitados pelo usuario na tela de cadastrar clientes
            
            Retorno
            ____
            p: Objeto da classe Pessoa
        '''
        nome = self.cadastrar_cliente_tela.lineEdit.text()
        cpf = self.cadastrar_cliente_tela.lineEdit_2.text()
        end = self.cadastrar_cliente_tela.lineEdit_3.text()
        telefone = self.cadastrar_cliente_tela.lineEdit_4.text()
        idade = self.cadastrar_cliente_tela.lineEdit_5.text()
        email = self.cadastrar_cliente_tela.lineEdit_6.text()
        p = None
        if not(nome == '' or cpf == '' or end == '' or telefone == '' or idade == '' or email == ''):

            dadoEnviar = {"tipo": "cliente", "nome": nome, "cpf": cpf, "end": end, "tel": telefone, "idade": idade, "email": email}

            dataJson = json.dumps(dadoEnviar)   
            sockObj.sendall(bytes(dataJson, encoding="utf-8"))

            dadoRecebido = sockObj.recv(1024)

            print("dado recebido (cadCliente): ", dadoRecebido.decode())

            p = dadoRecebido.decode()

            QMessageBox.information(None,'POO2','Cadastro Realizado com Sucesso!!')
            self.cadastrar_cliente_tela.lineEdit.setText('')
            self.cadastrar_cliente_tela.lineEdit_2.setText('')
            self.cadastrar_cliente_tela.lineEdit_3.setText('')
            self.cadastrar_cliente_tela.lineEdit_4.setText('')
            self.cadastrar_cliente_tela.lineEdit_5.setText('')
            self.cadastrar_cliente_tela.lineEdit_6.setText('')
        return p

    def telaCadastroProduto(self):
        self.QtStack.setCurrentIndex(6)
        self.cadastrar_produto_tela.cadastrarVoltar.clicked.connect(self.voltarMenuFuncionario)

    def telaProdutos(self):
        '''
            Metodo responsavel por mostrar os produtos que estao no estoque
        '''
        sockObj.send("mostrarEstoque".encode())
    
        produtos = sockObj.recv(1024)
        print("dado recebido (telaProdutos): ", produtos.decode())

        produtosStr = produtos.decode()
        
        self.listar_produtos_tela.listWidget.clear()
        if(produtosStr == "vazia"):
            QMessageBox.information(None,'POO2','Sem produtos cadastrados!')
        else:
            listaProdServer = produtosStr.split(";")

            print("lista prod: ", listaProdServer)

            self.QtStack.setCurrentIndex(7)

            for i in listaProdServer:
                print(type(i))
                iDict = json.loads(i)
                print(type(iDict))

                self.listar_produtos_tela.listWidget.addItem(f'ID: -- Nome: {iDict["nome"]} -- Qtd: {iDict["qtd"]} -- Preco: {iDict["preco"]}')
            
            self.listar_produtos_tela.btnVoltar.clicked.connect(self.voltarMenuFuncionario)

    def cadastrarProduto(self):
        '''
            metodo responsavel por armazenar os atributos digitados pelo usuario na tela de cadastrar produtos

            Retorno
            ____
            prod: Objeto da classe Produto
        '''
        nome = self.cadastrar_produto_tela.lineEdit.text()
        desc = self.cadastrar_produto_tela.lineEdit_2.text()
        preco = self.cadastrar_produto_tela.lineEdit_3.text()
        qtd = int(self.cadastrar_produto_tela.lineEdit_4.text())

        prod = None
        if not(nome == '' or desc == '' or preco == '' or qtd == ''):

            dadoEnviar = {"tipo": "produto", "nome": nome, "desc": desc, "preco": preco, "qtd": qtd}

            dataJson = json.dumps(dadoEnviar)
            sockObj.sendall(bytes(dataJson, encoding="utf-8"))

            dadoRecebido = sockObj.recv(1024)

            print("dado recebido (cadProdutos): ", dadoRecebido.decode())

            prod = dadoRecebido.decode()
            #prod = Produto(nome, desc, preco, qtd)
            QMessageBox.information(None,'POO2','Cadastro Realizado com Sucesso!!')
            self.cadastrar_produto_tela.lineEdit.setText('')
            self.cadastrar_produto_tela.lineEdit_2.setText('')
            self.cadastrar_produto_tela.lineEdit_3.setText('')
            self.cadastrar_produto_tela.lineEdit_4.setText('')
        return prod

    def cadastroDeProduto(self):
        '''
            Metodo responsavel por armazenar o produto no estoque
        '''
        prod = self.cadastrarProduto()

        if prod == None:
            QMessageBox.information(None,'POO2','Todos os Campos Devem ser Preenchidos!!')
        else:
            #self.estoque.armazenar(prod)
            print("dado recebido: ", prod)
#--------------------------------------------------------------------------- TELA VENDER PRODUTO

    def vendaProduto(self):
        '''
            Metodo reponsavel por realizar o a venda de um produto a um cliente

            Atributos
            ____
            ID: Variavel inteira que ira guardar o id do cliente a qual o produto sera vendido
            nomeP: String que ira armazenar o nome do produto
            qtd: Variavel inteira que ira armazenar a quantidade de produtos para venda
        '''

        clienteID = self.vender_produto_tela.lineEdit.text()
        nomeProd = self.vender_produto_tela.lineEdit_2.text()
        qtdProd = self.vender_produto_tela.lineEdit_3.text()

        print("id cli: ", clienteID)
        print("Nome prod: ", nomeProd)
        print("qtd: ", qtdProd)

        if not(clienteID == '' or nomeProd == '' or qtdProd == ''):
            qtdProd = int(qtdProd)
            clienteID = int(clienteID)

            objVender = {"tipo": "venderProduto", "idCliente": clienteID, "nomeProduto": nomeProd, "qtdProd": qtdProd}

            objVenderJson = json.dumps(objVender)
            sockObj.sendall(bytes(objVenderJson, encoding="utf-8"))

            dadoRecebido = sockObj.recv(1024)

            print("dado recebido (venderProduto): ", dadoRecebido.decode())

            if(dadoRecebido.decode() == "produtoVendido"):
                QMessageBox.information(None,'POO2','Produto Vendido!')

                self.vender_produto_tela.lineEdit.setText('')
                self.vender_produto_tela.lineEdit_2.setText('')
                self.vender_produto_tela.lineEdit_3.setText('')
            else:
                QMessageBox.information(None,'POO2','ERRO! Operação não concluida. Verifique os dados inseridos.')
    
                
    def telaVenderProduto(self):
        self.vender_produto_tela.listWidget.clear()
        self.vender_produto_tela.listWidget_2.clear()

        sockObj.send("mostrarClientes".encode())

        clientes = sockObj.recv(1024)

        print("dado recebido (telaVenderProduto): ", clientes.decode())
        clientesStr = clientes.decode() # converte os dados (bytes) em string

        if(clientesStr == "vazia"):
            QMessageBox.information(None,'POO2','Sem produtos ou clientes cadastrados!')
        else:

            listaClienteServer = clientesStr.split(",")
    
            self.QtStack.setCurrentIndex(8)
            # for i in self.estoque.produtos:
            #     print(i.nome)
            #     self.vender_produto_tela.listWidget_2.addItem(f"Nome: {i.nome} -- Qtd: {i.qtd}")

            countCli = 0
            for i in listaClienteServer:
                print("cliente: ", i)
                print(type(i))

                self.vender_produto_tela.listWidget.addItem(f"ID: {countCli}-- Nome: {i}")
                countCli += 1
                
            self.vendaProduto()

            self.vender_produto_tela.btnVender.clicked.connect(self.telaVenderProduto)
            self.vender_produto_tela.btnVoltar.clicked.connect(self.voltarMenuFuncionario)

#------------------------------------------------------------------------------------------------------
    def cadastrodeCliente(self):
        '''
            Metodo reponsavel por armazenar o cliente na lista de clientes
        '''
        p1 = self.cadPessoaCliente()
        if p1 == None:
            QMessageBox.information(None,'POO2','Todos os Campos Devem ser Preenchidos!!')
        else: 
            print(p1)
            #self.clientList.append(p1["nome"])
            self.cadastrar_cliente_tela.cadastrarVoltar.clicked.connect(self.voltarMenuFuncionario)

    def CadastrorDeFuncionario(self):
        '''
            Metodo reponsavel por armazenar o funcionario na lista de funcionarios
        '''
        p1 = self.cadPessoa()
        if p1 == None:
            QMessageBox.information(None,'POO2','Todos os Campos Devem ser Preenchidos!!')
        else: 
            f1 = Funcionario(p1)
            self.funcList.append(f1)

    def abrirTelaCadastrarFuncionario(self):
        self.QtStack.setCurrentIndex(1)
        
    def EscolherFuncionario(self):
        '''
            Metodo reponsavel por exibir os funcionarios na tela
        '''
        sockObj.send("mostrarFuncionario".encode())

        funcionarios = sockObj.recv(1024)

        print("dado recebido (telaFunc): ", funcionarios.decode())
        funcionariosStr = funcionarios.decode() # converte os dados (bytes) em string

        if(funcionariosStr == "vazia"):
            QMessageBox.information(None,'POO2','Sem FuncionariosS cadastrados!')    
        else:
            listaFuncionariosServer = funcionariosStr.split(",")
    
            self.funcionarios_tela.listWidget.clear()
            countFunc = 0

            for i in listaFuncionariosServer:
                print("func: ", i)
                print(type(i))

                self.funcionarios_tela.listWidget.addItem(f"ID: {countFunc} -- Nome: {i}")
                countFunc += 1

            self.funcionarios_tela.btnEscolherFunc.clicked.connect(self.abrirMenuFuncionario)

    def telaClientes(self):
        '''
            Metodo responsavel por exibir os clientes na tela
        '''
        sockObj.send("mostrarClientes".encode())

        clientes = sockObj.recv(1024)

        print("dado recebido (telaClientes): ", clientes.decode())
        clientesStr = clientes.decode() # converte os dados (bytes) em string

        if(clientesStr == "vazia"):
            QMessageBox.information(None,'POO2','Sem clientes cadastrados!')    
        else:
            listaClienteServer = clientesStr.split(",")
    
            self.listar_clientes_tela.listWidget.clear()
            self.QtStack.setCurrentIndex(5)

            countCli = 0
            for i in listaClienteServer:
                print("cliente: ", i)
                print(type(i))

                self.listar_clientes_tela.listWidget.addItem(f"ID: {countCli}-- Nome: {i}")
                countCli += 1

    def abrirMenuFuncionario(self):
        '''
            Metodo reponsavel por abrir a tela do funcionario escolhido pelo usuario
        '''

        escolha = int(self.funcionarios_tela.lineEdit.text())

        funcEscolhido = self.retornaFunc(escolha)

        print(f'funcEscolhido: {funcEscolhido.pessoa.nome}')

        QMessageBox.information(None, 'POO2', 'Funcionário escolhido: '+ funcEscolhido.pessoa.nome)
        self.QtStack.setCurrentIndex(3)

    def voltarMenuFuncionario(self):
        self.QtStack.setCurrentIndex(3)

    def retornaFunc(self, escolha):
        '''
            Metodo responsavel por armazenar um funcinario escolhido pelo usuario

            retorno
            ____
            i: Objeto do tipo Funcionario
        '''

        for i in self.funcList:
            if (i.id == escolha):
                return i

    def abrirTelaCadastrarCliente(self):
        self.QtStack.setCurrentIndex(4)

    def abrirTelaEntrar(self):
        self.QtStack.setCurrentIndex(2)
        self.EscolherFuncionario()

    def voltarTelaFuncionarios(self):
        self.funcionarios_tela.listWidget.clear()
        self.QtStack.setCurrentIndex(0)

    def voltarTelaCadastro(self):
        self.QtStack.setCurrentIndex(0)

    def telaVerHistorico(self):
        self.QtStack.setCurrentIndex(9)
        self.historico_estoque.listWidget.clear()

        sockObj.send("mostrarHistorico".encode())

        histServerStr = sockObj.recv(1024)
        histServerStr = histServerStr.decode()

        if(histServerStr == "vazio"):
            print("Historico vazio")
        else:
            print("historico server: ", histServerStr)

            listHistServer = histServerStr.split(";")
    
        # self.historico_estoque.listView.appendRow(f"{text}")
            for his in listHistServer:
                self.historico_estoque.listWidget.addItem(f"{his}")


    def voltarMenuFuncionarios(self):
        self.QtStack.setCurrentIndex(3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())