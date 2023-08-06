from pandas import DataFrame


def calculate_mfi(df: DataFrame, period) -> DataFrame:
    df['typical_price'] = (df['high'] + df['low'] + df['close']) / 3
    df['money_flow'] = df['typical_price'] * df['volume']

    for i in range(1, len(df)):
        if df['typical_price'][i] > df['typical_price'][i - 1]:
            df['positive_flow'][i] = df['money_flow'][i]
        elif df['typical_price'][i] < df['typical_price'][i - 1]:
            df['negative_flow'][i] = df['money_flow'][i]

    # Calculate the money flow ratio (MFR)
    df['positive_mfr'] = df['positive_flow'].rolling(window=period).sum() / df['negative_flow'].rolling(
        window=period).sum()

    # Calculate the Money Flow Index (MFI)
    df['mfi'] = 100 - (100 / (1 + df['positive_mfr']))

    return df
