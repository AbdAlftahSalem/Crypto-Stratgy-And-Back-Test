import threading

import pandas

import const_app as const_app
from strategies.mrc.back_test_mrc import longBackTestOptimized, sellBackTestOptimized
from utils.boost import boost
from utils.util_back_test import allStatistic, printStatistic


# Function to show next indicator data
def showMRCData(ticker, frame, ema, vwap):
    const_app.numberOfSuccessLongSignal = 0
    const_app.numberOfSuccessShortSignal = 0

    # Read data from CSV file
    df = pandas.read_csv(f"{const_app.saveDataFolder}{ticker}-{frame}-indicators.csv")

    # Perform long backtest
    dataLong = longBackTestOptimized(df, ticker, frame)

    # Perform sell backtest
    dataSell = sellBackTestOptimized(df, ticker, frame)

    allStatistic(dataLong, dataSell, ema, frame, ticker, 'MRC')


def mrcIndicatorBackText():
    # Create a list to store the threads
    thread_list = []

    for frame in const_app.intervals:
        # Create a thread for each combination of ema and frame
        th = threading.Thread(target=boost, args=(showMRCData, const_app.tickers, frame, '', ''))
        thread_list.append(th)
        th.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    printStatistic()
