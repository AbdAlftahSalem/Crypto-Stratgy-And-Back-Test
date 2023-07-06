import threading
from datetime import datetime

import pandas

import const_app
from back_tests_next_Indicator import longBackTest, sellBackTest


def showNextIndicatorData(ticker, frame, ema):
    df = pandas.read_csv(f"{const_app.saveDataFolder}{ticker}-{frame}-2022.csv")

    dataLong = longBackTest(df, ticker, frame, ema)
    dateSell = sellBackTest(df, ticker, frame, ema)

    winNumLong, loseNumLong, changeWinLong, changeLoseLong, startWalletLong, endWalletLong, pctSuccessLong, avgWaitingLong = getDetailOfSignals(
        dataLong["data"])
    winNumShort, loseNumShort, changeWinShort, changeLoseShort, startWalletShort, endWalletShort, pctSuccessShort, avgWaitingShort = getDetailOfSignals(
        dateSell["data"])

    total_lose_pct = round(sum((float(d["change"]) if d["status"] == "sl" else 0) for d in dateSell["data"]), 2)
    total_win_pct = round(sum((float(d["change"]) if d["status"] == "tp" else 0) for d in dateSell["data"]), 2)

    print(
        f"{ema} || SELL || Ticker: {ticker}, Frame: {frame}, Profit number: {dateSell['profitNum']}, Lose number: {dateSell['loseNum']} || ALL WIN CHANGE: +{total_win_pct}% || ALL LOSE CHANGE: {total_lose_pct}% || SUCCESS PCT: {round((dateSell['profitNum'] / (dateSell['profitNum'] + dateSell['loseNum'])) * 100, 2)}%")

    const_app.allWin += dateSell['profitNum']
    const_app.allLose += dateSell['loseNum']

    total_lose_pct = round(sum((d["change"] if d["status"] == "sl" else 0) for d in dataLong["data"]), 2)
    total_win_pct = round(sum((d["change"] if d["status"] == "tp" else 0) for d in dataLong["data"]), 2)
    print(
        f"BUY || Ticker: {ticker}, Frame: {frame}, Profit number: {dataLong['profitNum']}, Lose number: {dataLong['loseNum']} || ALL WIN CHANGE: +{total_win_pct}% || ALL LOSE CHANGE: {total_lose_pct}% || SUCCESS PCT: {round((dataLong['profitNum'] / (dataLong['profitNum'] + dataLong['loseNum'])) * 100, 2)}%\n")

    const_app.allWin += dataLong['profitNum']
    const_app.allLose += dataLong['loseNum']
    const_app.messageToTele = f"Next indicator + {ema} || LONG\n\nTICKER: {ticker}\n⏰Frame: {frame}\n💹Win number: {winNumLong}\n❌Lose number: {loseNumLong}\n🔥Win change: {changeWinLong}\n🔴Change lose: {changeLoseLong}\n✅Start wallet: {startWalletLong}\n❇End wallet: {endWalletLong}\n💯PCT success: {pctSuccessLong}\n⌛AVG waiting time (h): {avgWaitingLong}\n\n\nNext indicator + {ema} || SHORT\n\nTICKER: {ticker}\n⏰Frame: {frame}\n💹Win number: {winNumShort}\n❌Lose number: {loseNumShort}\n🔥Win change: {changeWinShort}\n🔴Change lose: {changeLoseShort}\n✅Start wallet: {startWalletShort}\n❇End wallet: {endWalletShort}\n💯PCT success: {pctSuccessShort}\n⌛AVG waiting time (h): {avgWaitingShort}\n\n\n\n"
    print(const_app.messageToTele)


def boost(callback, inputTickers, interval, ema):
    try:
        thread_list = []
        for ticker in inputTickers:
            th = threading.Thread(target=callback, args=(ticker, interval, ema))
            thread_list.append(th)
            th.start()

        for thread in thread_list:
            thread.join()

    except Exception as e:
        print(f"An error occurred: {e}")


def nextIndicatorBackText():
    for ema in const_app.ema:
        for frame in const_app.intervals:
            const_app.allWin = 0
            const_app.allLose = 0
            boost(showNextIndicatorData, const_app.tickers, frame, ema)
            print("************************************************************************************\n")
            print(f"ALL WIN {frame}: {const_app.allWin}")
            print(f"ALL LOSE {frame}: {const_app.allLose}")
            print(f"SUCCESS PCT: {round((const_app.allWin / (const_app.allWin + const_app.allLose)) * 100, 2)}%")
            print("************************************************************************************\n\n")


def getDetailOfSignals(data):
    loseNum = 0
    winNum = 0
    changeWin = 0
    changeLose = 0
    wallet = 100
    summDiffDate = 0

    for i in data:
        date1 = datetime.strptime(i["entryDate"], '%Y-%m-%d %H:%M:%S')
        date2 = datetime.strptime(i["outDate"], '%Y-%m-%d %H:%M:%S')

        summDiffDate += (date2 - date1).total_seconds() / 3600
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
