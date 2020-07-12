import datetime

from binance.client import Client
from market_depth import *

#Generate from Binance
BinanceKey = {'api_key': '<Your API_KEYS>',
    'api_secret':'<Your API_SECRET>'}
from binance.client import Client

def bot_execution(arbitrage_list):
    quantity = 100
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
