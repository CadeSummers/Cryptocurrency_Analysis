from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

###Project Start: 6/14/21
###Project Last Updated: 6/24/21

###Ultimate Goal: analyze whether negative language in news/media headlines has significant correlation with price change of cryptocurrency
    #Sub Goal: analyze if the change is positive or negative correlation, or just either (absolute value of change)
    #Sub Goal: analyze which currencies are more or less effected. In effect, which coin has the most "hype"
###This file contains data which grabs cryptocurrency information

####### Functions #######


####### Globals & Initialization #######


#initialization of the project, gaining info we need
url = "https://coinmarketcap.com/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = bs(html, "html.parser") #lxml or html.parser
text = soup.prettify()


######## TOTAL DATA GRAB ########

#grabs html tag <tr> (table row) data from coinmarketcap.com and saves to variable named data
data = soup.find_all("tr")

#initialization of two lists to store the price and name of each cryptocurrency
names = []
prices = []

#for loop iterating through all elements of data
for element in data:

    #grab name, which is inside of the class cmc-link in our url
    name = element.find("a", class_="cmc-link")

    # append name to names
    names.append(name)

    #converting element to string-form of html, as it's easier to parse for the price
    element = element.prettify()

    #this comment starts the price (if this doesn't work try adding '$\n')
    price_start = element.find("<!-- -->")

    #cut down on the string such that it only contains information after the found start index
    element = element[price_start:]
    
    #find the immediate next decimal place, representative of the numbers decimal place
    price_end = element.find(".")

    #add the index of the decimal point (plus 3) to account for cents value
    price_end = price_end + 3

    #the price is the remaining string between the initial index of the html comment '<!-- -->' 
    price = element[:price_end]

    #remove excess information (html comments and excess spaces)
    price = price.replace("<!-- -->", "").strip()

    #append price to list prices
    prices.append(price)

#removes top ten prices
topten = prices[:11]

#stores all other prices in this
prices = prices[11:]

#remainder prices: I am keeping this for the time being in case it's needed or desired to be parsed later, but most likely this is a...
#TODO discard this extra information after determining usefulness
#print(topten)

#convert list of prices to floats
for i in range(len(prices)):
    prices[i] = float(prices[i])

#initialization of two lists to store links (which contains name of currency)
currencies = []
symbols = []

#remove first element of list, which is void. Remaining list contains only elements of class bs4.element.Tag
names.pop(0)

#parse throught the list of names to get the coin name and the symbol
for i in range(len(names)):
    
    #find the span with class crypto symbol, save it to symbol, and append the list symbols with its' value
    symbol = names[i].find("span", class_="crypto-symbol")
    symbols.append(symbol)

    #find all span tags in this particular element of the list
    spans = names[i].find_all("span")

    #if spans is an empty list (in this case, follows divergent website logic from other core groups), continue to next iteration and save the indices where there is an empty list
    if spans == []:
        continue
    else:
        #otherwise, append the list of currences with the middle element of spans, which happens to contain the name
        currencies.append(spans[1])

#split symbols list into list containing top ten data, and the other 90    
top_ten_symbols = symbols[:10]
symbols = symbols[10:]

#adjusts names of cryptocurrencies
coin_names = []
for coin in currencies:
    
    #convert coin to type string
    coin = str(coin)

    #find string indeces of span tags
    span_start = coin.find("<span>")
    span_end = coin.find("</span>")

    #cut string to be just key information
    coin_name = coin[span_start:span_end]
    
    #append to coin_names the coin name excluding "<span>"
    coin_names.append(coin_name[len("<span>"):])

#initialization of a list called coin symbols to store just thes coin symbol
coin_symbols = []

#for every index of symbols
#this method can be done without being a numeric index of the list symbols by just iterating
for coin_symbol in symbols:

    #cast to string
    coin_symbol = str(coin_symbol)

    #find the indices of the start and end of the symbol
    span_start = coin_symbol.find("<span class=\"crypto-symbol\">")
    span_end = coin_symbol.find("</span>")
    
    #remove all unnesscary info
    coin_symbol = coin_symbol[span_start:span_end]
    coin_symbol = coin_symbol[len("<span class=\"crypto-symbol\">"):]

    #append the element to coin_symbols
    coin_symbols.append(coin_symbol)

#initialize dict of coins
coin_dict = {}

#coin_names should be len 90, same as symbols and prices
for i in range(len(coin_names)):

    #insert into coin dictionary the name of each coin, it's rank (index i) and the associated price and symbol
    coin_dict[coin_names[i]] = {"rank": i + 11, "price" : prices[i], "symbol": coin_symbols[i]}

print(coin_dict)
