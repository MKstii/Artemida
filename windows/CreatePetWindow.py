from PyQt5.QtWidgets import QMainWindow
from ui import Ui_CreatePet
from db_operations import get_owner

# Окно создания новой карты
class CreatePetWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_CreatePet()
        self.ui.setupUi(self)
        self.ui.pushButton_7.clicked.connect(self.close_application)
        self.ui.pushButton_6.clicked.connect(self.back_main_menu)
        self.ui.pushButton_8.clicked.connect(self.handle_owner)
        
        # Инициализируем переменные для хранения информации о владельце
        self.current_owner_id = None
        self.current_owner_name = None

    def back_main_menu(self):
        self.parent.stacked_widget.setCurrentWidget(self.parent.main_menu)

    def handle_owner(self):
        if self.current_owner_id:
            # Если владелец уже выбран, открываем окно редактирования
            self.parent.edit_owner.load_owner_data(self.current_owner_id)
            self.parent.stacked_widget.setCurrentWidget(self.parent.edit_owner)
        else:
            # Если владельца нет, открываем окно создания
            self.parent.create_owner.clear_fields()
            self.parent.stacked_widget.setCurrentWidget(self.parent.create_owner)

    def set_owner(self, owner_id, owner_name):
        self.current_owner_id = owner_id
        self.current_owner_name = owner_name

    def close_application(self):
        self.parent.close()
