import sqlite3

conn = sqlite3.connect('wellnest.db')



def create_table():

    # Tabel for User Table Test
    conn.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT, Name TEXT, Age INTEGER, gender TEXT, email TEXT, phone INTEGER, address TEXT, city TEXT, state TEXT, zip INTEGER, country TEXT, PRIMARY KEY(username))')
    conn.commit()
    conn.close()

create_table()


