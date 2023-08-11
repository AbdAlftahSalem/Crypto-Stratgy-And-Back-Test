import pandas as pd

import const_app
from indecators.applay import applyIndicators
from utils.send_to_tele import sentToTelegram


def add_all_indicator_to_csv():
    for ticker in const_app.tickers:
        for interval in const_app.intervals:
            df = pd.read_csv(f"{const_app.saveDataFolder}{ticker}-{interval}-indicators.csv")
            df = applyIndicators(df, ticker, interval)
            df.to_csv(
                f"D:\\Python project\\backtest\\Crypto-Stratgy-And-Back-Test\\data\\{ticker}-{interval}-indicators.csv")
            print(f"Add all indicator to {ticker}-{interval}.csv")
            sentToTelegram(f"Add all indicator to {ticker}-{interval}-indicators.csv\n\nLength : {len(df)}")
