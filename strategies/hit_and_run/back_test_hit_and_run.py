from utils.util import getNumByChange
from utils.util_back_test import getProfit, getStopLose


def longBackTest(df, ticker: str, frame: str):
    df["sponge_bob_long"] = df["sponge_bob_long"].fillna(0)

    output = {"ticker": ticker, "interval": frame, "profit_num": 0, "lose_num": 0, "strategy_name": "HAR", "data": []}

    # 1- Add sponge_bob_long condition [ sponge_bob_long != 0 and  sponge_bob_long <= -65 ] & candle is red
    condition = (df['sponge_bob_long'] != 0) & (df['sponge_bob_long'] <= -65) & (df['close'] < df['open'])

    # 2- Create a new column 'enterPrice' when the condition is true
    df.loc[condition, 'enterPrice'] = (getNumByChange(df.loc[condition, 'low'], -3)).fillna(0)

    # 3- Calculate target and stop prices based on the entered price
    df.loc[condition, 'targetPrice'] = (
        getNumByChange(df.loc[condition, 'enterPrice'], getProfit("hit_and_run", frame, True))).fillna(0)
    df.loc[condition, 'stopPrice'] = (
        getNumByChange(df.loc[condition, 'enterPrice'], -getStopLose("hit_and_run", True))).fillna(0)
    # add column strategy to df with true or false values
    df.loc[condition, 'strategy'] = True

    for i in range(len(df)):
        if df.iloc[i]["strategy"] == True:
            enterCandle = df.iloc[i]
            targetPrice = df.iloc[i]["targetPrice"]
            stopPrice = df.iloc[i]["stopPrice"]

            for j in range(i + 1, len(df)):
                # check if current candle low is less than or equal enterPrice and candle is red
                if df.iloc[j]["low"] <= enterCandle["enter_price"]:
                    # loop through candles until targetPrice or stopPrice is reached
                    for k in range(j, len(df)):
                        # check if current candle high is greater than or equal targetPrice
                        if df.iloc[k]["high"] >= targetPrice:
                            data = {
                                "entry_date": enterCandle["date"],
                                "out_date": df.iloc[k]["date"],
                                "enter_price": enterCandle["enter_price"],
                                "tp": targetPrice,
                                "sl": stopPrice,
                                "status": "tp",
                                "change": getProfit("hit_and_run", frame, True),
                            }
                            output["data"].append(data)
                            output["profit_num"] += 1
                            break

                        # check if current candle low is less than or equal stopPrice
                        elif df.iloc[k]["close"] <= stopPrice:
                            data = {
                                "entry_date": enterCandle["date"],
                                "out_date": df.iloc[k]["date"],
                                "enter_price": enterCandle["enter_price"],
                                "tp": targetPrice,
                                "sl": stopPrice,
                                "status": "sl",
                                "change": -getStopLose("hit_and_run", True),
                            }
                            output["data"].append(data)
                            output["lose_num"] += 1
                            break

                    break

    return output


def sellBackTest(combined_df, ticker: str, frame: str):
    """
    Perform a sell backtest on the combined DataFrame.

    Args:
        combined_df: The combined DataFrame containing the data.
        ticker: The ticker symbol.
        frame: The time frame.

    Returns:
        A dictionary containing the backtest data.
    """
    combined_df["sponge_bob_short"] = combined_df["sponge_bob_short"].fillna(0)

    output = {"ticker": ticker, "interval": frame, "profit_num": 0, "lose_num": 0, "strategy_name": "HAR", "data": []}

    # 1- Add sponge_bob_short condition [ sponge_bob_short != 0 and  sponge_bob_short >= 65 ] & candle is green
    condition = (combined_df['sponge_bob_short'] != 0) & (combined_df['sponge_bob_short'] >= 65) & (
            combined_df['close'] > combined_df['open'])

    # 2- Create a new column 'enterPrice' when the condition is true
    combined_df.loc[condition, 'enterPrice'] = (getNumByChange(combined_df.loc[condition, 'high'], 3)).fillna(0)

    # 3- Calculate target and stop prices based on the entered price
    combined_df.loc[condition, 'targetPrice'] = (
        getNumByChange(combined_df.loc[condition, 'enterPrice'], -getProfit("hit_and_run", frame, False))).fillna(0)
    combined_df.loc[condition, 'stopPrice'] = (
        getNumByChange(combined_df.loc[condition, 'enterPrice'], getStopLose("hit_and_run", False))).fillna(0)
    # add column strategy to df with true or false values
    combined_df.loc[condition, 'strategy'] = True

    for i in range(len(combined_df)):
        if combined_df.iloc[i]["strategy"] == True:
            enterCandle = combined_df.iloc[i]
            targetPrice = combined_df.iloc[i]["targetPrice"]
            stopPrice = combined_df.iloc[i]["stopPrice"]

            for j in range(i + 1, len(combined_df)):
                # check if current candle high is greater than or equal enterPrice and candle is green
                if combined_df.iloc[j]["high"] >= enterCandle["enter_price"]:
                    # loop through candles until targetPrice or stopPrice is reached
                    for k in range(j, len(combined_df)):
                        # check if current candle low is less than or equal targetPrice
                        if combined_df.iloc[k]["low"] <= targetPrice:
                            data = {
                                "entry_date": enterCandle["date"],
                                "out_date": combined_df.iloc[k]["date"],
                                "enter_price": enterCandle["enter_price"],
                                "tp": targetPrice,
                                "sl": stopPrice,
                                "status": "tp",
                                "change": -getProfit("hit_and_run", frame, False),
                            }
                            output["data"].append(data)
                            output["profit_num"] += 1
                            break

                        # check if current candle high is greater than or equal stopPrice
                        elif combined_df.iloc[k]["close"] >= stopPrice:
                            data = {
                                "entry_date": enterCandle["date"],
                                "out_date": combined_df.iloc[k]["date"],
                                "enter_price": enterCandle["enter_price"],
                                "tp": targetPrice,
                                "sl": stopPrice,
                                "status": "sl",
                                "change": getStopLose("hit_and_run", False),
                            }
                            output["data"].append(data)
                            output["lose_num"] += 1
                            break

    return output
