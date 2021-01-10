# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuFuncionario.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MenuFuncionario(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCadCliente = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadCliente.setGeometry(QtCore.QRect(190, 140, 111, 25))
        self.btnCadCliente.setObjectName("btnCadCliente")
        self.btnListarClientes = QtWidgets.QPushButton(self.centralwidget)
        self.btnListarClientes.setGeometry(QtCore.QRect(360, 140, 111, 25))
        self.btnListarClientes.setObjectName("btnListarClientes")
        self.btnCadProduto = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadProduto.setGeometry(QtCore.QRect(190, 180, 111, 25))
        self.btnCadProduto.setObjectName("btnCadProduto")
        self.btnListarProduto = QtWidgets.QPushButton(self.centralwidget)
        self.btnListarProduto.setGeometry(QtCore.QRect(360, 180, 111, 25))
        self.btnListarProduto.setObjectName("btnListarProduto")
        self.btnVender = QtWidgets.QPushButton(self.centralwidget)
        self.btnVender.setGeometry(QtCore.QRect(190, 220, 111, 25))
        self.btnVender.setObjectName("btnVender")
        self.btnHistorico = QtWidgets.QPushButton(self.centralwidget)
        self.btnHistorico.setGeometry(QtCore.QRect(360, 220, 111, 25))
        self.btnHistorico.setObjectName("btnHistorico")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(370, 320, 89, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 90, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnCadCliente.setText(_translate("MainWindow", "Cad. Cliente"))
        self.btnListarClientes.setText(_translate("MainWindow", "Listar Clientes"))
        self.btnCadProduto.setText(_translate("MainWindow", "Cad. Produto"))
        self.btnListarProduto.setText(_translate("MainWindow", "Listar Produtos"))
        self.btnVender.setText(_translate("MainWindow", "Vender Produto"))
        self.btnHistorico.setText(_translate("MainWindow", "Historico"))
        self.pushButton_7.setText(_translate("MainWindow", "Voltar"))
        self.label.setText(_translate("MainWindow", "Escolha uma operação"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MenuFuncionario()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

