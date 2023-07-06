import pandas as pd

import const_app
from indecator import nadaraya_watson_envelope
from util import divideDf


def applyIndicator(df: pd.DataFrame):
    """
    Apply indicators to the DataFrame.

    Args:
        df: The DataFrame to apply the indicators to.

    """
    for k in const_app.intervals:
        for ticker in const_app.tickers:
            # read df
            data = divideDf(df)

            fullDF = []
            for i in data:
                if len(i) > 499:
                    close = i["close"]

                    # Calculate the Nadaraya-Watson envelope
                    envelope = nadaraya_watson_envelope(500, 8., 3., close)

                    # Extract upper and lower bands from the envelope
                    upper = envelope[0]
                    lower = envelope[1]

                    # Calculate signals based on the close prices and bands
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
            combined_df = combined_df.reset_index()

            # Save the combined DataFrame with indicators to a CSV file
            combined_df.to_csv(f"{const_app.saveDataFolder}{ticker}-{k}-indicator.csv")
