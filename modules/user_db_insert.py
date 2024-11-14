import sqlite3

def insert_user(data):
    conn = sqlite3.connect('wellnest.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, password, Name, Age, gender, email, phone, address, city, state, zip, country)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['username'], data['password'], data['name'], data['age'], data['gender'], 
        data['email'], data['phone'], data['address'], data['city'], data['state'], 
        data['zip'], data['country']
    ))
    conn.commit()
    conn.close()