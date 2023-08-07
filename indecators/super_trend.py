import pandas_ta as ta
from pandas import DataFrame



def calculate_super_trend(df: DataFrame, period , multiplier) -> DataFrame:
    superTrendValues = ta.supertrend(df['high'], df['low'], df['close'], period=period, multiplier=multiplier)
    print(superTrendValues)
    df['superTrend'] = superTrendValues['SUPERT_7_3.0']
    df['superTrendDirection'] = superTrendValues['SUPERTl_7_3.0']
    return df

