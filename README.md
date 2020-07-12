# Crypto-Arbitrage-Bot-
A crypto Arbitrage Bot that pulls API from Binance, Bitfinex Kraken, Kucoin, Huobi, Ftx and Okex to compare and evaluate arbitrage opportunities 

api_bot.py

api_bot.py contains all the function that will request bid ask price from all the different exchanges, from Binance, Bitfinex Kraken, Kucoin, Huobi, Ftx and Okex. 

The api for Kraken is a little slow so I would leave it out for the rest of the project.

Arbitrage_bot.py

The arbitrage bot has two functions, compare and execution.

First, let us talk about threshold. Threshold is the minimum % you would like to consider for the purpose of the bot. It is in percentage points and adjust the figure as
you would like to. 

Compare will compare the bid and ask price of every symbol on each exchange and store the result in a dictionary, with the symbol pairing,premium and action needed. 

Execution.py

Execution allows you to customise for which exchange you would like to compare against. The default setting is all 6 exchanges, 
(Binance, Kucoin,Huobi,Ftx,Okex, Bitfinex). User can adjust the number of exchanges by editing the values in list. 

market_depth.py

Market_depth will run through every pairing with arbitrage opportunities and find the corresponding bid and ask quantity on each exchange. 
This allows for user to check on the available lidqudity for arbitrage opportunities.

binance_bot.py

User will have to add in their own public API and private API into the program. 

Binance Bot is a simple trading bot that will market buy and sell based on the result from Market_depth, if the action needed is to buy or sell
any symbol from Binance. 
