import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from cadastrar_funcionario import Cadastrar_Funcionario
from funcionarios_tela import Funcionarios_Tela
from tela_inicial import Tela_Inicial
from menufuncionario import MenuFuncionario
from cliente import Cliente
from funcionarios import Funcionario
from pessoa import Pessoa
from estoque import Estoque

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.cadastrar_funcionario = Cadastrar_Funcionario()
        self.cadastrar_funcionario.setupUi(self.stack1)

        self.funcionarios_tela = Funcionarios_Tela()
        self.funcionarios_tela.setupUi(self.stack2)

        self.menufuncionario = MenuFuncionario()
        self.menufuncionario.setupUi(self.stack3)



        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.funcList = []
        self.estoque = Estoque()

        self.tela_inicial.btnEntrar.clicked.connect(self.abrirTelaEntrar)
        self.tela_inicial.btnCadastrar.clicked.connect(self.abrirTelaCadastrarFuncionario)

        self.funcionarios_tela.btnVoltar.clicked.connect(self.voltarTelaFuncionarios)

        self.cadastrar_funcionario.cadastrarVoltar.clicked.connect(self.voltarTelaCadastro)
        self.cadastrar_funcionario.cadastrarFuncionario.clicked.connect(self.CadastrorDeFuncionario)

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
        if(len(self.funcList) == 0):
                # self.funcionarios_tela.listWidget.addItem('Sem funcionários cadastrados!')
                QMessageBox.information(None,'POO2','Sem funcionários cadastrados!')
        else:
            for i in self.funcList:
                self.funcionarios_tela.listWidget.addItem(f"ID: {i.id} -- Nome: {i.pessoa.nome}")

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