import threading

import pandas
import pandas_ta

import const_app
from back_tests import template_back_test
from utils.boost_search import boost_back_test
from utils.util_back_test import all_statistic


def show_back_test_output(ticker, interval, strategy_name):
    # Read data from CSV file
    df = pandas.read_csv(f"{const_app.settings['saveDataFolderIndicator']}{ticker}-{interval}-indicators-new7.csv")

    data = template_back_test.template_bak_test(df, strategy_name, ticker, interval)
    if len(data["data"]) > 0:
        all_statistic(data, interval, ticker, strategy_name)


def thread_output(strategy_name):
    # Create a list to store the threads
    thread_list = []

    for interval in const_app.strategies[strategy_name]['intervals']:
        # Create a thread for each combination of ema and interval
        th = threading.Thread(target=boost_back_test,
                              args=(
                                  show_back_test_output, const_app.settings['tickers'], interval, strategy_name))
        thread_list.append(th)
        th.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()
