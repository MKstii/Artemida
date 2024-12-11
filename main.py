import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, uic

from ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWind = self
        self.ChangeUI(Ui_MainWindow())
        self.popup = None
        self.ui.pushButton_3.clicked.connect(self.close_application)

    def ChangeUI(self, UI):
        self.ui = UI
        self.ui.setupUi(self)

    def close_application(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())