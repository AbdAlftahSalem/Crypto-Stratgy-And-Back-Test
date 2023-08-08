import const_app as const_app
from utils.util import getNumByChange
from utils.util_back_test import getProfit, getTradeData


def longBackTest_optimized(combined_df, ticker: str, frame: str):
    enterCandle = combined_df.iloc[0]
    ema20 = combined_df["ema20"]
    ema50 = combined_df["ema50"]
    ema100 = combined_df["ema100"]
    ema200 = combined_df["ema200"]
    superTrend = combined_df["superTrend"]
    close = combined_df["close"]
    high = combined_df["high"]
    low = combined_df["low"]

    profitPCT = getProfit(frame)

    output = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}

    searchProfit = False

    for i in range(len(combined_df)):
        currentCandleSearch = combined_df.iloc[i]
        previousCandleSearch = combined_df.iloc[i - 1]
        previousPreviousCandleSearch = combined_df.iloc[i - 2]

        profit = getNumByChange(enterCandle["close"], profitPCT)
        stop = getNumByChange(enterCandle["close"], ((profitPCT / const_app.stopLosePCTFromTPPCT) * -1))

        # check if ema20, ema50, ema100, ema200 is upper than close and close is upper than superTrend
        condition = (
                ema20[i] > ema50[i] > ema100[i] > ema200[i] and
                close[i] > superTrend[i]
        )

        # check if low previous candle is less than previous previous candle low and less than current candle low and close current candle is upper than previous candle close
        condition = (
                condition and
                previousCandleSearch["low"] < previousPreviousCandleSearch["low"] < currentCandleSearch["low"] and
                currentCandleSearch["close"] > previousCandleSearch["close"]
        )

        if condition and not searchProfit:
            enterCandle = currentCandleSearch
            searchProfit = True

        if searchProfit:
            if high[i] >= profit:
                output["data"].append(
                    getTradeData(enterCandle, currentCandleSearch, profit, stop, "tp", frame)
                )
                output["profitNum"] += 1
                searchProfit = False

            elif low[i] <= stop:
                output["data"].append(
                    getTradeData(enterCandle, currentCandleSearch, profit, stop, "sl", frame)
                )
                output["loseNum"] += 1
                searchProfit = False

    return output


def sellBackTest_optimized(combined_df, ticker: str, frame: str):
    enterCandle = combined_df.iloc[0]
    ema20 = combined_df["ema20"]
    ema50 = combined_df["ema50"]
    ema100 = combined_df["ema100"]
    ema200 = combined_df["ema200"]
    superTrend = combined_df["superTrend"]
    close = combined_df["close"]
    high = combined_df["high"]
    low = combined_df["low"]

    profitPCT = getProfit(frame)

    output = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}

    searchProfit = False

    for i in range(len(combined_df)):
        enterCandleSearch = combined_df.iloc[i]
        previousCandleSearch = combined_df.iloc[i - 1]
        previousPreviousCandleSearch = combined_df.iloc[i - 2]

        profit = getNumByChange(enterCandle["close"], profitPCT)
        stop = getNumByChange(enterCandle["close"], ((profitPCT / const_app.stopLosePCTFromTPPCT) * -1))

        # check if ema20, ema50, ema100, ema200 is lower than close and close is lower than superTrend
        condition = (
                ema20[i] < ema50[i] < ema100[i] < ema200[i] and
                close[i] < superTrend[i]
        )

        # check if high previous candle is upper than high current candle and upper than high previous previous candle and close previous previous candle is lower than previous candle close and close current candle is lower than previous candle low
        condition = (
                condition and
                previousCandleSearch["high"] > enterCandleSearch["high"] > previousPreviousCandleSearch["high"] and
                previousPreviousCandleSearch["close"] < previousCandleSearch["close"] and
                close[i] < previousCandleSearch["low"]
        )

        if condition and not searchProfit:
            enterCandle = enterCandleSearch
            searchProfit = True

        if searchProfit:
            if low[i] <= profit:
                output["data"].append(
                    getTradeData(enterCandle, enterCandleSearch, profit, stop, "tp", frame)
                )
                output["profitNum"] += 1
                searchProfit = False

            elif high[i] >= stop:
                output["data"].append(
                    getTradeData(enterCandle, enterCandleSearch, profit, stop, "sl", frame)
                )
                output["loseNum"] += 1
                searchProfit = False

    return output
