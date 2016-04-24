
#Purpose: Purpose of this file is to get every 24 hrs crude oil, gold
# and bitcoin pricing data every 24 hrs.
# need to include the following packages before importing Quandl
# pip install numpy
# pip install pandas
# pip install requests
# pip install Quandl
# also need to add your own authtoken from Quandl in order to connect with Quandl APIs

#Note: users need to put their own Quandl key for authtoken in order to get the commodity
#data from quandl.

import Quandl
import time

def getCommodityPrice():
    #get crude oil data
    oilData = Quandl.get("OPEC/ORB", authtoken="xxxxxxxxxxxxxxxx")
    print (oilData.tail())
    print (oilData.head())
    oilData.to_csv('quandlcrudeoilData.csv')

    #get gold data.
    goldData = Quandl.get("BUNDESBANK/BBK01_WT5511", authtoken="xxxxxxxxxxxxxxxx")
    print (goldData.tail())
    print (goldData.head())
    goldData.to_csv('quandlgoldData.csv')

    #get copper data
    copperData = Quandl.get("LSE/COPA", authtoken="xxxxxxxxxxxxxxxx")
    print (copperData.tail())
    print (copperData.head())
    copperData.to_csv('quandlcopperData.csv')

    #get silver data
    silverData = Quandl.get("LBMA/SILVER", authtoken="xxxxxxxxxxxxxxxx")
    print (silverData.tail())
    print (silverData.head())
    silverData.to_csv('quandlsilverData.csv')

    #get bitcoin pricing data.
    bitcoinData = Quandl.get("BAVERAGE/USD", authtoken="xxxxxxxxxxxxxxxx")
    print (bitcoinData.tail())
    print (bitcoinData.head())
    bitcoinData.to_csv('bitcoindata.csv')

    time.sleep(86400) #sleep for a day

while True:
    getCommodityPrice()
