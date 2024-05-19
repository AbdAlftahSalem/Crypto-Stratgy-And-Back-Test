from pandas import DataFrame
import pandas_ta as ta


def calculate_mfi(df: DataFrame, period) -> DataFrame:
    df['mfi'] = ta.mfi(df['high'], df['low'], df['close'], df['volume'], length=period)
    return df
