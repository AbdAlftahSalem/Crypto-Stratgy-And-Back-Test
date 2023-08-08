import threading

import pandas

import const_app as const_app
from back_test_nwe import longBackTest, sellBackTest
from boost import boost
from util_back_test import allStatistic, printStatistic


# Function to show next indicator data
def showNweData(ticker, frame, ema, vwap, numberOfSuccessLongSignal, numberOfSuccessShortSignal):

    # Read data from CSV file
    df = pandas.read_csv(f"{const_app.saveDataFolder}{ticker}-{frame}-indicators.csv")

    # Perform long backtest
    dataLong = longBackTest(df, ticker, frame, vwap)

    # Perform sell backtest
    dataSell = sellBackTest(df, ticker, frame, vwap)

    allStatistic(dataLong, dataSell, ema, frame, ticker, '')


def nweIndicatorBackText():
    # Create a list to store the threads
    thread_list = []
def nweIndicatorBackText(intervals, tickers):
    thread_list = []
    for frame in intervals:
        th = threading.Thread(target=boost, args=(showNweData, tickers, frame, '', ''))
        thread_list.append(th)
        th.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    printStatistic()