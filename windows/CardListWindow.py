from PyQt5.QtWidgets import QMainWindow

from ui import Ui_cardList
from dataBase import load_data_to_table

# Окно списка карточек
class CardListWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_cardList()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.back_main_menu)
        self.ui.pushButton_2.clicked.connect(self.close_application)

        load_data_to_table(self.ui.tableWidget)

    def back_main_menu(self):
        self.parent.stacked_widget.setCurrentWidget(self.parent.main_menu)

    def close_application(self):
        self.parent.close()