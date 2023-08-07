import pandas as pd

import const_app
from indecators import vwap_score as vwap
from indecators.cci import calculate_cci
from indecators.mfi import calculate_mfi
from indecators.nadaraya_watson_envelope import apply_waston_envelope
from indecators.rsi import calculate_rsi
from indecators.super_trend import calculate_super_trend


def applyIndicators(df: pd.DataFrame, ticker: str, interval: str):
    """
    Apply indicators to the DataFrame.

    Args:
        df: The DataFrame to apply the indicators to.
        ticker: The ticker symbol.
        interval: The time interval for the data.

    """
    # calculate vwap
    df["vwap21"] = vwap.vwap_score(df, 21)
    df["vwap50"] = vwap.vwap_score(df, 50)
    df["vwap100"] = vwap.vwap_score(df, 100)
    df["vwap200"] = vwap.vwap_score(df, 200)
    print("Finish calculate vwap")

    # calculate cci
    df = calculate_cci(df, 20)
    print("Finish calculate cci")

    # calculate EMA for each specified period
    for ema_period in const_app.ema:
        if ema_period == "None":
            continue
        span = int(ema_period[3:])
        df[f'{ema_period.lower()}'] = df['close'].ewm(span=span, adjust=False).mean()
    print("Finish calculate EMA")

    # calculate mfi
    df = calculate_mfi(df, 14)
    print("Finish calculate mfi")

    # calculate rsi
    df = calculate_rsi(df, 14)
    print("Finish calculate rsi")

    # calculate super trend
    df = calculate_super_trend(df, 10, 3)
    print("Finish calculate super trend")

    # calculate waston_envelopewaston_envelope
    df = apply_waston_envelope(df)
    print("Finish calculate waston_envelope \n\n\n")

    return df
