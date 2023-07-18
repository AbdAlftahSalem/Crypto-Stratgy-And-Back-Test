import datetime

import get_data
import data_adapter
import indecators
import back_test.const_app as const


def apply_strategy():
    if datetime.datetime.now().minute in const.time_start_15m:
        # start search in 15m interval
        for ticker in const.tickers_search:
            # Get data from with indicator for [ 15m, 1h, 30m ] intervals
            df, df1h, df30, nwe, nwe1h, nwe30, vwap, vwap1h, vwap30 = get_data_frame_with_indicator(ticker, "15m", 800,
                                                                                                    48)
            # search in last row of df of close , is upper than or equal upper line from nwe indicator , its mean buy
            if df.iloc[-1]["close"] >= nwe.iloc[-1]["upper"]:
                print("BUY NWE 15m")

            # search in last row of df of close , is lower than or equal lower line from nwe indicator , its mean sell
            if df.iloc[-1]["close"] <= nwe.iloc[-1]["lower"]:
                print("SELL NWE 15m")


def get_data_frame_with_indicator(ticker: str, frame: str, limit: int, vwap_value):
    df = get_data.getFromBinance(ticker, frame, limit)
    vwap = indecators.vwap_score.vwap_score(df, vwap_value)
    nwe = indecators.nadaraya_watson_envelope.nadaraya_watson_envelope(500, 8., 3., df["close"])
    # get data from binance 30m interval
    df30 = data_adapter.get_30m_data(df)
    vwap30 = indecators.vwap_score.vwap_score(df30, vwap_value)
    nwe30 = indecators.nadaraya_watson_envelope.nadaraya_watson_envelope(500, 8., 3., df30["close"])
    # get data from binance 1h interval
    df1h = data_adapter.get_1h_data(df)
    vwap1h = indecators.vwap_score.vwap_score(df1h, vwap_value)
    nwe1h = indecators.nadaraya_watson_envelope.nadaraya_watson_envelope(500, 8., 3., df1h["close"])
    return df, df1h, df30, nwe, nwe1h, nwe30, vwap, vwap1h, vwap30
