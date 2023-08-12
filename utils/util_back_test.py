from datetime import datetime

from colorama import Fore

import const_app


def getProfit(strategy: str, frame: str, long: bool):
    """
    Get the profit percentage based on the given time frame.

    Returns:
        The profit percentage.
        :param long:
        :param frame:
        :param strategy:

    """
    if frame == "5m":
        return const_app.strategies[strategy]["tp"]["long" if long else "short"]["tp5m"]

    elif frame == "15m":
        return const_app.strategies[strategy]["tp"]["long" if long else "short"]["tp15m"]

    elif frame == "30m":
        return const_app.strategies[strategy]["tp"]["long" if long else "short"]["tp30m"]

    elif frame == "1h":
        return const_app.strategies[strategy]["tp"]["long" if long else "short"]["tp1h"]

    elif frame == "4h":
        return const_app.strategies[strategy]["tp"]["long" if long else "short"]["tp4h"]


def getStopLose(strategy: str, long: bool):
    """
    Get the stop lose percentage based on the given strategy.

    Returns:
        The stop lose percentage.
        :param strategy:
        :param long:

    """
    return const_app.strategies[strategy]["tp"]["long" if long else "short"]["sl"]


def getTradeData(strategy, long, enterCandle, exitCandle, profit, stop, status, frame):
    """
    Get the trade data for a specific trade.

    Args:
        enterCandle: The enter candle data.
        exitCandle: The exit candle data.
        profit: The profit target.
        stop: The stop loss target.
        status: The trade status.
        frame: The time frame.
        strategy: The strategy name.
        long: The long status.

    """
    return {
        "entryDate": enterCandle["date"],
        "outDate": exitCandle["date"],
        "enterPrice": enterCandle["close"],
        "tp": profit,
        "sl": stop,
        "status": status,
        "change": getProfit(strategy, frame, long),
    }


def getDetailOfSignals(data):
    loseNum = 0
    winNum = 0
    changeWin = 0
    changeLose = 0
    wallet = 100
    summDiffDate = 0

    for i in data:
        entryDate = datetime.strptime(i["entryDate"], '%Y-%m-%d %H:%M:%S')
        outDate = datetime.strptime(i["outDate"], '%Y-%m-%d %H:%M:%S')

        summDiffDate += (outDate - entryDate).total_seconds() / 3600
        if i["status"] == "tp":
            winNum += 1
            changeWin += i["change"]
            wallet += ((i["change"] / 100) * wallet)
        else:
            loseNum += 1
            changeLose -= i["change"]
            wallet -= ((i["change"] / 100) * wallet)

    pctSuccess = f"{round((winNum / (winNum + loseNum)) * 100, 2)}%"
    wallet = f"{round(wallet, 2)} $"
    avgWaitingDate = summDiffDate / len(data)

    return winNum, loseNum, round(changeWin, 2), round(changeLose, 2), 100, wallet, pctSuccess, round(avgWaitingDate, 2)


def allStatistic(data, frame, ticker, prefixMessage, sell=False):
    try:
        if not sell:
            # Calculate statistics for long trades
            winNumLong, loseNumLong, changeWinLong, changeLoseLong, startWalletLong, endWalletLong, pctSuccessLong, avgWaitingLong = getDetailOfSignals(
                data["data"])
            print_buy(data, frame, prefixMessage, ticker)

        else:
            # Calculate statistics for short trades
            winNumShort, loseNumShort, changeWinShort, changeLoseShort, startWalletShort, endWalletShort, pctSuccessShort, avgWaitingShort = getDetailOfSignals(
                data["data"])
            print_sell(data, frame, prefixMessage, ticker)



    except Exception as e:
        print(e)


