##File to export information to csv
import csv
from crypto_analysis import get_coin_info

#initialize information from webscraping
coin_info = get_coin_info()

#separating coin_info in the names and dictionary values of the coins
coin_names = coin_info.keys()
coin_values = coin_info.values()

# for name in coin_names:
#     print(name)

# for value in coin_values:
#     print(value)

with open ("CryptoCurrencyInfo.csv", mode="w") as csv_file:
    fieldnames = ["name", "rank", "price", "symbol"]
    dwriter = csv.DictWriter(csv_file, fieldnames)
    dwriter.writeheader()

    #write nested dictionary to csv
    # for coin in coin_info:
    #     writer.writerow({field: coin_info[coin].get(field) or coin for field in fieldnames})

    for value in coin_values:
        print("writing", str(value), " to csv file")
        dwriter.writerow(value)


