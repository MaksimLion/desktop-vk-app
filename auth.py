import sys
import vk_tools

from design import auth_design
from PyQt5 import QtCore, QtGui, QtWidgets

    
class Auth(QtWidgets.QMainWindow, auth_design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.auth_btn.clicked.connect(self.authentication)

    def show_input_key_dialog(self):
        self.secret_key, ok = QtWidgets.QInputDialog.getText(self, 'Secret KEY', 'Enter key')
        if ok:
            pass

    def authentication(self):
        login = self.login_input.text()
        password = self.password_input.text()
        vk_tools.vk_auth(login=login, password=password)
        # self.show_input_key_dialog()
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