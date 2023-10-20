import threading

import pandas

import const_app as const_app
from utils.boost import boost
from utils.util_back_test import allStatistic, printStatistic


def show_data_helper(ticker, frame, longBackTest, sellBackTest):
    const_app.numberOfSuccessLongSignal = 0
    const_app.numberOfSuccessShortSignal = 0

    # Read data from CSV file
    df = pandas.read_csv(f"{const_app.saveDataFolderIndicator}{ticker}-{frame}-indicators.csv")

    if const_app.strategies["nwe"]["config"]["long"]:
        # Perform long backtest
        dataLong = longBackTest(df, ticker, frame)
        if len(dataLong["data"]) > 0:
            # plot_with_signals(df, dataLong)
            allStatistic(dataLong, frame, ticker, 'Nwe', False)

    if const_app.strategies["nwe"]["config"]["short"]:

        # Perform sell backtest
        dataSell = sellBackTest(df, ticker, frame)
        if len(dataSell["data"]) > 0:
            allStatistic(dataSell, frame, ticker, 'Nwe', True)


def threadData(longBackTest, sellBackTest):
    # Create a list to store the threads
    thread_list = []

    for interval in ["1h"]:
        # Create a thread for each combination of ema and frame
        th = threading.Thread(target=boost,
                              args=(show_data_helper, const_app.tickers, interval, longBackTest, sellBackTest))
        thread_list.append(th)
        th.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    printStatistic()
