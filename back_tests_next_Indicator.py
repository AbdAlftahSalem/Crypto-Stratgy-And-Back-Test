from util import getChange, getNumByChange


def longBackTest(combined_df, ticker: str, frame: str, ema: str):
    searchProfit = False
    profit = 0
    stop = 0

    enterCandle = combined_df.iloc[0]
    outPut = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}

    for i in range(len(combined_df)):
        enterCandleSearch = combined_df.iloc[i]

        if enterCandleSearch["signal"] == "buy" and not searchProfit and getChange(enterCandleSearch["high"],
                                                                                   enterCandleSearch[
                                                                                       "low"]) < 2 and getEMA(ema,
                                                                                                              enterCandleSearch,
                                                                                                              "long"):
            enterCandle = combined_df.iloc[i]
            profitPCT = getProfit(frame)
            profit = getNumByChange(enterCandle["close"], profitPCT)
            stop = getNumByChange(enterCandle["close"], ((profitPCT / 2) * -1))
            searchProfit = True

        if searchProfit:
            if combined_df.iloc[i]["high"] >= profit:
                outPut["data"].append(getTradeData(enterCandle, combined_df.iloc[i], profit, stop, "tp", frame))
                outPut["profitNum"] += 1
                searchProfit = False
                continue

            elif combined_df.iloc[i]["low"] <= stop:
                outPut["data"].append(getTradeData(enterCandle, combined_df.iloc[i], profit, stop, "sl", frame))
                outPut["loseNum"] += 1
                searchProfit = False
                continue

    return outPut


def sellBackTest(combined_df, ticker: str, frame: str, ema: str):
    searchProfit = False
    profit = 0
    stop = 0
    enterCandle = combined_df.iloc[0]

    outPut = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}

    for i in range(len(combined_df)):
        enterCandleSearch = combined_df.iloc[i]
        if enterCandleSearch["signal"] == "sell" and not searchProfit and getChange(enterCandleSearch["high"],
                                                                                    enterCandleSearch[
                                                                                        "low"]) < 2 and getEMA(ema,
                                                                                                               enterCandleSearch,
                                                                                                               "short"):
            enterCandle = combined_df.iloc[i]
            profitPCT = getProfit(frame)
            profit = getNumByChange(enterCandle["close"], profitPCT * -1)
            stop = getNumByChange(enterCandle["close"], (profitPCT / 2))
            searchProfit = True

        if searchProfit:
            if combined_df.iloc[i]["low"] <= profit:
                outPut["data"].append(getTradeData(enterCandle, combined_df.iloc[i], profit, stop, "tp", frame))
                outPut["profitNum"] += 1
                searchProfit = False
                i += 1
                continue

            elif combined_df.iloc[i]["high"] >= stop:
                outPut["data"].append(getTradeData(enterCandle, combined_df.iloc[i], profit, stop, "sl", frame))
                outPut["loseNum"] += 1
                searchProfit = False
                i += 1
                continue

    return outPut


def getProfit(frame: str):
    if frame == "15m":
        return 1.5

    elif frame == "30m":
        return 3

    elif frame == "1h":
        return 5


def getTradeData(enterCandle, exitCandle, profit, stop, status, frame):
    return {
        "entryDate": enterCandle['date'],
        "outDate": exitCandle['date'],
        "enterPrice": enterCandle['close'],
        "tp": profit,
        "sl": stop,
        "status": status,
        "change": getProfit(frame)
    }


def getEMA(ema: str, enterCandleSearch, trade_type: str):
    if trade_type == "long":
        return enterCandleSearch[ema] <= enterCandleSearch["close"]
    elif trade_type == "short":
        return enterCandleSearch[ema] >= enterCandleSearch["close"]
    elif ema == "None":
        return True
