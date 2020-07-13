import datetime

from binance.client import Client
from market_depth import *

#Generate from Binance
BinanceKey = {'api_key': '<Your API_KEYS>',
    'api_secret':'<Your API_SECRET>'}
#from binance.client import Client

def bot_execution(arbitrage_list):
    number_of_arbitrage_pairs = len(arbitrage_list)
    print ("-----------------------------------------")
    print ("There are ", number_of_arbitrage_pairs,"of arbitrage pairs")
    for i in arbitrage_list:
        print(i)
    print ("-----------------------------------------")
    
    quantity = 100 # to be determined 
    for group in arbitrage_list:
        for each in group:
            if "Binance" in each[1]:

                symbol = each[0]
                if "Buy Binance" in each[1]:
                    print("Buying", symbol, "on Binance at Market")
                    #client.order_market_buy(symbol= symbol, quantity = quantity)
                elif "Sell Binance" in each[1]:
                    #client.order_market_sell(symbol= symbol,quantity = quantity)
                    print("Selling", symbol, "on Binance at Market")


bot_execution(final_list(market_depth(execution(list))))
