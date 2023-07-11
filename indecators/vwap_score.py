def vwap_score(df, period):
    df['volume'] = df['volume'].astype(float)  # Convert 'volume' column to float
    df['close'] = df['close'].astype(float)  # Convert 'close' column to float

    df['vc'] = df['volume'] * df['close']

    return round((df['vc'].rolling(window=period).sum()) / (df['volume'].rolling(window=period).sum()),
                 10).fillna(method='bfill')
