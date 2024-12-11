import sys
from dataBase import load_data_to_table
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, uic

from ui import Ui_MainWindow, Ui_cardList


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWind = self
        self.ChangeUI(Ui_MainWindow())
        self.popup = None
        self.ui.pushButton_3.clicked.connect(self.close_application)

        self.ui.pushButton_2.clicked.connect(self.load_data)

    def ChangeUI(self, UI):
        self.ui = UI
        self.ui.setupUi(self)

    def close_application(self):
        self.close()

    def load_data(self):
        load_data_to_table(self.ui.tableWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())