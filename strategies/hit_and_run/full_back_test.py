import threading

import pandas

import const_app as const_app
from strategies.hit_and_run.back_test_sponge_bob import longBackTest, sellBackTest
from utils.boost import boost
from utils.util_back_test import allStatistic, printStatistic


# Function to show next indicator data
def show_nwe_data(ticker, frame):
    const_app.numberOfSuccessLongSignal = 0
    const_app.numberOfSuccessShortSignal = 0

    # Read data from CSV file
    df = pandas.read_csv(f"{const_app.saveDataFolder}{ticker}-{frame}-indicators.csv")

    if const_app.strategies["hit_and_run"]["config"]["long"]:
        # Perform long backtest
        dataLong = longBackTest(df, ticker, frame)
        allStatistic(dataLong, frame, ticker, 'Nwe', False)

    if const_app.strategies["hit_and_run"]["config"]["short"]:
        # Perform sell backtest
        dataSell = sellBackTest(df, ticker, frame)
        allStatistic(dataSell, frame, ticker, 'Nwe', True)


def nweIndicatorBackText():
    # Create a list to store the threads
    thread_list = []

    for frame in const_app.intervals:
        # Create a thread for each combination of ema and frame
        th = threading.Thread(target=boost, args=(show_nwe_data, const_app.tickers, frame))
        thread_list.append(th)
        th.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    printStatistic()
