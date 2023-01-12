import ccxt

#  Binance exchange
exchange = ccxt.binance()

# API keys
exchange.apiKey = '********'
exchange.secret = '********'

# capital__
balance = exchange.fetch_balance()
print(balance)

# market coins
market = 'BTC/USDT'
market = 'LUNC/BUSD'
market = 'ETH/USDT'
market = 'ADA/USDT'
market = 'MATIC/USDT'

#BTC 
amount = 0.01

limit_price = 0.1 * purchase_price

#/
#for testing mode  1
prediction = model.predict(X_test)[0]

# prediction is to buy or sell
if prediction > 0:
    # create a buy order
    order = exchange.create_order(market, 'market', 'buy', amount)
else:
    # create a sell order
    order = exchange.create_order(market, 'market', 'sell', amount)
#//

#  buy order
order = exchange.create_order(market, 'limit', 'buy', amount, purchase_price)


status = order['status']

while status == 'open':
    #order status 
    order = exchange.fetch_order(order['id'])
    status = order['status']

#  sell order ec
sell_order = exchange.create_order(market, 'limit', 'sell', amount, limit_price)

# sell order
status = sell_order['status']

while status == 'open':
   
    sell_order = exchange.fetch_order(sell_order['id'])
    status = sell_order['status']

print("Trade complete!")
