import threading

import pandas

import const_app as const_app
from strategies.trend_following.back_test_trend_following import longBackTest_optimized, sellBackTest_optimized
from utils.boost import boost
from utils.util_back_test import allStatistic, printStatistic


# Function to show next indicator data
def show_trend_followingData(ticker, frame, ema, vwap):
    const_app.numberOfSuccessLongSignal = 0
    const_app.numberOfSuccessShortSignal = 0

    # Read data from CSV file
    df = pandas.read_csv(f"{const_app.saveDataFolder}{ticker}-{frame}-indicators.csv")

    # Perform long backtest
    dataLong = longBackTest_optimized(df, ticker, frame)

    # Perform sell backtest
    dataSell = sellBackTest_optimized(df, ticker, frame)

    allStatistic(dataLong, dataSell, ema, frame, ticker, 'Trend Following')


def trendFollowingIndicatorBackText():
    # Create a list to store the threads
    thread_list = []

    for frame in ["5m"]:
        # Create a thread for each combination of ema and frame
        th = threading.Thread(target=boost, args=(show_trend_followingData, const_app.tickers, frame, '', ''))
        thread_list.append(th)
        th.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    printStatistic()
