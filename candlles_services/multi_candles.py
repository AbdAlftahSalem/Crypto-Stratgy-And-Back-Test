import ccxt
import pandas as pd
from binance.client import Client

import const_app
from analysis.applay_indicator_to_csv import apply_indicators


def get_ticker_data(ticker, interval):
    """
    Retrieve historical data for a specific ticker and interval from Binance API.

    Args:
        ticker: The ticker symbol.
        interval: The time interval for the data.

    Returns:
        A Data interval containing the retrieved data.

    """
    client = Client()
    kLine = client.get_historical_klines(ticker, interval, "4 OCT, 2023")
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
    print(f"✅ Finish get data for ticker : {ticker} ||| Interval : {interval}")

    return df
    # df.to_csv(f"{const_app.saveDataFolder}{ticker}-{interval}.csv")


def get_data_for_all_tickers():
    """
    Retrieve historical data for all tickers and intervals specified in const_app.

    """
    print(
        f"\n\n🔃 Start get data for\nTickers: {const_app.settings['tickers']}\nIntervals: {const_app.settings['intervals']}\n\n")
    for ticker in const_app.settings['tickers']:

        for interval in const_app.settings['intervals']:
            get_ticker_data(ticker, interval)


def get_from_binance(ticker, interval='5m', limit=1000):
    try:

        exchange = ccxt.binanceusdm()
        exchange.enableRateLimit = True
        bars = exchange.fetch_ohlcv(ticker, timeframe=interval, limit=limit)
        df = pd.DataFrame(
            bars, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
        df['date'] = pd.to_datetime(df["date"], unit='ms')
        # df.to_csv(f"{ticker}-{interval}.csv")
        # df_5m, df_15m, df_30m = apply_indicators(df)
        print(df)
        df_15m = apply_indicators(df)

        return df_15m
        # return df_5m, df_15m, df_30m

    except:
        pass
