import numpy as np
import ta as ta2
from pandas import DataFrame


def buying_climax_and_selling_climax(df: DataFrame):
    df['rsi'] = ta2.momentum.rsi(df.close, window=14)
    mp = 2
    ratio = 50
    cand = 100
    range_1 = ta2.volatility.AverageTrueRange(high=df['high'], low=df['low'], close=df['close'],
                                              window=cand).average_true_range()
    candr = abs(df['high'] - df['low'])

    bodyr = abs(df['open'] - df['close'])

    prev = abs(df['high'].shift(1) - df['low'].shift(1))
    nextabs = abs(df['high'] - df['low'])
    explose = (bodyr / candr >= ratio / 100) & (candr >= range_1 * mp) & (df['volume'] > 2 * df['volume'].shift(3)) & (
            nextabs > 2 * prev)
    df['Explosive Move'] = np.where(explose, 'black', np.nan)

    for i in range(len(df)):
        if df.iloc[i]["Explosive Move"] == "black":
            print(df.iloc[i])
            print()
            print()
            print()
