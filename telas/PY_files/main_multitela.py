import sys
import os

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
from classes.cliente import Cliente
from classes.funcionarios import Funcionario
from classes.pessoa import Pessoa
from classes.estoque import Estoque
from classes.produto import Produto

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

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

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):

        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.funcList = []
        self.clientList = []

        self.estoque = Estoque()
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

        self.cadastrar_produto_tela.cadastrarFuncionario.clicked.connect(self.cadastroDeProduto)

    def cadPessoa(self):

        nome = self.cadastrar_funcionario.lineEdit.text()
        cpf = self.cadastrar_funcionario.lineEdit_2.text()
        end = self.cadastrar_funcionario.lineEdit_3.text()
        telefone = self.cadastrar_funcionario.lineEdit_4.text()
        idade = self.cadastrar_funcionario.lineEdit_5.text()
        email = self.cadastrar_funcionario.lineEdit_6.text()
        p = None
        if not(nome == '' or cpf == '' or end == '' or telefone == '' or idade == '' or email == ''):
            p = Pessoa(nome,cpf,end,telefone,idade,email)
            QMessageBox.information(None,'POO2','Cadastro Realizado com Sucesso!!')
            self.cadastrar_funcionario.lineEdit.setText('')
            self.cadastrar_funcionario.lineEdit_2.setText('')
            self.cadastrar_funcionario.lineEdit_3.setText('')
            self.cadastrar_funcionario.lineEdit_4.setText('')
            self.cadastrar_funcionario.lineEdit_5.setText('')
            self.cadastrar_funcionario.lineEdit_6.setText('')        

        return p
    def cadPessoaCliente(self):
        nome = self.cadastrar_cliente_tela.lineEdit.text()
        cpf = self.cadastrar_cliente_tela.lineEdit_2.text()
        end = self.cadastrar_cliente_tela.lineEdit_3.text()
        telefone = self.cadastrar_cliente_tela.lineEdit_4.text()
        idade = self.cadastrar_cliente_tela.lineEdit_5.text()
        email = self.cadastrar_cliente_tela.lineEdit_6.text()
        p = None
        if not(nome == '' or cpf == '' or end == '' or telefone == '' or idade == '' or email == ''):
            p = Pessoa(nome,cpf,end,telefone,idade,email)
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
        self.listar_produtos_tela.listWidget.clear()
        if(len(self.estoque.produtos) == 0):
            QMessageBox.information(None,'POO2','Sem produtos cadastrados!')
        else:
            self.QtStack.setCurrentIndex(7)
            for i in self.estoque.produtos:
                print(i.nome)
                self.listar_produtos_tela.listWidget.addItem(f"ID: {i.id} -- Nome: {i.nome}")
            
            self.listar_produtos_tela.btnVoltar.clicked.connect(self.voltarMenuFuncionario)
    def cadastrarProduto(self):
        nome = self.cadastrar_produto_tela.lineEdit.text()
        desc = self.cadastrar_produto_tela.lineEdit_2.text()
        preco = self.cadastrar_produto_tela.lineEdit_3.text()
        qtd = self.cadastrar_produto_tela.lineEdit_4.text()
        prod = None
        if not(nome == '' or desc == '' or preco == '' or qtd == ''):
            prod = Produto(nome, desc, preco, qtd)
            QMessageBox.information(None,'POO2','Cadastro Realizado com Sucesso!!')
            self.cadastrar_produto_tela.lineEdit.setText('')
            self.cadastrar_produto_tela.lineEdit_2.setText('')
            self.cadastrar_produto_tela.lineEdit_3.setText('')
            self.cadastrar_produto_tela.lineEdit_4.setText('')
        return prod
    def cadastroDeProduto(self):
        prod = self.cadastrarProduto()
        if prod == None:
            QMessageBox.information(None,'POO2','Todos os Campos Devem ser Preenchidos!!')
        else:
            self.estoque.armazenar(prod)
            print(prod.nome, prod.preco)

    def cadastrodeCliente(self):
        p1 = self.cadPessoaCliente()
        if p1 == None:
            QMessageBox.information(None,'POO2','Todos os Campos Devem ser Preenchidos!!')
        else: 
            p1 = Cliente(p1)
            print(p1.pessoa.nome, p1.pessoa.cpf)
            self.clientList.append(p1)

            self.cadastrar_cliente_tela.cadastrarVoltar.clicked.connect(self.voltarMenuFuncionario)

    def CadastrorDeFuncionario(self):
        
        p1 = self.cadPessoa()
        if p1 == None:
            QMessageBox.information(None,'POO2','Todos os Campos Devem ser Preenchidos!!')
        else: 
            f1 = Funcionario(p1)
            self.funcList.append(f1)

    def abrirTelaCadastrarFuncionario(self):
        self.QtStack.setCurrentIndex(1)
        
    def EscolherFuncionario(self):
        self.funcionarios_tela.listWidget.clear()
        if(len(self.funcList) == 0):
                #self.funcionarios_tela.listWidget.addItem('Sem funcionários cadastrados!')
                QMessageBox.information(None,'POO2','Sem funcionários cadastrados!')
        else:
            for i in self.funcList:
                self.funcionarios_tela.listWidget.addItem(f"ID: {i.id} -- Nome: {i.pessoa.nome}")

            self.funcionarios_tela.btnEscolherFunc.clicked.connect(self.abrirMenuFuncionario)
    def telaClientes(self):
        self.listar_clientes_tela.listWidget.clear()
        if(len(self.clientList) == 0):
            QMessageBox.information(None,'POO2','Sem clientes cadastrados!')
        else:
            self.QtStack.setCurrentIndex(5)
            for i in self.clientList:
                print(i.pessoa.nome)
                self.listar_clientes_tela.listWidget.addItem(f"ID: {i.id} -- Nome: {i.pessoa.nome}")
            
            

    def abrirMenuFuncionario(self):
        escolha = int(self.funcionarios_tela.lineEdit.text())

        funcEscolhido = self.retornaFunc(escolha)

        print(f'funcEscolhido: {funcEscolhido.pessoa.nome}')

        QMessageBox.information(None, 'POO2', 'Funcionário escolhido: '+ funcEscolhido.pessoa.nome)
        self.QtStack.setCurrentIndex(3)

    def voltarMenuFuncionario(self):
        self.QtStack.setCurrentIndex(3)

    def retornaFunc(self, escolha):
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())