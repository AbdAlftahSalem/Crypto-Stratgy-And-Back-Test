from utils.util import getNumByChange
from utils.util_back_test import getProfit, getStopLose, getTradeData


def is_hammer(row):
    return (row['open'] > row['close']) and (row['close'] - row['low'] >= 2.5 * (row['open'] - row['close']))


def isInvertedHammerCandle(row):
    return (row['close'] > row['open']) and (row['high'] - row['close'] >= 2.5 * (row['close'] - row['open']))


def longBackTest(df, ticker: str, frame: str):
    output = {"ticker": ticker, "interval": frame, "profit_num": 0, "lose_num": 0, "strategy_name": "hammer",
              "strategy_type": "Long", "start_date": df.iloc[0]["date"],
              "end_date": df.iloc[-1]["date"], "data": []}

    searchProfit = False
    profit = 0
    stop = 0
    enterCandle = df.iloc[0]

    df['IsHammer'] = df.apply(is_hammer, axis=1)

    for i in range(len(df)):
        if df.iloc[i]["IsHammer"] and df.iloc[i]["rsi"] <= 40 and not searchProfit:
            enterCandle = df.iloc[i]
            profitPCT = getProfit("hammer", frame, True)
            profit = getNumByChange(enterCandle["close"], profitPCT)
            stop = getNumByChange(enterCandle["close"], ((profitPCT / getStopLose("hammer", True)) * -1))
            searchProfit = True

        if searchProfit:
            if df.iloc[i]["high"] >= profit:
                output["data"].append(
                    getTradeData("hammer", True, enterCandle, df.iloc[i], profit, stop, "tp", frame)
                )
                output["profit_num"] += 1
                searchProfit = False
                continue

            elif df.iloc[i]["close"] <= stop:
                output["data"].append(
                    getTradeData("hammer", True, enterCandle, df.iloc[i], profit, stop, "sl", frame)
                )
                output["lose_num"] += 1
                searchProfit = False
                continue

    return output


def sellBackTest(df, ticker: str, frame: str):
    output = {"ticker": ticker, "interval": frame, "profit_num": 0, "lose_num": 0, "strategy_name": "hammer",
              "strategy_type": "Short", "start_date": df.iloc[0]["date"],
              "end_date": df.iloc[-1]["date"], "data": []}

    searchProfit = False
    profit = 0
    stop = 0
    enterCandle = df.iloc[0]

    df['IsInvertedHammer'] = df.apply(isInvertedHammerCandle, axis=1)

    for i in range(len(df)):
        if df.iloc[i]["IsInvertedHammer"] and df.iloc[i]["rsi"] >= 60 and not searchProfit:
            enterCandle = df.iloc[i]
            profitPCT = getProfit("hammer", frame, False)
            profit = getNumByChange(enterCandle["close"], -profitPCT)
            stop = getNumByChange(enterCandle["close"], (profitPCT / getStopLose("hammer", False)))
            searchProfit = True

        if searchProfit:
            if df.iloc[i]["low"] <= profit:
                output["data"].append(
                    getTradeData("hammer", False, enterCandle, df.iloc[i], profit, stop, "tp", frame)
                )
                output["profit_num"] += 1
                searchProfit = False
                continue

            elif df.iloc[i]["close"] >= stop:
                output["data"].append(
                    getTradeData("hammer", False, enterCandle, df.iloc[i], profit, stop, "sl", frame)
                )
                output["lose_num"] += 1
                searchProfit = False
                continue

    return output
