import const_app as const_app
from utils.util import getNumByChange
from utils.util_back_test import getProfit, getTradeData


def longBackTestOptimized(combined_df, ticker: str, frame: str):
    output = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}
    enterCandle = combined_df.iloc[0]

    rsi_condition = combined_df["rsi"] < 20
    mfi_condition = combined_df["mfi"] < 20
    cci_condition = combined_df["cci"] < -200

    searchProfit = False
    profit = 0
    stop = 0

    for i in range(len(combined_df)):
        currentCandleSearch = combined_df.iloc[i]

        if (
                rsi_condition[i]
                and mfi_condition[i]
                and cci_condition[i]
        ):
            enterCandle = currentCandleSearch
            profitPCT = getProfit(frame)
            profit = getNumByChange(enterCandle["close"], profitPCT)
            stop = getNumByChange(enterCandle["close"], ((profitPCT / const_app.stopLosePCTFromTPPCT) * -1))
            searchProfit = True

        if searchProfit:
            if currentCandleSearch["high"] >= profit:
                output["data"].append(
                    getTradeData(enterCandle, currentCandleSearch, profit, stop, "tp", frame)
                )
                output["profitNum"] += 1
                searchProfit = False
                continue

            elif currentCandleSearch["low"] <= stop:
                output["data"].append(
                    getTradeData(enterCandle, currentCandleSearch, profit, stop, "sl", frame)
                )
                output["loseNum"] += 1
                searchProfit = False
                continue

    return output


def sellBackTestOptimized(combined_df, ticker: str, frame: str):
    output = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}
    enterCandle = combined_df.iloc[0]

    rsi_condition = combined_df["rsi"] > 70
    mfi_condition = combined_df["mfi"] > 80
    cci_condition = combined_df["cci"] > 100

    searchProfit = False
    profit = 0
    stop = 0

    for i in range(len(combined_df)):
        enterCandleSearch = combined_df.iloc[i]

        if (
                rsi_condition[i]
                and mfi_condition[i]
                and cci_condition[i]
        ):
            enterCandle = enterCandleSearch
            profitPCT = getProfit(frame)
            profit = getNumByChange(enterCandle["close"], profitPCT * -1)
            stop = getNumByChange(enterCandle["close"], (profitPCT / 2))
            searchProfit = True

        if searchProfit:
            if enterCandleSearch["low"] <= profit:
                output["data"].append(
                    getTradeData(enterCandle, enterCandleSearch, profit, stop, "tp", frame)
                )
                output["profitNum"] += 1
                searchProfit = False
                continue

            elif enterCandleSearch["high"] >= stop:
                output["data"].append(
                    getTradeData(enterCandle, enterCandleSearch, profit, stop, "sl", frame)
                )
                output["loseNum"] += 1
                searchProfit = False
                continue

    return output
