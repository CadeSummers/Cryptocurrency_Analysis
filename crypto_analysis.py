from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

###Project Start: 6/14/21
###Project Last Updated: 6/21/21

####### Functions #######

#TODO this function does not work properly, but the for loop below does -- figure out why
#parsing top ten cryptocurrencies and other crypto currencies slightly different per website design -- This function grabs the top ten cryptocurrencies and their prices more easily. Similar to body of main.
def grab_top_ten():

    names2 = []
    prices2 = []

    #for loop iterating through all elements of toptendata
    for element in toptendata:

        #convert element of type bs4 tag, to string
        element = str(element)

        #the index of the string which contains the name variable occurs following the "/currencies/" text in the html of the website
        name_start = element.find("/currencies/")

        #the index of the end of the string follows this piece of text: ""><div class=\"sc-16r8icm-0\"
        name_end = element.find("/markets/")

        #find the dollar sign value
        price_start = element.find("$")

        #find the decimal (cents) value and add 3 to account for the cents value we want to grab
        price_end = element.find(".") + 3
        names2.append(element[name_start:name_end])
        prices2.append(element[price_start:price_end])

        if len(names2) == len(prices2):
            top_ten_key_info = zip(names2, prices2)

        for item in top_ten_key_info:
            item[0].strip("/currencies")
            print(item)
        
        return top_ten_key_info


####### Globals & Initialization #######


#initialization of the project, gaining info we need
url = "https://coinmarketcap.com/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = bs(html, "html.parser") #lxml or html.parser
text = soup.prettify()


######## TOTAL DATA GRAB ########

#grabs table row data from coinmarketcap.com and saves to variable named data
data = soup.find_all("tr")

#initialization of two lists to store the price and name of each cryptocurrency
names = []
prices = []

#for loop iterating through all elements of data
for element in data:

    #convert element of type bs4 tag, to string
    element = str(element)

    #the index of the string which contains the name variable occurs following the "/currencies/" text in the html of the website
    name_start = element.find("/currencies/")

    #the index of the end of the string follows this piece of text: ""><div class=\"sc-16r8icm-0\"
    name_end = element.find("><div class=\"sc-16r8icm-0\"")

    #find the dollar sign value
    price_start = element.find("$")

    #find the decimal (cents) value and add 3 to account for the cents value we want to grab
    price_end = element.find(".") + 3
    names.append(element[name_start:name_end])
    prices.append(element[price_start:price_end])

if len(names) == len(prices):
    key_info = zip(names, prices)

for item in key_info:
    item[0].strip("/currencies")
    #print(item)


######## TOP TEN DATA GRAB ########


#grabs the data for the top ten cryptocurrencies
toptendata = soup.find_all("div", {"class" : "price___3rj7O"})

names2 = []
prices2 = []

#for loop iterating through all elements of toptendata
for element in toptendata:

    #convert element of type bs4 tag, to string
    element = str(element)

    #the index of the string which contains the name variable occurs following the "/currencies/" text in the html of the website
    name_start = element.find("/currencies/")

    #the index of the end of the string follows this piece of text: ""><div class=\"sc-16r8icm-0\"
    name_end = element.find("/markets/")

    #find the dollar sign value
    price_start = element.find("$")

    #find the decimal (cents) value and add 3 to account for the cents value we want to grab
    price_end = element.find(".") + 3
    names2.append(element[name_start:name_end])
    prices2.append(element[price_start:price_end])

if len(names2) == len(prices2):
    top_ten_key_info = zip(names2, prices2)

for item in top_ten_key_info:
    item[0].strip("/currencies")
    print(item)



