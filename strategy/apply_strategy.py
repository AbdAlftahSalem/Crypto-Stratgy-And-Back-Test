import datetime

import back_test.const_app as const
import data_adapter
import get_data
import indecators
from indecators import vwap_score, nadaraya_watson_envelope


def apply_strategy():
    # if datetime.datetime.now().minute in const.time_start_15m:
    # start search in 15m interval
    for ticker in const.tickers_search:
        # Get data from with indicator for [ 15m, 1h, 30m ] intervals
        df, df30, df1h, nwe_upper, nwe_lower, nwe1h, nwe30, vwap15m, vwap30, vwap1h = get_data_frame_with_indicator(
            ticker, "15m", 800, 48)

        # apply filter strategy
        filter_strategy(df, nwe_upper, nwe_lower, ticker, vwap15m, vwap1h, vwap30)


def filter_strategy(df, nwe_upper, nwe_lower, ticker, vwap15m, vwap1h, vwap30):
    # search in last row of df of close, is upper than or equal to the upper line from nwe indicator and close is upper than vwap15m
    if df["close"].iloc[-1] >= nwe_upper.iloc[-1] and df["close"].iloc[-1] >= vwap15m.iloc[-1]:
        print(
            f"Sell {ticker} signal in 15m interval, price: {df['close'].iloc[-1]}, vwap: {vwap15m.iloc[-1]}, nwe: {nwe_upper['upper'].iloc[-1]}")
    if df["close"].iloc[-1] <= nwe_lower.iloc[-1] and df["close"].iloc[-1] <= vwap15m.iloc[-1]:
        print(
            f"Buy {ticker} signal in 15m interval, price: {df['close'].iloc[-1]}, vwap: {vwap15m.iloc[-1]}, nwe: {nwe_upper['lower'].iloc[-1]}")

    # search in last row of df of close, is upper than or equal to the upper line from nwe indicator and close is upper than vwap1h
    if datetime.datetime.now().minute == 59:
        if df["close"].iloc[-1] >= nwe_upper.iloc[-1] and df["close"].iloc[-1] >= vwap1h[-1]:
            print(
                f"Sell {ticker} signal in 1h interval, price: {df['close'].iloc[-1]}, vwap: {vwap1h[-1]}, nwe: {nwe_upper['upper'].iloc[-1]}")
        if df["close"].iloc[-1] <= nwe_lower.iloc[-1] and df["close"].iloc[-1] <= vwap1h[-1]:
            print(
                f"Buy {ticker} signal in 1h interval, price: {df['close'].iloc[-1]}, vwap: {vwap1h[-1]}, nwe: {nwe_upper['lower'].iloc[-1]}")

    # search in last row of df of close, is upper than or equal to the upper line from nwe indicator and close is upper than vwap30
    if datetime.datetime.now().minute == 59 or datetime.datetime.now().minute == 29:
        if df["close"].iloc[-1] >= nwe_upper.iloc[-1] and df["close"].iloc[-1] >= vwap30[-1]:
            print(
                f"Sell {ticker} signal in 30m interval, price: {df['close'].iloc[-1]}, vwap: {vwap30[-1]}, nwe: {nwe_upper['upper'].iloc[-1]}")
        if df["close"].iloc[-1] <= nwe_lower.iloc[-1] and df["close"].iloc[-1] <= vwap30[-1]:
            print(
                f"Buy {ticker} signal in 30m interval, price: {df['close'].iloc[-1]}, vwap: {vwap30[-1]}, nwe: {nwe_upper['lower'].iloc[-1]}")


def get_data_frame_with_indicator(ticker: str, frame: str, limit: int, vwap_value):
    df = get_data.getFromBinance(ticker, frame, limit)
    vwap15m = vwap_score.vwap_score(df, vwap_value)
    nwe = nadaraya_watson_envelope.nadaraya_watson_envelope(200, 8., 3., df["close"])

    nwe_upper = nwe[0]
    nwe_lower = nwe[1]
    # get data from binance 30m interval
    df30 = data_adapter.get_30m_data(df)
    vwap30 = vwap_score.vwap_score(df30, vwap_value)
    nwe30 = nadaraya_watson_envelope.nadaraya_watson_envelope(200, 8., 3., df30["close"])

    # get data from binance 1h interval
    df1h = data_adapter.get_1h_data(df)
    vwap1h = indecators.vwap_score.vwap_score(df1h, vwap_value)
    nwe1h = indecators.nadaraya_watson_envelope.nadaraya_watson_envelope(200, 8., 3., df1h["close"])
    return df, df1h, df30, nwe_upper, nwe_lower, nwe1h, nwe30, vwap15m, vwap30, vwap1h
