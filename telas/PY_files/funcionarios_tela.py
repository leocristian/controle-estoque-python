# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'funcionarios_tela.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Funcionarios_Tela(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(130, 60, 401, 301))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 30, 301, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 371, 31, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 370, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.btnEscolherFunc = QtWidgets.QPushButton(self.centralwidget)
        self.btnEscolherFunc.setGeometry(QtCore.QRect(210, 410, 89, 25))
        self.btnEscolherFunc.setObjectName("btnEscolherFunc")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(330, 410, 89, 25))
        self.btnVoltar.setObjectName("btnVoltar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Selecione um funcionario pelo ID"))
        self.label_2.setText(_translate("MainWindow", "ID:"))
        self.btnEscolherFunc.setText(_translate("MainWindow", "Escolher"))
        self.btnVoltar.setText(_translate("MainWindow", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Funcionarios_Tela()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

