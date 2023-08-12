import threading

import pandas

import const_app as const_app
from strategies.trend_following.back_test_trend_following import long_backTest_optimized, sell_backTest_optimized
from utils.boost import boost
from utils.util_back_test import allStatistic, printStatistic


# Function to show next indicator data
def show_trend_following_data(ticker, frame):
    const_app.numberOfSuccessLongSignal = 0
    const_app.numberOfSuccessShortSignal = 0

    # Read data from CSV file
    df = pandas.read_csv(f"{const_app.saveDataFolder}{ticker}-{frame}-indicators.csv")

    if const_app.strategies["trend_following"]["config"]["long"]:
        # Perform long backtest
        dataLong = long_backTest_optimized(df, ticker, frame)
        allStatistic(dataLong, frame, ticker, 'Trend Following', False)

    if const_app.strategies["trend_following"]["config"]["short"]:
        # Perform sell backtest
        dataSell = sell_backTest_optimized(df, ticker, frame)
        allStatistic(dataSell, frame, ticker, 'Trend Following', True)


def trendFollowingIndicatorBackText():
    # Create a list to store the threads
    thread_list = []

    for frame in const_app.intervals:
        # Create a thread for each combination of ema and frame
        th = threading.Thread(target=boost, args=(show_trend_following_data, const_app.tickers, frame))
        thread_list.append(th)
        th.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    printStatistic()
