import sqlite3
import time
from merge_coin_dicts import get_coin_info

#grabbing coin_info
coin_info = get_coin_info()

#creation / connect of the database in current directory
coin_db = sqlite3.connect('cryptocurrencies.db')

#creation of a cursor instance
c = coin_db.cursor()

#store time as unix time for database
current_time = time.time()

#error check for invalid cryptocurrency index length
if len(coin_info) < 100:
    print("Error: Invalid Coin Info Dictionary Length")
    exit()

#for all coins in summary dict
for coin in coin_info:
    
    #record to be added into database
    coin_record = [(coin, coin_info[coin]["symbol"], coin_info[coin]["rank"], coin_info[coin]["price"], current_time)]

    #inserting values into table
    c.executemany("""INSERT INTO coins VALUES(
        ?,
        ?,
        ?,
        ?,
        ?
    );""", coin_record)

    #test output
    #print(coin_record)


#commits changes to database
coin_db.commit()

#close connection
coin_db.close()

#test output
#print(coin_info)