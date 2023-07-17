import threading
from datetime import datetime

import pandas
from colorama import Fore

import const_app
from back_tests_next_Indicator import longBackTest, sellBackTest


# Function to show next indicator data
def showNextIndicatorData(ticker, frame, ema, vwap):
    # Read data from CSV file
    df = pandas.read_csv(f"{const_app.saveDataFolder}{ticker}-{frame}-indicator.csv")

    # Perform long backtest
    dataLong = longBackTest(df, ticker, frame, ema, vwap)

    # Perform sell backtest
    dataSell = sellBackTest(df, ticker, frame, ema, vwap)

    # Calculate statistics for long trades
    winNumLong, loseNumLong, changeWinLong, changeLoseLong, startWalletLong, endWalletLong, pctSuccessLong, avgWaitingLong = getDetailOfSignals(
        dataLong["data"])

    # Calculate statistics for short trades
    winNumShort, loseNumShort, changeWinShort, changeLoseShort, startWalletShort, endWalletShort, pctSuccessShort, avgWaitingShort = getDetailOfSignals(
        dataSell["data"])

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
        f"{vwap} || SELL || Ticker: {ticker}, Frame: {frame}, Profit number: {dataSell['profitNum']}, Lose number: {dataSell['loseNum']} || ALL WIN CHANGE: +{total_win_pct}% || ALL LOSE CHANGE: {total_lose_pct}% || SUCCESS PCT: {round((dataSell['profitNum'] / (dataSell['profitNum'] + dataSell['loseNum'])) * 100, 2)}%")

    # Calculate total win and lose percentages for long signals
    total_lose_pct = round(sum((d["change"] if d["status"] == "sl" else 0) for d in dataLong["data"]), 2)
    total_win_pct = round(sum((d["change"] if d["status"] == "tp" else 0) for d in dataLong["data"]), 2)

    # Print buy signal statistics
    print(
        f"{vwap} || BUY || Ticker: {ticker}, Frame: {frame}, Profit number: {dataLong['profitNum']}, Lose number: {dataLong['loseNum']} || ALL WIN CHANGE: +{total_win_pct}% || ALL LOSE CHANGE: {total_lose_pct}% || SUCCESS PCT: {round((dataLong['profitNum'] / (dataLong['profitNum'] + dataLong['loseNum'])) * 100, 2)}%\n")

    # Update overall win and lose counts
    const_app.numberOfSuccessLongSignal += dataLong['profitNum']
    const_app.numberOfLoseLongSignal += dataLong['loseNum']

    const_app.summationOfSuccessLongPCT += total_win_pct
    const_app.summationOfLoseLongPCT += total_lose_pct

    # Generate message for Telegram
    const_app.messageToTele = f"Next indicator + {ema} || LONG\n\nTICKER: {ticker}\n⏰Frame: {frame}\n💹Win number: {winNumLong}\n❌Lose number: {loseNumLong}\🔥Win change: {changeWinLong}\n🔴Change lose: {changeLoseLong}\n✅Start wallet: {startWalletLong}\n❇End wallet: {endWalletLong}\n💯PCT success: {pctSuccessLong}\n⌛AVG waiting time (h): {avgWaitingLong}\n\n\nNext indicator + {ema} || SHORT\n\nTICKER: {ticker}\n⏰Frame: {frame}\n💹Win number: {winNumShort}\n❌Lose number: {loseNumShort}\n🔥Win change: {changeWinShort}\n🔴Change lose: {changeLoseShort}\n✅Start wallet: {startWalletShort}\n❇End wallet: {endWalletShort}\n💯PCT success: {pctSuccessShort}\n⌛AVG waiting time (h): {avgWaitingShort}\n\n\n\n"
    # print(const_app.messageToTele)


def nextIndicatorBackText():
    # Create a list to store the threads
    thread_list = []

    # Iterate over ema and frame intervals
    for index in range(len(const_app.vwap)):
        for frame in const_app.intervals:
            # Create a thread for each combination of ema and frame
            th = threading.Thread(target=boost,
                                  args=(showNextIndicatorData, const_app.tickers, frame, const_app.ema[index],
                                        const_app.vwap[index]))
            thread_list.append(th)
            th.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    print(f"******************************************************************************\n")
    print(f"Tickers search                         : {const_app.tickers}")
    print(f"Interval search                        : {const_app.intervals}\n\n")
    print(Fore.GREEN + f"Number Of Success Long Signal          : +{const_app.numberOfSuccessLongSignal}")
    print(Fore.GREEN + f"Number Of Success Short Signal         : +{const_app.numberOfSuccessShortSignal}\n")
    print(Fore.RED + f"Number Of Lose Long Signal             : -{const_app.numberOfLoseLongSignal}")
    print(Fore.RED + f"Number Of Lose Short Signal            : -{const_app.numberOfLoseShortSignal}\n")
    print(Fore.GREEN + f"Summation Of Success Long PCT          : +{const_app.summationOfSuccessLongPCT} %")
    print(Fore.GREEN + f"Summation Of Success Short PCT         : +{const_app.summationOfSuccessShortPCT} %")

    print(Fore.RED + f"Summation Of Lose Long PCT             : -{const_app.summationOfLoseLongPCT} %")
    print(Fore.RED + f"Summation Of Lose Short PCT            : -{const_app.summationOfLoseShortPCT} %\n")
    print(
        Fore.RED + f"Summation of Lose in Long and Short    : -{const_app.summationOfLoseShortPCT + const_app.summationOfLoseLongPCT} %")
    print(
        Fore.GREEN + f"Summation of Success in Long and Short : +{const_app.summationOfSuccessShortPCT + const_app.summationOfSuccessLongPCT} %\n")
    print(f"******************************************************************************\n")


#  This method to increase speed for back test by using threads
#  This link in linkedin talks about using threads in this code :
#  https://www.linkedin.com/posts/abd-alftah-salem-a3ba0b1bb_%D9%83%D9%86%D8%AA-%D8%A7%D9%84%D9%8A%D9%88%D9%85-%D8%B4%D8%BA%D8%A7%D9%84-%D8%B9%D9%84%D9%89-%D8%A8%D8%B1%D9%88%D8%AC%D9%8A%D9%83%D8%AA-%D8%A8%D8%A7%D9%8A%D8%AB%D9%88%D9%86-%D9%83%D9%86%D8%AA-%D8%A8%D8%AC%D8%B1%D8%A8-activity-7072175553000222720-uYA1?utm_source=share&utm_medium=member_desktop

def boost(callback, inputTickers, interval, ema, vwap):
    try:
        thread_list = []
        for ticker in inputTickers:
            th = threading.Thread(target=callback, args=(ticker, interval, ema, vwap))
            thread_list.append(th)
            th.start()

        for thread in thread_list:
            thread.join()

    except Exception as e:
        print(f"An error occurred: {e}")


# def nextIndicatorBackText():
#     # Iterate over ema and frame intervals
#     for ema in const_app.ema:
#         for frame in const_app.intervals:
#             boost(showNextIndicatorData, const_app.tickers, frame, ema)


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
