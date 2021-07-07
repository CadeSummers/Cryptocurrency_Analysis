## grabs top ten cryptocurrencies

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

###Project Start: 6/14/21
###Project Last Updated: 6/21/21

####### Functions #######

def toptengdatagrab():

####### Initialization #######

    #initialization of the project, gaining info we need
    url = "https://coinmarketcap.com/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = bs(html, "html.parser") #lxml or html.parser

    ######## TOP TEN DATA GRAB ########
    
    #previously, function to call was this class top_ten_data = soup.find_all("div", {"class" : "price___3rj7O"})
    #New class for top 10: sc-131di3y-0 cLgOOr

    #grabs the data for the top ten cryptocurrencies, who have special class to grab them compared to others
    top_ten_data = soup.find_all("div", {"class" : "sc-131di3y-0 cLgOOr"})


    #initialization of lists
    names = []
    prices = []

    #for loop iterating through all elements of toptendata
    for element in top_ten_data:

        #convert element of type bs4 tag, to string
        element = str(element)

        #the index of the string which contains the name variable occurs following the "/currencies/" text in the html of the website
        name_start = element.find("/currencies/")

        #the index of the end of the string follows this piece of text: ""><div class=\"sc-16r8icm-0\"
        name_end = element.find("/markets/")

        #append name to list names
        names.append(element[name_start:name_end])

        #find the dollar sign value, indicating where the price occurs, and grab the index next to it (where the numeric piece begins)
        price_start = element.find("$") + 1

        #find price end, equivalent to the decimal place
        price_end = element.find(".")

        #if price end did not fail
        if price_end != -1:
            #add 3 to account for the cents value we want to grab
            price_end = price_end + 3

        #On occasion, prices can be kept as singular digit values (ie $1 instead of $1.00). This is/else statement is a simple check for that condition
        if price_end == -1:
            #index of price start is the first number
            coin_price = element[price_start]
        else:
            coin_price = element[price_start:price_end]

        if coin_price == "":
            print(element)
            print(element[price_end])

        #remove commas and excess spaces from values
        coin_price = coin_price.replace(",","")

        #convert coin price to float and append to list prices
        prices.append(float(coin_price))

    #initialize new list to store updated names
    coin_names = []

    #modifing name to be of one standard
    for name in names:
        #git rid of /currencies/ piece
        name = name[len("/currencies/"):]

        #edge case for specificaly updated information per website standard (sometimes coinmarketcap names updated versions of cryptocurrences with -new)
        name = name.replace("-new", "")
        
        #replace dashes with space
        name = name.replace("-", " ")
        name = name.title()

        #append modified name to new list
        coin_names.append(name)

    #grabs all paragraph tags in top ten data with class coin item symbol (this class contains our symbol text)
    top_ten_symbols_html = soup.find_all("p", {"class" : "sc-1eb5slv-0 gGIpIK coin-item-symbol"})

    #initialize empty list
    top_ten_symbols = []

    #grab text information from each row and append it to our list of top ten cryptocurrencies symbols. Type is of string.
    for symbol in top_ten_symbols_html:
        top_ten_symbols.append(symbol.text)

    #Creation of top_ten_coin_dict
    top_ten_coin_dict = {}

    #fill new dict with dict containing key information
    for i in range(len(coin_names)):
        top_ten_coin_dict[coin_names[i]] = {"rank" : i + 1, "price" : prices[i], "symbol" : top_ten_symbols[i]}

    return top_ten_coin_dict

#test print
#print(toptengdatagrab())