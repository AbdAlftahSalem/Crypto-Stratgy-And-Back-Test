import const_app
from util import getChange, getNumByChange


def longBackTest(combined_df, ticker: str, frame: str, ema: str, vwap: str):
    """
    Perform a long backtest on the combined DataFrame.

    Args:
        combined_df: The combined DataFrame containing the data.
        ticker: The ticker symbol.
        frame: The time frame.
        ema: The Exponential Moving Average (EMA) to consider.
        vwap: VWAP.

    Returns:
        A dictionary containing the backtest results.


    """
    searchProfit = False
    profit = 0
    stop = 0
    enterCandle = combined_df.iloc[0]

    output = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}

    for i in range(len(combined_df)):
        enterCandleSearch = combined_df.iloc[i]
        if (
                enterCandleSearch["signal"] == "buy"
                and not searchProfit
                and getChange(enterCandleSearch["high"], enterCandleSearch["low"]) < 2
                #  this condition to search in strategy with EMA and without it
                and getVWAP(vwap, enterCandleSearch, "long")
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


def sellBackTest(combined_df, ticker: str, frame: str, ema: str, vwap: str):
    """
    Perform a sell backtest on the combined DataFrame.

    Args:
        combined_df: The combined DataFrame containing the data.
        ticker: The ticker symbol.
        frame: The time frame.
        ema: The Exponential Moving Average (EMA) to consider.
        vwap: VWAP.


    Returns:
        A dictionary containing the backtest results.

    """
    searchProfit = False
    profit = 0
    stop = 0
    enterCandle = combined_df.iloc[0]

    output = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}

    for i in range(len(combined_df)):
        enterCandleSearch = combined_df.iloc[i]

        if (
                enterCandleSearch["signal"] == "sell"
                and not searchProfit
                and getChange(enterCandleSearch["high"], enterCandleSearch["low"]) < 2
                #  this condition to search in strategy with EMA and without it
                and getEMA(ema, enterCandleSearch, "short")
        ):
            enterCandle = combined_df.iloc[i]
            profitPCT = getProfit(frame)
            profit = getNumByChange(enterCandle["close"], profitPCT * -1)
            stop = getNumByChange(enterCandle["close"], (profitPCT / 2))
            searchProfit = True

        if searchProfit:
            if combined_df.iloc[i]["low"] <= profit:
                output["data"].append(
                    getTradeData(enterCandle, combined_df.iloc[i], profit, stop, "tp", frame)
                )
                output["profitNum"] += 1
                searchProfit = False
                i += 1
                continue

            elif combined_df.iloc[i]["high"] >= stop:
                output["data"].append(
                    getTradeData(enterCandle, combined_df.iloc[i], profit, stop, "sl", frame)
                )
                output["loseNum"] += 1
                searchProfit = False
                i += 1
                continue

    return output


def getProfit(frame: str):
    """
    Get the profit percentage based on the given time frame.

    Args:
        frame: The time frame.

    Returns:
        The profit percentage.

    """
    if frame == "15m":
        return const_app.interval15mTpPCT

    elif frame == "30m":
        return const_app.interval30mTpPCT

    elif frame == "1h":
        return const_app.interval1hTpPCT


def getTradeData(enterCandle, exitCandle, profit, stop, status, frame):
    """
    Get the trade data for a specific trade.

    Args:
        enterCandle: The enter candle data.
        exitCandle: The exit candle data.
        profit: The profit target.
        stop: The stop loss target.
        status: The trade status.
        frame: The time frame.

    Returns:
        A dictionary containing the trade data.

    """
    return {
        "entryDate": enterCandle["date"],
        "outDate": exitCandle["date"],
        "enterPrice": enterCandle["close"],
        "tp": profit,
        "sl": stop,
        "status": status,
        "change": getProfit(frame),
    }


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


def getVWAP(ema: str, enterCandleSearch, trade_type: str):
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
        return enterCandleSearch[ema] <= enterCandleSearch["close"]
    elif trade_type == "short":
        return enterCandleSearch[ema] >= enterCandleSearch["close"]
    elif ema == "None":
        return True
