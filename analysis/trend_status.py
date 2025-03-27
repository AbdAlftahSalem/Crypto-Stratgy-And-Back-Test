import pandas as pd


def trend_status(df: pd.DataFrame, back_candle: int = 8) -> pd.DataFrame:
    trend_status_list = [0] * len(df)

    df['ema30'] = df['close'].ewm(span=30, adjust=False).mean()
    df['ema50'] = df['close'].ewm(span=50, adjust=False).mean()

    for i in range(back_candle, len(df)):

        # get nwe df with back_candle length
        new_df = df.iloc[i: i + back_candle]

        min_low = min(new_df['low'])
        max_high = max(new_df['high'])

        min_ema30 = min(new_df['ema30'])

        ema_trend_up_condition = new_df.iloc[-1]['ema30'] > new_df.iloc[-1]['ema50']
        ema_trend_down_condition = new_df.iloc[-1]['ema30'] < new_df.iloc[-1]['ema50']

        candle_trend_up_condition = min_low > min_ema30 and ema_trend_up_condition
        candle_trend_down_condition = max_high < min_ema30 and ema_trend_down_condition

        if candle_trend_up_condition:
            trend_status_list.append(1)

        elif candle_trend_down_condition:
            trend_status_list.append(-1)

        else:
            trend_status_list.append(0)
    df['trend_status'] = trend_status_list
    print("IN TREND")
    print(df)
    return df
