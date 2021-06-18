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
            if "price" in string:
                
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
text = soup.prettify()

#represents the start of specific section of page to hold coin prices
start = text.find("<script id=\"__NEXT_DATA__\" type=\"application/json\">")


#limit data to what's useful to us, roughly speaking
text = text[start:]
end = text.find("</script>") #end of script tag, after initializing the text to find above, the text to end at being the following script is sufficient
text = text[:end]

#split text on basic metric and print to dev for eval
text = text.split(":")

#hold list of prices_list
prices_list = []

grabbed = False

#for loop to identify key information
for item in text:
    #if our text contains "Buy$", note that the following numeric item is the value we desire to capture
    
    if grabbed:
        prices_list.append(item)
        grabbed = False
    
    if "price" in item:
        #append item to prices_list
        grabbed = True

grabbed = False

name_list = []

#take an int index of the item in prices_list, and change it to be split on the $denoter
for item in text:

    if grabbed:
        name_list.append(item)
        grabbed = False

    if "name" in item:
        #append item to prices_list
        grabbed = True

print(len(text))
#grab(prices_list)
print(name_list)
print(prices_list)

print(len(name_list))
print(len(prices_list))
#print(text)

#print("\n", prices_list)
