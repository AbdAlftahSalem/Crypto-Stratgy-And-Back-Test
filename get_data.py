import pandas as pd
from binance.client import Client

import const_app
from utils.send_to_tele import sentToTelegram


def getData(ticker, interval):
    """
    Retrieve historical data for a specific ticker and interval from Binance API.

    Args:
        ticker: The ticker symbol.
        interval: The time interval for the data.

    Returns:
        A DataFrame containing the retrieved data.

    """
    client = Client()
    kLine = client.get_historical_klines(ticker, interval)
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

    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["open"] = df["open"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df
    # df.to_csv(f"{const_app.saveDataFolder}{ticker}-{interval}.csv")

    # print(f'* Finish getting data for {ticker} in {interval} and save in the {const_app.saveDataFolder} folder')
    # sentToTelegram(f"FINISH {ticker} {interval}")


def getDataForAllTickers():
    """
    Retrieve historical data for all tickers and intervals specified in const_app.

    """
    print(f'Start get data for\nTickers: {const_app.tickers}\nIntervals: {const_app.intervals}\n\n')
    for ticker in const_app.tickers:
        for interval in const_app.intervals:
            getData(ticker, interval)