def print_buy(dataLong, frame, prefixMessage, ticker):
    # Calculate total win and lose percentages for long signals
    total_lose_pct = round(sum((d["change"] if d["status"] == "sl" else 0) for d in dataLong["data"]), 2)
    total_win_pct = round(sum((d["change"] if d["status"] == "tp" else 0) for d in dataLong["data"]), 2)
    # Update overall win and lose counts
    const_app.numberOfSuccessLongSignal += dataLong['profitNum']
    const_app.numberOfLoseLongSignal += dataLong['loseNum']
    const_app.summationOfSuccessLongPCT += total_win_pct
    const_app.summationOfLoseLongPCT += total_lose_pct
    # Print buy signal statistics
    print(
        Fore.GREEN + f"{prefixMessage} || BUY || Ticker: {ticker}, Frame: {frame}, Profit number: {dataLong['profitNum']}, Lose number: {dataLong['loseNum']} || ALL WIN CHANGE: +{total_win_pct}% || ALL LOSE CHANGE: {total_lose_pct}% || SUCCESS PCT: {round((dataLong['profitNum'] / (dataLong['profitNum'] + dataLong['loseNum'])) * 100, 2)}%\n")

    # # print last 7 buy signal
    # for i in dataLong['data'][-7:]:
    #     print(Fore.GREEN + f"{i}")


def print_sell(dataSell, frame, prefixMessage, ticker):
    # Calculate total win and lose percentages for sell signals
    total_lose_pct = round(sum((float(d["change"]) if d["status"] == "sl" else 0) for d in dataSell["data"]), 2)
    total_win_pct = round(sum((float(d["change"]) if d["status"] == "tp" else 0) for d in dataSell["data"]), 2)
    # Update overall win and lose counts
    const_app.allWin += dataSell['profitNum']
    const_app.allLose += dataSell['loseNum']
    const_app.numberOfSuccessShortSignal += dataSell['profitNum']
    const_app.numberOfLoseShortSignal += dataSell['loseNum']
    const_app.summationOfSuccessShortPCT += total_win_pct
    const_app.summationOfLoseShortPCT += total_lose_pct
    # Print sell signal statistics
    print(
        Fore.RED + f"{prefixMessage} || SELL || Ticker: {ticker}, Frame: {frame}, Profit number: {dataSell['profitNum']}, Lose number: {dataSell['loseNum']} || ALL WIN CHANGE: +{total_win_pct}% || ALL LOSE CHANGE: {total_lose_pct}% || SUCCESS PCT: {round((dataSell['profitNum'] / (dataSell['profitNum'] + dataSell['loseNum'])) * 100, 2)}%\n")

    # # print last 7 sell signal
    # for i in dataSell['data'][-7:]:
    #     print(Fore.RED + f"{i}")


def printStatistic():
    print(f"******************************************************************************\n")
    print(f"Tickers search                         : {const_app.tickers}")
    print(f"Interval search                        : {const_app.intervals}\n\n")
    print(Fore.GREEN + f"Number Of Success Long Signal          : +{const_app.numberOfSuccessLongSignal}")
    print(Fore.GREEN + f"Number Of Success Short Signal         : +{const_app.numberOfSuccessShortSignal}")
    print(
        Fore.GREEN + f"Number all success signal               : {round(const_app.numberOfSuccessLongSignal + const_app.numberOfSuccessShortSignal, 2)}\n\n")
    print(Fore.RED + f"Number Of Lose Long Signal             : -{const_app.numberOfLoseLongSignal}")
    print(Fore.RED + f"Number Of Lose Short Signal            : -{const_app.numberOfLoseShortSignal}")
    print(
        Fore.RED + f"Number all lose signal                 : {round(const_app.numberOfLoseLongSignal + const_app.numberOfLoseShortSignal, 2)}\n\n")
    print(Fore.GREEN + f"Summation Of Success Long PCT          : +{const_app.summationOfSuccessLongPCT} %")
    print(Fore.GREEN + f"Summation Of Success Short PCT         : +{const_app.summationOfSuccessShortPCT} %")
    print(Fore.RED + f"Summation Of Lose Long PCT             : -{const_app.summationOfLoseLongPCT} %")
    print(Fore.RED + f"Summation Of Lose Short PCT            : -{const_app.summationOfLoseShortPCT} %\n")
    print(
        Fore.RED + f"Summation of Lose in Long and Short    : -{const_app.summationOfLoseShortPCT + const_app.summationOfLoseLongPCT} %")
    print(
        Fore.GREEN + f"Summation of Success in Long and Short : +{const_app.summationOfSuccessShortPCT + const_app.summationOfSuccessLongPCT} %\n")
    print(f"******************************************************************************\n")
