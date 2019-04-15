import sys

from vk_tools import VkTools
from design import auth_design
from PyQt5 import QtCore, QtGui, QtWidgets

    
class Auth(QtWidgets.QMainWindow, auth_design.Ui_MainWindow, VkTools):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.auth_btn.clicked.connect(self.authentication)

    def get_key(self):
        secret_key, ok = self.show_input_dialog()
        if ok:
            return secret_key

    def show_input_dialog(self):
        return QtWidgets.QInputDialog.getText(self, 'Secret KEY', 'ENTER KEY')

    def authentication(self):
        login = self.login_input.text()
        password = self.password_input.text()
        self.vk_auth(login=login, password=password, auth_handler=self.auth_handler)
        self.clear_input_fields()
   
    def clear_input_fields(self):
        self.login_input.clear()
        self.password_input.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Auth()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()