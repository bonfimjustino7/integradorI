from PyQt5 import QtWidgets, uic
from controller.views import get_users


class LoginForm(object):
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.form = uic.loadUi('gui/login/login.ui')
        self.form.pushButton.clicked.connect(self.entrar)
        self.form.pushButton_2.clicked.connect(self.cancelar)

    def show(self):
        self.form.show()
        self.app.exec()

    def cancelar(self):
        self.app.exit()

    def entrar(self):
        if self.form.lineEdit.text() and self.form.lineEdit_2.text():
            usuario = self.form.lineEdit.text()
            senha = self.form.lineEdit_2.text()
            if get_users(usuario, senha):
                print(f"Usuário: {usuario}\nSenha: {senha}")
                QtWidgets.QMessageBox.about(self.form, 'Logado com Sucesso', 'Olá, Bem vindo ao nosso sistema de Vendas.')
            else:
                QtWidgets.QMessageBox.about(self.form, 'Alerta',
                                            'Dados inválidos. Informe um usuário e senha válidos.')
        else:
            QtWidgets.QMessageBox.about(self.form, 'Alerta',
                                        'Informe o usuário e senha.')

