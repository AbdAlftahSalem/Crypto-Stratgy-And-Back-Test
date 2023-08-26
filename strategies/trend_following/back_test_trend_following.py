from utils.util import getNumByChange
from utils.util_back_test import getProfit, getTradeData, getStopLose


def long_backTest_optimized(combined_df, ticker: str, frame: str):
    enterCandle = combined_df.iloc[0]
    close = combined_df["close"]
    high = combined_df["high"]
    low = combined_df["low"]

    ema20 = combined_df["ema20"]
    ema50 = combined_df["ema50"]
    ema100 = combined_df["ema100"]
    ema200 = combined_df["ema200"]
    superTrend = combined_df["superTrend"]
    cci = combined_df["cci"]
    vwap21 = combined_df["vwap21"]
    vwap50 = combined_df["vwap50"]
    vwap100 = combined_df["vwap100"]
    vwap200 = combined_df["vwap200"]

    profitPCT = getProfit("trend_following", frame, True)

    output = {"ticker": ticker, "interval": frame, "profit_num": 0, "lose_num": 0, "data": []}

    searchProfit = False

    for i in range(len(combined_df)):
        currentCandleSearch = combined_df.iloc[i]
        previousCandleSearch = combined_df.iloc[i - 1]
        previousPreviousCandleSearch = combined_df.iloc[i - 2]

        profit = getNumByChange(enterCandle["close"], profitPCT)
        stop = getNumByChange(enterCandle["close"], ((profitPCT / getStopLose("trend_following", True)) * -1))

        # check if close upper than vwap21 and vwap50 and vwap100 and vwap200 , check if ema10 ema20 upper than ema50 and ema100 and ema200 , check if superTrend is lower than close
        condition = (
                close[i] > vwap21[i] > vwap50[i] > vwap100[i] > vwap200[i] and
                superTrend[i] < close[i] and
                cci[i] > 100

        )

        # check if low previous candle is less than previous previous candle low and less than current candle low and high previous previous candle is upper than previous candle high and current candle high upper than previous candle high and previous previous candle high
        # condition = condition and (
        #         previousCandleSearch["low"] < previousPreviousCandleSearch["low"] < currentCandleSearch["low"] and
        #         previousPreviousCandleSearch["high"] > previousCandleSearch["high"] < currentCandleSearch["high"]
        # )

        if condition and not searchProfit:
            enterCandle = currentCandleSearch
            searchProfit = True

        if searchProfit:
            if high[i] >= profit:
                output["data"].append(
                    getTradeData("trend_following", True, enterCandle, currentCandleSearch, profit, stop, "tp", frame)
                )
                output["profit_num"] += 1
                searchProfit = False

            elif low[i] <= stop:
                output["data"].append(
                    getTradeData("trend_following", True, enterCandle, currentCandleSearch, profit, stop, "sl", frame)
                )
                output["lose_num"] += 1
                searchProfit = False

    return output


def sell_backtest_optimized(combined_df, ticker: str, frame: str):
    enterCandle = combined_df.iloc[0]
    ema20 = combined_df["ema20"]
    ema50 = combined_df["ema50"]
    ema100 = combined_df["ema100"]
    ema200 = combined_df["ema200"]
    superTrend = combined_df["superTrend"]
    close = combined_df["close"]
    high = combined_df["high"]
    low = combined_df["low"]

    profitPCT = getProfit("trend_following", frame, False)

    output = {"ticker": ticker, "interval": frame, "profit_num": 0, "lose_num": 0, "data": []}

    searchProfit = False

    for i in range(len(combined_df)):
        enterCandleSearch = combined_df.iloc[i]
        previousCandleSearch = combined_df.iloc[i - 1]
        previousPreviousCandleSearch = combined_df.iloc[i - 2]

        profit = getNumByChange(enterCandle["close"], profitPCT * -1)
        stop = getNumByChange(enterCandle["close"], ((profitPCT / getStopLose("trend_following", True)) * 1))
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
                    getTradeData("trend_following", False, enterCandle, enterCandleSearch, profit, stop, "tp", frame)
                )
                output["profit_num"] += 1
                searchProfit = False

            elif high[i] >= stop:
                output["data"].append(
                    getTradeData("trend_following", False, enterCandle, enterCandleSearch, profit, stop, "sl", frame)
                )
                output["lose_num"] += 1
                searchProfit = False

    return output
