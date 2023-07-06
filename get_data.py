import pandas as pd
from binance.client import Client

import const_app

client = Client()


def getData(ticker, interval):
    kLine = client.get_historical_klines(ticker, interval, "1 Jan, 2022")
    df = pd.DataFrame(
        kLine,
        columns=['date', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades', 'taker_base_vol',
                 'taker_quote_vol', 'ignore'])
    df['date'] = pd.to_datetime(df["date"], unit='ms')
    del df["taker_quote_vol"]
    del df["close_time"]
    del df["qav"]
    del df["num_trades"]
    del df["taker_base_vol"]
    del df["ignore"]
    # Calculate EMA10

    df['ema10'] = df['close'].ewm(span=10, adjust=False).mean()

    # Calculate EMA20
    df['ema20'] = df['close'].ewm(span=20, adjust=False).mean()

    # Calculate EMA50
    df['ema50'] = df['close'].ewm(span=50, adjust=False).mean()
    # Calculate EMA100
    df['ema100'] = df['close'].ewm(span=100, adjust=False).mean()
    # Calculate EMA200
    df['ema200'] = df['close'].ewm(span=200, adjust=False).mean()
    df.to_csv(f'{ticker}-{interval}-2022.csv')
    df.to_csv(f'{ticker}-{interval}-2022.csv')

    return df


def getDataForAllTickers():
    print(f'Start get data for\nTickers : {const_app.tickers}\nIntervals : {const_app.intervals}')
    for ticker in const_app.tickers:
        for interval in const_app.intervals:
            getData(ticker, interval)
            print(f'Finish get data for {ticker} in {interval} and save in : {const_app.saveDataFolder} folder')
