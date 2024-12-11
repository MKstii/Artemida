import sqlite3

# Создаем или открываем базу данных
conn = sqlite3.connect('artemida.db')
cursor = conn.cursor()

# Создание таблицы PET_LIST
cursor.execute('''
CREATE TABLE IF NOT EXISTS PET_LIST (
    pet_ID INTEGER PRIMARY KEY,
    owner_ID INTEGER,
    pet_name TEXT NOT NULL,
    owner_FIO TEXT NOT NULL,
    FOREIGN KEY (owner_ID) REFERENCES OWNER_DETAILS(owner_ID)
)
''')

# Создание таблицы OWNER_DETAILS
cursor.execute('''
CREATE TABLE IF NOT EXISTS OWNER_DETAILS (
    owner_ID INTEGER PRIMARY KEY,
    owner_lastname TEXT NOT NULL,
    owner_name TEXT NOT NULL,
    owner_patronymic TEXT,
    owner_phone TEXT,
    owner_email TEXT
)
''')

# Создание таблицы PET_DETAILS
cursor.execute('''
CREATE TABLE IF NOT EXISTS PET_DETAILS (
    pet_ID INTEGER PRIMARY KEY,
    owner_ID INTEGER,
    pet_name TEXT NOT NULL,
    pet_type TEXT,
    pet_sex TEXT,
    pet_birthday date,
    pet_age TEXT,
    pet_breed TEXT,
    pet_color TEXT,
    pet_weight INTEGER,
    pet_features TEXT,
    pet_visit date,
    FOREIGN KEY (pet_visit) REFERENCES VISIT_DETAILS(pet_visit),
    FOREIGN KEY (owner_ID) REFERENCES OWNER_DETAILS(owner_ID)
)
''')

# Создание таблицы VISIT_DETAILS
cursor.execute('''
CREATE TABLE IF NOT EXISTS VISIT_DETAILS (
    pet_visit date PRIMARY KEY,
    pet_complaints TEXT,
    pet_diagnosis TEXT,
    pet_analyses TEXT,
    pet_treatment TEXT
)
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных и таблицы успешно созданы!")
