from utils.util import getNumByChange
from utils.util_back_test import getProfit, getTradeData, getStopLose


def longBackTest(combined_df, ticker: str, frame: str):
    """
    Perform a long backtest on the combined DataFrame.

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

    output = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}

    for i in range(len(combined_df)):
        currentCandleSearch = combined_df.iloc[i]

        # check if open is less than lower
        condition = (currentCandleSearch["sponge_bob_long"] is not None)

        if (
                condition
                and not searchProfit
        ):
            enterCandle = combined_df.iloc[i]
            profitPCT = getProfit("hit_and_run", frame, True)
            profit = getNumByChange(enterCandle["close"], profitPCT)
            stop = getNumByChange(enterCandle["close"], ((profitPCT / getStopLose("hit_and_run", True)) * -1))
            searchProfit = True

        if searchProfit:
            if combined_df.iloc[i]["high"] >= profit:
                output["data"].append(
                    getTradeData("hit_and_run", True, enterCandle, combined_df.iloc[i], profit, stop, "tp", frame)
                )
                output["profitNum"] += 1
                searchProfit = False
                continue

            elif combined_df.iloc[i]["low"] <= stop:
                output["data"].append(
                    getTradeData("hit_and_run", True, enterCandle, combined_df.iloc[i], profit, stop, "sl", frame)
                )
                output["loseNum"] += 1
                searchProfit = False
                continue

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

    output = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}

    for i in range(len(combined_df)):
        enterCandleSearch = combined_df.iloc[i]
        condition = (enterCandleSearch["sponge_bob_short"] is not None)

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
