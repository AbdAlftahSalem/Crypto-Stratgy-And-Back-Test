import pandas as pd
from pandas import DataFrame


def get_30m_data(df: DataFrame) -> DataFrame:
    return df.resample('.5H', on='date').agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum'
    })


def get_1h_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.resample('1H', on='date').agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum'
    })
