from grab_others import grab_others
from toptendatagrab import toptengdatagrab

#function to merge dictionaries in seperate files
def merge():
    coindict = toptengdatagrab()
    otherdict = grab_others()
    coindict.update(otherdict)
    return coindict

#main to test output
def main():
    coindict = merge()
    print(coindict)

main()