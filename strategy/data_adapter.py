import pandas as pd
from pandas import DataFrame


def get_30m_data(df: DataFrame) -> DataFrame:
    data = []
    for i in range(1, len(df) - 1):
        first = df.iloc[i]
        second = df.iloc[i + 1]

        open_candle = first["open"]
        close_candle = second["close"]
        high_candle = max(first["high"], second["high"])
        low_candle = min(first["low"], second["low"])
        volume_candle = first["volume"] + second["volume"]
        data.append([open_candle, high_candle, low_candle, close_candle, volume_candle])

    return pd.DataFrame(data, columns=["open", "high", "low", "close", "volume"])


def get_1h_data(df: DataFrame) -> DataFrame:
    data = []
    for i in range(0, len(df) - 3):
        first = df.iloc[i]
        second = df.iloc[i + 1]
        third = df.iloc[i + 2]
        fourth = df.iloc[i + 3]

        open_candle = first["open"]
        close_candle = fourth["close"]
        high_candle = max(first["high"], second["high"], third["high"], fourth["high"])
        low_candle = min(first["low"], second["low"], third["low"], fourth["low"])
        volume_candle = first["volume"] + second["volume"] + third["volume"] + fourth["volume"]
        data.append([open_candle, high_candle, low_candle, close_candle, volume_candle])

    return pd.DataFrame(data, columns=["open", "high", "low", "close", "volume"])
