import time, json, requests,copy

"""standardised all dictionary to symbol, bid and ask"""

"""https://docs.binance.org/api-reference/dex-api/paths.html
https://api.binance.com/api/v3/ticker/bookTicker

Base api = https://api.binance.com
Ticker = https://api.binance.com/api/v3/ticker/bookTicker (with bid and ask price)
https://api.binance.com/api/v3/ticker/price
"""

def binance():

    """Key in the tic
    ker symbols into pairs that we would like to view for lastest prices"""
    binance_list = []
    url = "https://api.binance.com/api/v3/ticker/bookTicker"
    binance_price = requests.get(url).json()
    #Need to remove pairs with no liquidity
    binance_shortlisted = []
    for i in binance_price:
        if float(i['askQty']) != 0 or float(i['bidQty']) != 0:
            i['bid'] = i['bidPrice']
            i['ask'] = i['askPrice']
            binance_shortlisted.append(i)
            i['exchange'] = 'Binance'

    return binance_shortlisted


def kucoin():
    """https://docs.kucoin.com/#get-all-tickers
https://docs.kucoin.com/#reading-guide
The base url is https://api.kucoin.com.
/api/v1/market/orderbook/level1
/api/v1/market/allTickers
OrderBook =
https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=BTC-USDT"""
# we need to change buy to best bid and sell to best ask
    kucoin_list = []
    url = "https://api.kucoin.com/api/v1/market/allTickers"
    kucoin_price = requests.get(url).json()
    k = kucoin_price['data']['ticker']
    #again we need to shortlist and remove the dash
    for i in k:
        if (i['buy']) != '0' and (i['sell']) != '0':
            i['symbol'] = i['symbol'].replace('-','')
            i['bid'] = i['buy']
            i['ask'] =  i['sell']
            i['exchange'] = 'Kucoin'


    #print(len(k))

    return k

def kraken():
    asset_pair = "https://api.kraken.com/0/public/AssetPairs"
    url = "https://api.kraken.com/0/public/Ticker?pair=%s"
    urld = """https://api.kraken.com/0/public/Depth?pair=%s&count=1"""

    kraken_list = []
    asset_pair = requests.get(asset_pair).json()
    kraken = asset_pair["result"]
    for i in kraken:
        kraken_price = requests.get(urld %(i)).json()
        kraken_list.append(kraken_price['result'])


    return kraken_list

"""https://api-pub.bitfinex.com/v2/tickers"""

def bitfinex():
    bit_list = []
    url = "https://api-pub.bitfinex.com/v2/tickers?symbols=ALL"


    bitfnex_price = requests.get(url).json()

    x = ['symbol' ,'bid', 'BID_SIZE','ask','ASK_SIZE','DAILY_CHANGE','DAILY_CHANGE_RELATIVE','LAST_PRICE','VOLUME','HIGH','LOW']
        #remove those with no volume then put it in a dictionary
    for i in bitfnex_price:
        bit_dict = {}
        #print(i)
        if len(i) == 11 and i[5] != 0:
            count = 0
            for each in x:
                bit_dict[each] = i[count]
                count += 1
                #print(bit_dict)
            bit_list.append(bit_dict)
    for pair in bit_list:
        pair['symbol'] = pair['symbol'][1:]
        pair['exchange'] = 'bitfinex'

    return bit_list


"""https://huobiapi.github.io/docs/spot/v1/en/#get-latest-aggregated-ticker
Base api is https://api.huobi.pro
https://api.huobi.pro/market/depth?symbol=btcusdt&type=step1
https://api.huobi.pro/market/tickers
Find ticker symbols at https://api.huobi.pro/v1/common/symbols"""
def huobi():
    huobi_list = []
    huobi_dic = {}
    url = "https://api.huobi.pro/market/tickers"

    huobi_price = requests.get(url).json()
    data = huobi_price['data']
    for name in data:
        if name['ask'] != 0 and name['bid'] != 0:
            name['symbol'] = name['symbol'].upper()
            name['exchange'] = 'huobi'
    for i in data:
            huobi_list.append(i)


    return huobi_list

def ftx():
    """/markets/{market_name}/orderbook?depth={depth}"""

    ftx_list = []
    url = "https://ftx.com/api/markets"
    ftx_price = requests.get(url).json()
    result = ftx_price['result']
    #we eliminate low volume and futures
    for each in result:
        if each['change24h'] != 0 and each['type'] != 'future':
            ftx_list.append(each)
    for i in ftx_list:
        x = ('change1h','change24h','changeBod')
        i['symbol'] = i['name'].replace('/','')
        i['exchange'] = 'ftx'

        for q in x:
            del i[q]

    return ftx_list


def okex():
    """/api/spot/v3/instruments/ticker"""
    "https://okex.com/api/spot/v3/instruments/%s/book?size=5&depth=0"
    url = "https://okex.com/api/spot/v3/instruments/ticker"
    okex_price = requests.get(url).json()
    for i in okex_price:
        i['symbol'] = i['product_id'].replace('-','')
        i['bid'] = i['best_bid']
        i['ask'] = i['best_ask']
        i['exchange'] = 'OKex'

    return okex_price
