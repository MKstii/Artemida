import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget

from windows.CardListWindow import CardListWindow
from windows.MainWindow import MainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1440, 864)
        
        # Создаем стек виджетов, куда поместим все окна для удобного переключения
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Создаем окна
        self.main_menu = MainWindow(self)
        self.card_list_menu = CardListWindow(self)

        # Добавляем окна в стек
        self.stacked_widget.addWidget(self.main_menu)
        self.stacked_widget.addWidget(self.card_list_menu)

        # Устанавливаем главное окно
        self.stacked_widget.setCurrentWidget(self.main_menu)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())