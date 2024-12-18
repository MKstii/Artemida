from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui import Ui_createOwner
from db_operations import create_owner

# Окно создания владельца
class CreateOwnerWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_createOwner()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.close_application)
        self.ui.pushButton_3.clicked.connect(self.save_and_back)

    def save_and_back(self):
        patronymic = self.ui.lineEdit_3.text()
        phone = self.ui.lineEdit_4.text()
        email = self.ui.lineEdit_5.text()
        lastname = self.ui.lineEdit_6.text()
        name = self.ui.lineEdit_7.text()

        if not lastname or not name:
            QMessageBox.warning(self, "Ошибка", "Фамилия и имя обязательны для заполнения!")
            return

        try:
            # Создаем нового владельца
            owner_id = create_owner(lastname, name, patronymic, phone, email)
            QMessageBox.information(self, "Успех", "Владелец успешно добавлен!")
            
            # Передаем ID владельца в окно создания питомца
            self.parent.create_pet.set_owner(owner_id, f"{lastname} {name} {patronymic}")

            # Очищаем поля
            self.clear_fields()
            # Возвращаемся к окну создания питомца
            self.parent.stacked_widget.setCurrentWidget(self.parent.create_pet)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при сохранении: {str(e)}")

    def clear_fields(self):
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()

    def close_application(self):
        self.parent.close()
