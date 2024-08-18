import pandas as pd

import const_app
from analysis import vwap_score as vwap
from analysis.nadaraya_watson_envelope import apply_waston_envelope
from analysis.trend_status import trend_status
from utils.convert_df import convert_df
from utils.send_to_tele import send_message_to_telegram


def apply_indicators(df: pd.DataFrame):
    """
    Apply indicators to the Data interval.

    Args:
        df: The Data interval to apply the indicators to.

    """

    # Convert df
    df5m, df15m, df30m = convert_df(df)

    df_5m = apply_in_one_df(df5m)
    df_15m = apply_in_one_df(df15m)
    df_30m = apply_in_one_df(df30m)

    return df_5m, df_15m, df_30m


def apply_in_one_df(df):
    # calculate vwap
    df["vwap21"] = vwap.vwap_score(df, 21)
    df["vwap50"] = vwap.vwap_score(df, 50)
    df["vwap100"] = vwap.vwap_score(df, 100)
    df["vwap200"] = vwap.vwap_score(df, 200)

    # calculate EMA for each specified period
    for ema_period in const_app.settings["ema"]:
        if ema_period == "None":
            continue
        span = int(ema_period[3:])
        df[f'{ema_period.lower()}'] = df['close'].ewm(span=span, adjust=False).mean()

    # df = calculate_mfi(df, 14)
    # df = calculate_rsi(df, 14)
    # df = calculate_super_trend(df, 10, 3)
    df = apply_waston_envelope(df)
    # df = spongebob_indicator(df)

    # df = bollinger_band(df)
    df = trend_status(df, 12)
    return df


def add_all_indicator_to_csv():
    for ticker in const_app.settings['tickers']:
        for interval in const_app.settings['intervals']:
            df = pd.read_csv(f"{const_app.settings['saveDataFolder']}{ticker}-{interval}.csv")

            df_5m, df_15m, df_30m = apply_indicators(df)
            df_5m.to_csv(f"{const_app.settings['saveDataFolderIndicator']}{ticker}-{interval}-indicators.csv")
            df_15m.to_csv(f"{const_app.settings['saveDataFolderIndicator']}{ticker}-{interval}-indicators.csv")
            df_30m.to_csv(f"{const_app.settings['saveDataFolderIndicator']}{ticker}-{interval}-indicators.csv")

            print(f"Add all indicator to {ticker}-{interval}.csv")
            send_message_to_telegram(f"Add all indicator to {ticker}-{interval}-indicators.csv\n\nLength : {len(df)}")
