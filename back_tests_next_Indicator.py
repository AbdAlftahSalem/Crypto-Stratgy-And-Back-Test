from util import getChange, getNumByChange


def longBackTest(combined_df, ticker: str, frame: str, ema: str):
    searchProfit = False
    profit = 0
    stop = 0

    enterCandle = combined_df.iloc[0]
    outPut = {"ticker": ticker, "frame": frame, "profitNum": 0, "loseNum": 0, "data": []}
    for i in range(len(combined_df)):
        enterCandleSearch = combined_df.iloc[i]

        if enterCandleSearch["signal"] == "buy" and not searchProfit and getChange(
                enterCandleSearch["high"],
                enterCandleSearch[
                    "low"]) < 2 and getEMALong(ema, enterCandleSearch):
            enterCandle = combined_df.iloc[i]
            profitPCT = getProfit(frame)
            profit = getNumByChange(enterCandle["close"], profitPCT)
            stop = getNumByChange(enterCandle["close"], ((profitPCT / 2) * -1))
            searchProfit = True

        if searchProfit:
            if combined_df.iloc[i]["high"] >= profit:
                outPut["data"].append({"entryDate": enterCandle['date'], "outDate": combined_df.iloc[i]['date'],
                                       "enterPrice": enterCandle['close'], "tp": profit, "sl": stop, "status": "tp",
                                       "change": getProfit(frame)})
                outPut["profitNum"] += 1
                searchProfit = False
                continue

            elif combined_df.iloc[i]["low"] <= stop:
                outPut["data"].append({"entryDate": enterCandle['date'], "outDate": combined_df.iloc[i]['date'],
                                       "enterPrice": enterCandle['close'], "tp": profit, "sl": stop, "status": "sl",
                                       "change": -getProfit(frame) / 2})
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
        if enterCandleSearch["signal"] == "sell" and not searchProfit and getChange(
                enterCandleSearch["high"],
                enterCandleSearch[
                    "low"]) < 2 and getEMAShort(ema, enterCandleSearch):
            enterCandle = combined_df.iloc[i]
            profitPCT = getProfit(frame)
            profit = getNumByChange(enterCandle["close"], profitPCT * -1)
            stop = getNumByChange(enterCandle["close"], (profitPCT / 2))
            searchProfit = True

        if searchProfit:
            if combined_df.iloc[i]["low"] <= profit:
                outPut["data"].append({"entryDate": enterCandle['date'], "outDate": combined_df.iloc[i]['date'],
                                       "enterPrice": enterCandle['close'], "tp": profit, "sl": stop, "status": "tp",
                                       "change": getProfit(frame)})
                outPut["profitNum"] += 1
                searchProfit = False
                i += 1
                continue

            elif combined_df.iloc[i]["high"] >= stop:
                outPut["data"].append({"entryDate": enterCandle['date'], "outDate": combined_df.iloc[i]['date'],
                                       "enterPrice": enterCandle['close'], "tp": profit, "sl": stop, "status": "sl",
                                       "change": -getProfit(frame) / 2})
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


def getEMALong(ema: str, enterCandleSearch):
    if ema == "EMA200":
        return enterCandleSearch["EMA200"] <= enterCandleSearch["close"]

    elif ema == "EMA100":
        return enterCandleSearch["EMA100"] <= enterCandleSearch["close"]

    elif ema == "EMA50":
        return enterCandleSearch["EMA50"] <= enterCandleSearch["close"]

    elif ema == "EMA20":
        return enterCandleSearch["EMA20"] <= enterCandleSearch["close"]

    elif ema == "EMA10":
        return enterCandleSearch["EMA10"] <= enterCandleSearch["close"]

    elif ema == "None":
        return True


def getEMAShort(ema: str, enterCandleSearch):
    if ema == "EMA200":
        return enterCandleSearch["EMA200"] >= enterCandleSearch["close"]

    elif ema == "EMA100":
        return enterCandleSearch["EMA100"] >= enterCandleSearch["close"]

    elif ema == "EMA50":
        return enterCandleSearch["EMA50"] >= enterCandleSearch["close"]

    elif ema == "EMA20":
        return enterCandleSearch["EMA20"] >= enterCandleSearch["close"]

    elif ema == "EMA10":
        return enterCandleSearch["EMA10"] >= enterCandleSearch["close"]

    elif ema == "None":
        return True
