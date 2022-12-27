#seleect asset (btc)
asset = 'BTC/USDT'

#  select data of the asset
data = collect_historical_data(asset)

# preprocess the data
data = preprocess_data(data)


def preprocess_data(data):
    # handle missing values
    data = data.dropna()
    
    # scale the data
    scaler = MinMaxScaler()
    data[['open', 'high', 'low', 'close']] = scaler.fit_transform(data[['open', 'high', 'low', 'close']])
    
    return data

