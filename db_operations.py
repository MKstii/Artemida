import sqlite3

def create_owner(lastname, name, patronymic, phone, email):
    conn = sqlite3.connect('db/artemida.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO OWNER_DETAILS (owner_lastname, owner_name, owner_patronymic, owner_phone, owner_email)
    VALUES (?, ?, ?, ?, ?)
    ''', (lastname, name, patronymic, phone, email))
    
    owner_id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    return owner_id

def update_owner(owner_id, lastname, name, patronymic, phone, email):
    conn = sqlite3.connect('db/artemida.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE OWNER_DETAILS 
    SET owner_lastname=?, owner_name=?, owner_patronymic=?, owner_phone=?, owner_email=?
    WHERE owner_ID=?
    ''', (lastname, name, patronymic, phone, email, owner_id))
    
    conn.commit()
    conn.close()

def get_owner(owner_id):
    conn = sqlite3.connect('db/artemida.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT owner_lastname, owner_name, owner_patronymic, owner_phone, owner_email
    FROM OWNER_DETAILS
    WHERE owner_ID=?
    ''', (owner_id,))
    
    owner = cursor.fetchone()
    conn.close()
    
    return owner if owner else None

def get_all_owners():
    conn = sqlite3.connect('db/artemida.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT owner_ID, owner_lastname, owner_name, owner_patronymic
    FROM OWNER_DETAILS
    ORDER BY owner_lastname, owner_name
    ''')
    
    owners = cursor.fetchall()
    conn.close()
    
    return owners
