import sqlite3

#creation / connect of the database in current directory
coin_db = sqlite3.connect('cryptocurrencies.db')

#creation of a cursor instance
c = coin_db.cursor()

#execution of SQL creating new table coins
c.execute("""CREATE TABLE coins (
    name TEXT,
    symbol TEXT,
    rank INTEGER,
    price REAL,
    date REAL
)""")

#commits changes to database
coin_db.commit()

#close connection
coin_db.close()

#no error print statement
print("database created successfully")