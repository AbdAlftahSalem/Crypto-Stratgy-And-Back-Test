import pandas_ta as ta


def calculate_cci(df, period):
    df['cci'] = ta.cci(df['high'], df['low'], df['close'], length=period)
    return df['cci']
