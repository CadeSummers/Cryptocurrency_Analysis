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

#grabs table row data from coinmarketcap.com and saves to variable named data
data = soup.find_all("tr")

#initialization of two lists to store the price and name of each cryptocurrency
names = []
prices = []

#for loop iterating through all elements of data
for element in data:

    #grab name, which is inside of the class cmc-link in our url
    name = element.find("a", class_="cmc-link")

    #TODO filter names information (long strip of bs4 tag information) into just currency name

    print(name)

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

    #TODO? Should I also include the symbol of each of these currencies?

    
print(len(names))
print(len(prices))
#print(names[1])
#print(names[-1])

#TODO most prices are here as numeric strings, but some still contain vast amounts of html. Top ten seem to have different logic, which is handled in toptendatagrab.py
print(prices)

#TODO convert prices to floats


