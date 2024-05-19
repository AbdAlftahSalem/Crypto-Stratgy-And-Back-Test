import pandas


# should be 15m interval
def convert_df(df):
    d = {'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume': 'sum'}
    df['date'] = pandas.to_datetime(df['date'])
    df15m = df.resample('15T', on='date').agg(d)
    df30m = df.resample('30T', on='date').agg(d)

    return df, df15m, df30m
