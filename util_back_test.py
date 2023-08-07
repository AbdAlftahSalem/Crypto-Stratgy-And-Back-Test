import const_app


def getProfit(frame: str):
    """
    Get the profit percentage based on the given time frame.

    Args:
        frame: The time frame.

    Returns:
        The profit percentage.

    """
    if frame == "5m":
        return const_app.interval5mTpPCT

    elif frame == "15m":
        return const_app.interval15mTpPCT

    elif frame == "30m":
        return const_app.interval30mTpPCT

    elif frame == "1h":
        return const_app.interval1hTpPCT

    elif frame == "4h":
        return const_app.interval4hTpPCT


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
