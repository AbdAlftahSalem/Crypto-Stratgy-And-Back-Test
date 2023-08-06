import pandas_ta as ta
from pandas import DataFrame


def RSI(df: DataFrame, length) -> DataFrame:
    df['rsi'] = ta.rsi(df['close'], length=length)
    return df
