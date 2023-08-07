import pandas as pd
from binance.client import Client

import const_app
from send_to_tele import sentToTelegram


def getData(ticker, interval):
    """
    Retrieve historical data for a specific ticker and interval from Binance API.

    Args:
        ticker: The ticker symbol.
        interval: The time interval for the data.

    Returns:
        A DataFrame containing the retrieved data.

    """
    client = Client()
    kLine = client.get_historical_klines(ticker, interval, "1 jan, 2021")
    df = pd.DataFrame(
        kLine,
        columns=['date', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades', 'taker_base_vol',
                 'taker_quote_vol', 'ignore'])
    df['date'] = pd.to_datetime(df["date"], unit='ms')
    del df["taker_quote_vol"]
    del df["close_time"]
    del df["qav"]
    del df["num_trades"]
    del df["taker_base_vol"]
    del df["ignore"]

    df.to_csv(f"D:\\Python project\\nadaraya_watson_envelope\\data\\{ticker}-{interval}.csv")

    # # Calculate EMA for each specified period
    # for ema_period in const_app.ema:
    #     if ema_period == "None":
    #         continue
    #     span = int(ema_period[3:])
    #     df[f'{ema_period.lower()}'] = df['close'].ewm(span=span, adjust=False).mean()
    #
    # # Apply indicators to the DataFrame
    # # applay.applyIndicators(df, ticker, interval)
    # print(f'* Finish getting data for {ticker} in {interval} and save in the {const_app.saveDataFolder} folder')
    # sentToTelegram(f"FINISH {ticker} {interval}")


def getDataForAllTickers():
    """
    Retrieve historical data for all tickers and intervals specified in const_app.

    """
    print(f'Start get data for\nTickers: {const_app.tickers}\nIntervals: {const_app.intervals}\n\n')
    for ticker in const_app.tickers:
        for interval in const_app.intervals:
            getData(ticker, interval)
