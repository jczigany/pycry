from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QDialog

import sys


class LoginWindow(QDialog):
    def __init__(self, parent):
        super(LoginWindow, self).__init__(parent)
        self.setWindowTitle("Kérem adja meg a bejelentkezési adatokat")
        main_layout = QVBoxLayout(self)

        name_layout = QHBoxLayout()
        name_label = QLabel("E-mail cím vagy név:")
        self.name = QLineEdit()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name)
        main_layout.addLayout(name_layout)

        password_layout = QHBoxLayout()
        password_label = QLabel("Jelszó:")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password)
        main_layout.addLayout(password_layout)

        button_layout = QHBoxLayout()
        self.login_button = QPushButton("Bejelentkezés")
        self.cancel_button = QPushButton("Kiürít")
        self.exit_button = QPushButton("Kilépés")
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.exit_button)
        main_layout.addLayout(button_layout)

        self.login_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.form_clear)
        self.exit_button.clicked.connect(self.reject)

    def accept(self):
        if len(self.name.text()) and len(self.password.text()):
            print(f"Bejelentkezési név: {self.name.text()}")
            print(f"Jelszó: {self.password.text()}")
            # pass
            super(LoginWindow, self).accept()
        else:
            return

    def form_clear(self):
        self.name.clear()
        self.password.clear()
 
    def reject(self):
        super(LoginWindow, self).reject()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow(None)
    win.show()
    app.exec_()