import pandas_ta as ta
from pandas import DataFrame


def calculate_rsi(df: DataFrame, length) -> DataFrame:
    df['rsi'] = ta.rsi(df['close'], length=length)
    return df
