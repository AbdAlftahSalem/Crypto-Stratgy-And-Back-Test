import numpy as np
import pandas_ta as ta
from pandas import DataFrame


def calc_buying_climax_and_selling_climax(df: DataFrame):
    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    df['rsi'] = ta.rsi(df['close'], length=14)
    mp = 2
    ratio = 50
    cand = 100
    range_1 = ta.atr(df['high'], df['low'], df['close'], length=cand)
    candr = abs(df['high'] - df['low'])

    bodyr = abs(df['open'] - df['close'])

    prev = abs(df['high'].shift(1) - df['low'].shift(1))
    nextabs = abs(df['high'] - df['low'])

    explose = (bodyr / candr >= ratio / 100) & (candr >= range_1 * mp) & (df['volume'] > 2 * df['volume'].shift(3)) & (
            nextabs > 2 * prev)
    df['Explosive Move'] = np.where(explose, 'black', np.nan)

    df['Upper Line'] = np.where(df['Explosive Move'] == 'black', df['high'], np.nan)
    df['Lower Line'] = np.where(df['Explosive Move'] == 'black', df['low'], np.nan)

    return df
