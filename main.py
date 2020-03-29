from PySide2.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QPushButton

import sys

from login.login_dialog import LoginWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.belepve = False

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QHBoxLayout(central_widget)

        self.category_layout = QVBoxLayout()
        gomb1 = QPushButton()
        self.category_layout.addWidget(gomb1)
        self.item_layout = QVBoxLayout()
        gomb2 = QPushButton()
        self.item_layout.addWidget(gomb2)
        self.details_layout = QVBoxLayout()
        gomb3 = QPushButton()
        self.details_layout.addWidget(gomb3)

        if not self.belepve:
            belepes = LoginWindow(self)

            if belepes.exec_():
                print("dialóg lefutott")
                self.change_mainwindow_layout()
            else:
                print("Ki kellene lépni")
                self.close()

    def closeEvent(self, event):
        print("Kilépés")
        sys.exit()


    def change_mainwindow_layout(self):

        self.main_layout.addLayout(self.category_layout)
        self.main_layout.addLayout(self.item_layout)
        self.main_layout.addLayout(self.details_layout)
        # self.login_widget = None

    def Login_clicked(self):
        print("Login clicked")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()