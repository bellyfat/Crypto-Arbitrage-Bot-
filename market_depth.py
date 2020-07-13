from Arbitrage_Bot import *


def market_depth(a):
    order_book = []
    url_binance = "https://api.binance.com/api/v3/ticker/bookTicker?symbol=%s" #binance is ok
    url_kucoin = "https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=BTC-USDT"
    url_huobi = "https://api.huobi.pro/market/depth?symbol=%s&type=step1"
    url_kucoin = "https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=%s"#adjust levels here
    url_normal_kucoin = "https://api.kucoin.com/api/v1/market/allTickers"
    url_okex_book = "https://okex.com/api/spot/v3/instruments/%s/book?size=5&depth=0"
    url_ftx = "https://ftx.com/api/markets"
    url_ftx_book = "https://ftx.com/api/markets/%s/orderbook"
    url_bitfinex = "https://api-pub.bitfinex.com/v2/tickers?symbols=%s"
    url_okex = "https://okex.com/api/spot/v3/instruments/ticker"


    for key in a:
        for info in key:
            if 'Binance' in info[1]:
                symbol = info[0]
                if 'Sell Binance' in info[1]:
                    bid_quantity = requests.get(url_binance%(symbol)).json()['bidQty']
                    binance_bid_quantity = 'Bid_Qty: ' + str(bid_quantity)
                    key[info] = key[info] + ", " + binance_bid_quantity


                else:
                    ask_quantity = requests.get(url_binance%(symbol)).json()['askQty']
                    binance_asked_quantity = 'Ask_Qty: ' + str(ask_quantity)
                    key[info] = key[info] + ", " + binance_asked_quantity

            if 'huobi' in info[1]:
                #we need to get bid price from binance
                symbol = info[0].lower()
                if 'Sell huobi' in info[1]:
                    #print(symbol)
                    #print (requests.get(url_huobi%(symbol)).json())
                    bid_quantity = requests.get(url_huobi%(symbol)).json()['tick']['bids']
                    huobi_bid_size = bid_quantity[0][1]
                    huobi_bid_quantity = 'Bid_Qty: ' + str(huobi_bid_size)
                    key[info] = key[info] + ", " + huobi_bid_quantity


                else:
                    ask_quantity = requests.get(url_huobi%(symbol)).json()['tick']['asks']
                    huobi_ask_size = ask_quantity[0][1]
                    huobi_ask_quantity = 'Ask_Qty: ' + str(huobi_ask_size)
                    key[info] = key[info] + ", " + huobi_ask_quantity

            if 'bitfinex' in info[1]:
                            #we need to get bid price from binance
                    symbol = "t"+info[0]
                    if 'Sell bitfinex' in info[1]:
                        bitfinex_bid_size = requests.get(url_bitfinex%(symbol)).json()[0][2]
                        bitfinex_bid_quantity = 'Bid_Qty:' + str(bitfinex_bid_size)
                        key[info] = key[info] + ", " + bitfinex_bid_quantity
                    else:
                        bitfinex_ask_size = requests.get(url_bitfinex%(symbol)).json()[0][4]
                        bitfinex_ask_quantity = 'Ask_Qty:' + str(bitfinex_ask_size)
                        key[info] = key[info] + ", " + bitfinex_ask_quantity

            if 'Kucoin' in info[1]:
                    symbol = info[0]
                    kucoin_base = requests.get(url_normal_kucoin).json()
                    kucoin_list = kucoin_base['data']['ticker']

                    for long_symbol in kucoin_list:
                            required_symbol_to_check = long_symbol['symbol']
                            updated_symbol = long_symbol['symbol'].replace('-','')
                            if updated_symbol in symbol and "Sell Kucoin" in info[1]:
                                    kucoin_api = requests.get(url_kucoin%(required_symbol_to_check)).json()
                                    bid_kucoin = kucoin_api['data']['bids']
                                    if len(bid_kucoin) != 0:
                                        kucoin_bid_size = bid_kucoin[0][1]
                                        kucoin_bid_quantity = 'Bid_Qty:' + str(kucoin_bid_size)
                                        key[info] = key[info] + ", " + kucoin_bid_quantity


                            elif updated_symbol in symbol and "Buy Kucoin" in info[1]:
                                    kucoin_api = requests.get(url_kucoin%(required_symbol_to_check)).json()
                                    ask_kucoin = kucoin_api['data']['asks']
                                    if len(ask_kucoin) != 0:
                                        kucoin_ask_size = ask_kucoin[0][1]
                                        kucoin_ask_quantity = 'Ask_Qty:' + str(kucoin_ask_size)
                                        key[info] = key[info] + ", " + kucoin_ask_quantity


            if 'OKex' in info[1]:
                okex_list = requests.get(url_okex).json()

                symbol = info[0]
                for okex_indi in okex_list:
                    required_symbol_to_check = okex_indi['instrument_id']

                    updated_symbol = required_symbol_to_check.replace("-","")

                    if updated_symbol == symbol and "Sell OKex" in info[1]:
                        okex_api = requests.get(url_okex_book%(required_symbol_to_check)).json()
                        bid_okex = okex_api['bids']
                        okex_bid_size = bid_okex[0][1]
                        okex_bid_quantity = 'Bid_Qty:' + str(okex_bid_size)
                        key[info] = key[info] + ", " + okex_bid_quantity
                    elif updated_symbol == symbol and "Buy OKex" in info[1]:
                        okex_api = requests.get(url_okex_book%(required_symbol_to_check)).json()
                        ask_okex = okex_api['asks']
                        okex_ask_size = ask_okex[0][1]
                        okex_ask_quantity = 'Ask_Qty:' + str(okex_ask_size)
                        key[info] = key[info] + ", " + okex_ask_quantity

            if 'ftx' in info[1]:
                ftx_price = requests.get(url_ftx).json()
                ftx_list = ftx_price['result']
                symbol = info[0]

                for long_symbol in ftx_list:
                    required_symbol_to_check = long_symbol['name']
                    updated_symbol = required_symbol_to_check.replace("/","")
                    if updated_symbol == symbol and "Sell ftx" in info[1]:
                        ftx_api = requests.get(url_ftx_book%(required_symbol_to_check)).json()
                        bid_ftx = ftx_api['result']['bids']
                        ftx_bid_size = bid_ftx[0][1]
                        ftx_bid_quantity = 'Bid_Qty:' + str(ftx_bid_size)
                        key[info] = key[info] + ", " + ftx_bid_quantity
                    elif updated_symbol == symbol and "Buy ftx" in info[1]:
                        ftx_api = requests.get(url_ftx_book%(required_symbol_to_check)).json()
                        ask_ftx = ftx_api['result']['asks']
                        ftx_ask_size = ask_ftx[0][1]
                        ftx_ask_quantity = 'Ask_Qty:' + str(ftx_ask_size)
                        key[info] = key[info] + ", " + ftx_ask_quantity
    #print(a)
    return a



def final_list(answer):
    final_arbi_list = []
    for each_ex in answer:
        #print (each_ex)
        for each in each_ex:
            diction = {}
            arbi_info = each_ex[each]
            if "Bid_Qty" in each_ex[(each)] and "Ask_Qty" in each_ex[(each)]:
                diction[each] = arbi_info
                final_arbi_list.append(diction)

    return final_arbi_list



#final_list(market_depth(execution(list)))
