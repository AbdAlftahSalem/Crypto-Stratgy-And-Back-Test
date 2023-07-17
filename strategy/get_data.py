import ccxt
import pandas as pd
from pandas import DataFrame


def getFromBinance(ticker: str, interval: str, limit) -> DataFrame:
    try:
        ticker = ticker.strip()
        interval = interval.strip()
        exchange = ccxt.binance()
        bars = exchange.fetch_ohlcv(ticker, timeframe=interval, limit=limit)
        df = pd.DataFrame(
            bars, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
        df['date'] = pd.to_datetime(df["date"], unit='ms')

        return df

    except:
        pass
