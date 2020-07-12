from api_bot import *
import copy




def compare(first_exchange,second_exchange):
    #set the min arbitrage percentage we will consider
    arbi_list = {}

    threshold = 2
    upper = 30


    for first in first_exchange:
        for second in second_exchange:
            if first['symbol'] == second['symbol']:
                bid_on_first = float(first['bid'])
                ask_on_first = float(first['ask'])
                bid_on_second = float(second['bid'])
                ask_on_second = float(second['ask'])
                bid_ask_on_first = (bid_on_first/ask_on_second - 1)*100 #If we sell on first and buy on second
                bid_ask_on_second = (bid_on_second/ask_on_first - 1)*100 #If we buy on first and sell on second
                if (bid_ask_on_first) > threshold and bid_ask_on_first < upper:
                    arbi_list[(first['symbol'],"Buy " + second['exchange'] + " Sell " + first['exchange'])] = str(round(bid_ask_on_first,2))  + '%'
                elif (bid_ask_on_second)  > threshold and (bid_ask_on_second) < upper:
                    arbi_list[(first['symbol'],"Buy " + first['exchange'] + " Sell " + second['exchange'])] = str(round(bid_ask_on_second,2))  + '%'
    return arbi_list

list = [binance(),huobi(),ftx(),okex(),bitfinex(),kucoin()]

def execution(list):
    arbitrage_list = []
    deepcopy_list = copy.deepcopy(list)
    ii = 0

    for i in list:
        list = list[1:]
        for k in list:
            if k != i:
                ii += len(compare(i,k))
                if len(compare(i,k)) != 0:
                    arbitrage_list.append(compare(i,k))

    return arbitrage_list



(execution(list))
