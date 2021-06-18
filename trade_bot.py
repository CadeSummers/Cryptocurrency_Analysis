from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

####### Functions #######

#grabs the prices_list values in a list of text objects
def grab(prices_list):
    #list to hold new prices_list 
    prices = []
    
    #base condition whether or not we want to grab a segment
    grab = False
    for segment in prices_list:

        for string in segment:

            #if grab is true
            if grab:
                #initialize grab to False ("we've 'grabbed' this segment")
                grab = False
                
                #now append to list segment
                prices.append(string)
                print(string)

            #if we come across the section to by, set grab bool to true, lets function know that on the NEXT iteration it needs to grab the segment we are looking for. This if searches for the value, the prior one actually grabs the segment.
            if string.endswith("Buy"):
                
                #segment ending in "Buy" is indicator next segment is valid price
                grab = True

    print("PRINT OF PRICES")
    print(prices)

####### Globals & Initialization #######

#initialization of the project, gaining info we need
url = "https://coinmarketcap.com/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = bs(html, "html.parser")
text = soup.get_text()

start = text.find("EventsWatchlistPortfolioFilters") #seems unique enough, don't you think?
found = text.find("...")

#limit data to what's useful to us, roughly speaking
#text = text[start:found]
#text = text[start:]

#split text on basic metric and print to dev for eval
text = text.split("%")

#hold list of prices_list
prices_list = []

#for loop to identify key information
for item in text:
    #if our text contains "Buy$", note that the following numeric item is the value we desire to capture
    if "Buy$" in item:
        #append item to prices_list
        prices_list.append(item)

#take an int index of the item in prices_list, and change it to be split on the $denoter
for item in range(len(prices_list)):
    prices_list[item] = prices_list[item].split("$")
    print(prices_list[item])

print(text)
#print(prices_list) #XRP8Polkadot8DOTBuy
grab(prices_list)

#print(text)

#print("\n", prices_list)
