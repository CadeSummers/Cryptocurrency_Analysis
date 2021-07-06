import sqlite3
import time
from crypto_analysis import get_coin_info

#grabbing coin_info
coin_info = get_coin_info()


# #adding name into coin_info as explicit dictionary input, rather than coin name as key to data about coin (easier sql input)
# for coin_name in coin_info:
#     coin_info[coin_name] = {"name" : coin_name}

#creation / connect of the database in current directory
coin_db = sqlite3.connect('cryptocurrencies.db')

#creation of a cursor instance
c = coin_db.cursor()

current_time = time.time()

#error check for invalid cryptocurrency index length
if len(coin_info) < 100:
    print("Error: Invalid Coin Info Dictionary Length")
    exit()

for coin in coin_info:

    
    coin_record = [(coin, coin_info[coin]["symbol"], coin_info[coin]["rank"], coin_info[coin]["price"], current_time)]

    #inserting values into table
    c.executemany("""INSERT INTO coins VALUES(
        ?,
        ?,
        ?,
        ?,
        ?
    );""", coin_record)

    print(coin_record)


#commits changes to database
coin_db.commit()

#close connection
coin_db.close()

print(coin_info)