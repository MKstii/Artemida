from PyQt5.QtWidgets import QMainWindow

from ui import Ui_MainWindow

# Окно главного меню
class MainWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.popup = None
        self.ui.pushButton_3.clicked.connect(self.close_application)
        self.ui.pushButton_2.clicked.connect(self.show_card_list)

    def show_card_list(self):
        self.parent.stacked_widget.setCurrentWidget(self.parent.card_list_menu)

    def close_application(self):
        self.parent.close()