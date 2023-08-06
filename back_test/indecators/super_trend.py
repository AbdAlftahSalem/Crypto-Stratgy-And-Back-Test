import pandas_ta as ta
from pandas import DataFrame


def calculateSuperTrend(df: DataFrame, period) -> DataFrame:
    superTrendValues = ta.supertrend(df['high'], df['low'], df['close'], period=period)
    df['superTrend'] = superTrendValues['SUPERT_3_7.0']
    df['superTrendDirection'] = superTrendValues['SUPERTd_3_7.0']
    return df
