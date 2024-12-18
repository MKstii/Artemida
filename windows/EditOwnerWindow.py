from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui import Ui_editOwner
from db_operations import update_owner, get_owner

# Окно редактирования владельца
class EditOwnerWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_editOwner()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.close_application)
        self.ui.pushButton_6.clicked.connect(self.save_and_back)
        self.current_owner_id = None

    def load_owner_data(self, owner_id):
        self.current_owner_id = owner_id
        owner_data = get_owner(owner_id)
        if owner_data:
            self.ui.lineEdit_3.setText(owner_data[2])
            self.ui.lineEdit_4.setText(owner_data[3])
            self.ui.lineEdit_5.setText(owner_data[4])
            self.ui.lineEdit_6.setText(owner_data[0])
            self.ui.lineEdit_7.setText(owner_data[1])
            self.ui.label_7.setText(f"{owner_data[2]} {owner_data[3]} {owner_data[4]}")

    def save_and_back(self):
        if not self.current_owner_id:
            QMessageBox.warning(self, "Ошибка", "Владелец не выбран!")
            return

        patronymic = self.ui.lineEdit_3.text()
        phone = self.ui.lineEdit_4.text()
        email = self.ui.lineEdit_5.text()
        lastname = self.ui.lineEdit_6.text()
        name = self.ui.lineEdit_7.text()

        if not lastname or not name:
            QMessageBox.warning(self, "Ошибка", "Фамилия и имя обязательны для заполнения!")
            return

        try:
            update_owner(self.current_owner_id, lastname, name, patronymic, phone, email)
            QMessageBox.information(self, "Успех", "Данные владельца обновлены!")
            
            # Обновляем информацию в окне создания питомца
            self.parent.create_pet.set_owner(
                self.current_owner_id, 
                f"{lastname} {name} {patronymic}"
            )
            
            # Возвращаемся к окну создания питомца
            self.parent.stacked_widget.setCurrentWidget(self.parent.create_pet)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при сохранении: {str(e)}")

    def close_application(self):
        self.parent.close()
