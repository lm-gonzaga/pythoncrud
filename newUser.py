# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\newUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

connect = mysql.connector.connect(
    host='db3.super10.com.br',
    user='ludwig.gonzaga',
    password='61u7Mfy&iS#x',
    database='tests'
)


class Ui_newUser(object):
    def setupUi(self, newUser):
        newUser.setObjectName("newUser")
        newUser.setWindowModality(QtCore.Qt.NonModal)
        newUser.resize(554, 279)
        font = QtGui.QFont()
        font.setFamily("Arial")
        newUser.setFont(font)
        # newUser.setSizeGripEnabled(False)
        # newUser.setModal(False)
        self.labelName = QtWidgets.QLabel(newUser)
        self.labelName.setGeometry(QtCore.QRect(90, 90, 61, 21))
        self.labelName.setObjectName("labelName")
        self.labelEmail = QtWidgets.QLabel(newUser)
        self.labelEmail.setGeometry(QtCore.QRect(90, 120, 61, 21))
        self.labelEmail.setObjectName("labelEmail")
        self.labelPass = QtWidgets.QLabel(newUser)
        self.labelPass.setGeometry(QtCore.QRect(90, 150, 61, 21))
        self.labelPass.setObjectName("labelPass")
        self.labelTitulo = QtWidgets.QLabel(newUser)
        self.labelTitulo.setGeometry(QtCore.QRect(10, 10, 531, 51))
        self.labelTitulo.setObjectName("labelTitulo")
        self.lineName = QtWidgets.QLineEdit(newUser)
        self.lineName.setGeometry(QtCore.QRect(160, 90, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineName.setFont(font)
        self.lineName.setObjectName("lineName")
        self.lineEmail = QtWidgets.QLineEdit(newUser)
        self.lineEmail.setGeometry(QtCore.QRect(160, 120, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEmail.setFont(font)
        self.lineEmail.setObjectName("lineEmail")
        self.linePass = QtWidgets.QLineEdit(newUser)
        self.linePass.setGeometry(QtCore.QRect(160, 150, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.linePass.setFont(font)
        self.linePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePass.setObjectName("linePass")
        self.btnCadastrar = QtWidgets.QPushButton(newUser)
        self.btnCadastrar.setGeometry(QtCore.QRect(40, 210, 101, 41))
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.btnSair = QtWidgets.QPushButton(newUser)
        self.btnSair.setGeometry(QtCore.QRect(400, 210, 121, 41))
        self.btnSair.setObjectName("btnSair")

        self.retranslateUi(newUser)
        self.btnSair.clicked.connect(newUser.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(newUser)
        self.btnCadastrar.clicked.connect(self.cadastrar)

    def retranslateUi(self, newUser):
        _translate = QtCore.QCoreApplication.translate
        newUser.setWindowTitle(_translate("newUser", "Novo Usuário"))
        self.labelName.setText(_translate("newUser", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">Nome:</span></p></body></html>"))
        self.labelEmail.setText(_translate("newUser", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">E-mail:</span></p></body></html>"))
        self.labelPass.setText(_translate("newUser", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">Senha:</span></p></body></html>"))
        self.labelTitulo.setText(_translate("newUser", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Novo Usuário</span></p></body></html>"))
        self.btnCadastrar.setText(_translate("newUser", "Cadastrar"))
        self.btnSair.setText(_translate("newUser", "Sair"))

    def cadastrar(self):
        name = str(self.lineName.text())
        email = str(self.lineEmail.text())
        password = str(self.linePass.text())

        print("O nome inserido foi: " + name)
        print("O e-mail inserido foi: " + email)
        print("A senha inserida foi: " + password)

        cursor = connect.cursor()

        comando = f'INSERT INTO user (name, pass, email) VALUES ("{name}","{password}","{email}");'
        cursor.execute(comando)
        connect.commit()

        cursor.close()

        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Dados inseridos")
        msg.setText("Nome inserido: " + name + " " + "Email inserido: " + email)
        msg.exec()

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Principal = QtWidgets.QMainWindow()
        ui = Ui_newUser()
        ui.setupUi(Principal)
        Principal.show()
        sys.exit(app.exec_())
