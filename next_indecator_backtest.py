import pandas as pd

from indecator import nadaraya_watson_envelope
from util import divideDf

tickers = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "MATICUSDT", "SOLUSDT", "DOTUSDT", "AVAXUSDT",
           "LINKUSDT"]
for k in ["15m", "30m", "1h"]:
    for ticker in tickers:
        # read df
        df = pd.read_csv(f'./{ticker}-{k}-2022.csv')
        data = divideDf(df)

        fullDF = []
        for i in data:
            if len(i) > 499:
                close = i["close"]

                envelope = nadaraya_watson_envelope(500, 8., 3., close)

                # upper and lower are pandas Series
                upper = envelope[0]
                lower = envelope[1]
                # cross_up and cross_dn are float numbers
                cross_up = envelope[2]
                cross_dn = envelope[3]

                i["upper"] = upper
                i["lower"] = lower
                i['signal'] = ''
                i.loc[i['close'] > i['upper'], 'signal'] = 'sell'
                i.loc[i['close'] < i['lower'], 'signal'] = 'buy'
                fullDF.append(i)

            else:
                print(f"PASS {i.iloc[0]['date']} , to {i.iloc[-1]['date']}")
                pass

        combined_df = pd.concat(fullDF, ignore_index=True)
        combined_df = (combined_df.reset_index())

        combined_df['EMA200'] = combined_df['close'].ewm(span=200, adjust=False).mean()
        combined_df['EMA100'] = combined_df['close'].ewm(span=100, adjust=False).mean()
        combined_df['EMA50'] = combined_df['close'].ewm(span=50, adjust=False).mean()
        combined_df['EMA20'] = combined_df['close'].ewm(span=20, adjust=False).mean()
        combined_df['EMA10'] = combined_df['close'].ewm(span=10, adjust=False).mean()
        combined_df.to_csv(f"{ticker}-{k}-indicator.csv")
