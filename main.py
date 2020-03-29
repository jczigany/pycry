from PySide2.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QPushButton, QAction

import sys

from login.login_dialog import LoginWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.create_menu()

        self.main_layout = QHBoxLayout(central_widget)

        self.category_layout = QVBoxLayout()
        gomb1 = QPushButton("1. Gomb")
        self.category_layout.addWidget(gomb1)
        self.item_layout = QVBoxLayout()
        gomb2 = QPushButton("2. Gomb")
        self.item_layout.addWidget(gomb2)
        self.details_layout = QVBoxLayout()
        gomb3 = QPushButton("3. Gomb")
        self.details_layout.addWidget(gomb3)
        self.main_layout.addLayout(self.category_layout)
        self.main_layout.addLayout(self.item_layout)
        self.main_layout.addLayout(self.details_layout)

    def create_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")

        exit_action = QAction("Kilépés", file_menu)
        exit_action.triggered.connect(self.exit_action)
        file_menu.addAction(exit_action)

    def exit_action(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    belepes = LoginWindow(None)

    if belepes.exec_():
        win = MainWindow()
        win.show()
        app.exec_()
