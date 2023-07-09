import pandas as pd

import const_app
import indecators
from indecators import nadaraya_watson_envelope, vwap_score
from util import divideDf


def applyIndicators(df: pd.DataFrame, ticker: str, interval: str):
    """
    Apply indicators to the DataFrame.

    Args:
        df: The DataFrame to apply the indicators to.
        ticker: The ticker symbol.
        interval: The time interval for the data.

    """

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
            i.loc[i['close'].astype(float) > i['upper'].astype(float), 'signal'] = 'sell'
            i.loc[i['close'].astype(float) < i['lower'].astype(float), 'signal'] = 'buy'

            fullDF.append(i)
        else:
            print(f"PASS {i.iloc[0]['date']} , to {i.iloc[-1]['date']}")
            pass

    combined_df = pd.concat(fullDF, ignore_index=True)
    combined_df = combined_df.reset_index()

    combined_df = vwap_score(combined_df, 21)
    combined_df = vwap_score(combined_df, 48)
    combined_df = vwap_score(combined_df, 96)
    combined_df = vwap_score(combined_df, 192)
    combined_df = vwap_score(combined_df, 384)
    # Save the combined DataFrame with indicators to a CSV file
    combined_df.to_csv(f"{const_app.saveDataFolder}{ticker}-{interval}-indicators.csv")
