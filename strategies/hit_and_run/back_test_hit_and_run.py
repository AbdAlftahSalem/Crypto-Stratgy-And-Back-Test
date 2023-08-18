from utils.util import getNumByChange
from utils.util_back_test import getProfit, getTradeData, getStopLose


def longBackTest(df, ticker: str, frame: str):
    df["sponge_bob_long"] = df["sponge_bob_long"].fillna(0)

    output = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}

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
                if df.iloc[j]["low"] <= enterCandle["enterPrice"]:
                    # loop through candles until targetPrice or stopPrice is reached
                    for k in range(j, len(df)):
                        # check if current candle high is greater than or equal targetPrice
                        if df.iloc[k]["high"] >= targetPrice:
                            data = {
                                "entryDate": enterCandle["date"],
                                "outDate": df.iloc[k]["date"],
                                "enterPrice": enterCandle["enterPrice"],
                                "tp": targetPrice,
                                "sl": stopPrice,
                                "status": "tp",
                                "change": getProfit("hit_and_run", frame, True),
                            }
                            output["data"].append(data)
                            output["profitNum"] += 1
                            break

                        # check if current candle low is less than or equal stopPrice
                        elif df.iloc[k]["close"] <= stopPrice:
                            data = {
                                "entryDate": enterCandle["date"],
                                "outDate": df.iloc[k]["date"],
                                "enterPrice": enterCandle["enterPrice"],
                                "tp": targetPrice,
                                "sl": stopPrice,
                                "status": "sl",
                                "change": -getStopLose("hit_and_run", True),
                            }
                            output["data"].append(data)
                            output["loseNum"] += 1
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
        A dictionary containing the backtest results.

    """
    searchProfit = False
    profit = 0
    stop = 0
    enterCandle = combined_df.iloc[0]
    combined_df["sponge_bob_short"] = combined_df["sponge_bob_long"].fillna(0)

    output = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}

    for i in range(len(combined_df)):
        enterCandleSearch = combined_df.iloc[i]
        condition = (enterCandleSearch["sponge_bob_short"] != 0 and
                     enterCandleSearch["mfi"] >= 65 and
                     enterCandleSearch["rsi"] >= 65
                     )

        if (
                condition
                and not searchProfit
        ):
            enterCandle = combined_df.iloc[i]
            profitPCT = getProfit("hit_and_run", frame, False)
            profit = getNumByChange(enterCandle["close"], profitPCT * -1)
            stop = getNumByChange(enterCandle["close"], ((profitPCT / getStopLose("hit_and_run", True)) * 1))
            searchProfit = True

        if searchProfit:
            if combined_df.iloc[i]["low"] <= profit:
                output["data"].append(
                    getTradeData("hit_and_run", False, enterCandle, combined_df.iloc[i], profit, stop, "tp", frame))
                output["profitNum"] += 1
                searchProfit = False
                i += 1
                continue

            elif combined_df.iloc[i]["high"] >= stop:
                output["data"].append(
                    getTradeData("hit_and_run", False, enterCandle, combined_df.iloc[i], profit, stop, "sl", frame))
                output["loseNum"] += 1
                searchProfit = False
                i += 1
                continue

    return output
