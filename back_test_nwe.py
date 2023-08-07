import const_app as const_app
from util import getNumByChange, getChange
from util_back_test import getProfit, getTradeData


def longBackTest(combined_df, ticker: str, frame: str, vwap: str):
    """
    Perform a long backtest on the combined DataFrame.

    Args:
        combined_df: The combined DataFrame containing the data.
        ticker: The ticker symbol.
        frame: The time frame.
        vwap: VWAP.

    Returns:
        A dictionary containing the backtest results.


    """
    searchProfit = False
    profit = 0
    stop = 0
    enterCandle = combined_df.iloc[0]

    output = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}

    for i in range(len(combined_df) - 3):
        currentCandleSearch = combined_df.iloc[i]
        nextCandleSearch = combined_df.iloc[i + 1]
        nextNextCandleSearch = combined_df.iloc[i + 2]

        # check if open and close is less than lower
        condition = (currentCandleSearch["open"] < currentCandleSearch["lower"])

        # check if low next candle is less than low current candle and less than next next candle low and close next next candle is upper than next candle close
        condition = (condition and
                     nextCandleSearch["low"] < currentCandleSearch["low"] < nextNextCandleSearch["low"] and
                     nextNextCandleSearch["close"] > nextCandleSearch["close"])

        if (
                condition
                and not searchProfit
                and getChange(currentCandleSearch["high"], currentCandleSearch["low"]) < 2
                #  this condition to search in strategy with EMA and without it
                # and getVWAP(vwap, currentCandleSearch, "long")
        ):
            enterCandle = combined_df.iloc[i]
            profitPCT = getProfit(frame)
            profit = getNumByChange(enterCandle["close"], profitPCT)
            stop = getNumByChange(enterCandle["close"], ((profitPCT / const_app.stopLosePCTFromTPPCT) * -1))
            searchProfit = True

        if searchProfit:
            if combined_df.iloc[i]["high"] >= profit:
                output["data"].append(
                    getTradeData(enterCandle, combined_df.iloc[i], profit, stop, "tp", frame)
                )
                output["profitNum"] += 1
                searchProfit = False
                continue

            elif combined_df.iloc[i]["low"] <= stop:
                output["data"].append(
                    getTradeData(enterCandle, combined_df.iloc[i], profit, stop, "sl", frame)
                )
                output["loseNum"] += 1
                searchProfit = False
                continue

    return output


def sellBackTest(combined_df, ticker: str, frame: str, vwap: str):
    """
    Perform a sell backtest on the combined DataFrame.

    Args:
        combined_df: The combined DataFrame containing the data.
        ticker: The ticker symbol.
        frame: The time frame.
        vwap: VWAP.


    Returns:
        A dictionary containing the backtest results.

    """
    searchProfit = False
    profit = 0
    stop = 0
    enterCandle = combined_df.iloc[0]

    output = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}

    for i in range(len(combined_df) - 3):
        enterCandleSearch = combined_df.iloc[i]
        nextCanldeSearch = combined_df.iloc[i + 1]
        nextNextCandleSearch = combined_df.iloc[i + 2]

        # check if open and close is greater than upper
        condition = (enterCandleSearch["open"] > enterCandleSearch["upper"])

        # check if high next candle is greater than high current candle and greater than next next candle high and close next next candle is lower than next candle close
        condition = (condition and
                     nextCanldeSearch["high"] > enterCandleSearch["high"] > nextNextCandleSearch["high"] and
                     nextNextCandleSearch["close"] < nextCanldeSearch["close"])

        if (
                condition
                and not searchProfit
                and getChange(enterCandleSearch["high"], enterCandleSearch["low"]) < 2
                #  this condition to search in strategy with EMA and without it
                # and getVWAP(vwap, enterCandleSearch, "short")
        ):
            enterCandle = combined_df.iloc[i]
            profitPCT = getProfit(frame)
            profit = getNumByChange(enterCandle["close"], profitPCT * -1)
            stop = getNumByChange(enterCandle["close"], (profitPCT / 2))
            searchProfit = True

        if searchProfit:
            if combined_df.iloc[i]["low"] <= profit:
                output["data"].append(getTradeData(enterCandle, combined_df.iloc[i], profit, stop, "tp", frame))
                output["profitNum"] += 1
                searchProfit = False
                i += 1
                continue

            elif combined_df.iloc[i]["high"] >= stop:
                output["data"].append(getTradeData(enterCandle, combined_df.iloc[i], profit, stop, "sl", frame))
                output["loseNum"] += 1
                searchProfit = False
                i += 1
                continue

    return output


def getEMA(ema: str, enterCandleSearch, trade_type: str):
    """
    Check if the current candle satisfies the EMA condition.

    Args:
        ema: The EMA to consider.
        enterCandleSearch: The current candle data.
        trade_type: The trade type (long or short).

    Returns:
        True if the condition is satisfied, False otherwise.

    """
    if trade_type == "long":
        return enterCandleSearch[ema] >= enterCandleSearch["close"]
    elif trade_type == "short":
        return enterCandleSearch[ema] <= enterCandleSearch["close"]
    elif ema == "None":
        return True


def getVWAP(vwap: str, enterCandleSearch, trade_type: str):
    """
    Check if the current candle satisfies the EMA condition.

    Args:
        vwap: The EMA to consider.
        enterCandleSearch: The current candle data.
        trade_type: The trade type (long or short).

    Returns:
        True if the condition is satisfied, False otherwise.

    """
    if trade_type == "long":
        return enterCandleSearch[vwap] >= enterCandleSearch["close"]
    elif trade_type == "short":
        return enterCandleSearch[vwap] <= enterCandleSearch["close"]
    elif vwap == "None":
        return True
