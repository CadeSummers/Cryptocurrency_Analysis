##File to export information to csv
import csv
from merge_coin_dicts import get_coin_info

#initialize information from webscraping
coin_info = get_coin_info()

#separating coin_info in the names and dictionary values of the coins
coin_names = coin_info.keys()
coin_values = coin_info.values()

#write csv file
with open ("CryptoCurrencyInfo.csv", mode="w", newline="") as csv_file:

    #columns initialization
    fieldnames = ["name", "rank", "price", "symbol"]

    dwriter = csv.DictWriter(csv_file, fieldnames)
    dwriter.writeheader()

    #TODO cast coin_names to dictionary that binds field "name" to values of coin names, zip with value in coin_values and writerow to file
    #for all coins in coin_info
    for coin in coin_info:

        #grab the values of the coin info dict at the value of the string coin and store in values
        values = coin_info[coin]

        #initialize a new dictionary which binds the coin name to a key named "name"
        export_dict = {"name" : coin}

        #update the dict with the remaining values
        export_dict.update(values)
        
        #test output
        #print("writing", str(export_dict), " to csv file")
        
        #write new dictionary value to csv
        dwriter.writerow(export_dict)


