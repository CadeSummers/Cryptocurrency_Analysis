from grab_others import grab_others
from toptendatagrab import toptengdatagrab

#function to merge dictionaries in seperate files
#TODO rename all files to more coherent information
def get_coin_info():
    #merges the coin_dicts from toptendatagrab and grab others and returns it as singular dictionary
    coindict = toptengdatagrab()
    otherdict = grab_others()
    coindict.update(otherdict)
    return coindict

