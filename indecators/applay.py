import pandas as pd

import const_app
from indecators import nadaraya_watson_envelope as nadaraya, vwap_score as vwap
from util import divideDf


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

    data = divideDf(df)

    fullDF = []
    for i in data:
        if len(i) > 499:
            close = i["close"]

            # Calculate the Nadaraya-Watson envelope
            envelope = nadaraya.nadaraya_watson_envelope(500, 8., 3., close)

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

    # Save the combined DataFrame with indicators to a CSV file
    combined_df.to_csv(f"{const_app.saveDataFolder}{ticker}-{interval}-indicator.csv")
    print(f'* Finish getting data for {ticker} in {interval} and save in the {const_app.saveDataFolder} folder')
