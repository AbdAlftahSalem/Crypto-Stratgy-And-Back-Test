from strategies.hit_and_run.back_test_hit_and_run import longBackTest, sellBackTest
from strategies.show_data_helper import threadData


# Function to show next indicator data
def show_hit_and_run_data(ticker, frame):
    threadData(longBackTest, sellBackTest)

#     const_app.numberOfSuccessLongSignal = 0
#     const_app.numberOfSuccessShortSignal = 0
#
#     # Read data from CSV file
#     df = pandas.read_csv(f"{const_app.saveDataFolderIndicator}{ticker}-{frame}-indicators.csv")
#
#     if const_app.strategies["hit_and_run"]["config"]["long"]:
#         # Perform long backtest
#         dataLong = longBackTest(df, ticker, frame)
#         allStatistic(dataLong, frame, ticker, 'Hit And Run', False)
#
#     if const_app.strategies["hit_and_run"]["config"]["short"]:
#         # Perform sell backtest
#         dataSell = sellBackTest(df, ticker, frame)
#         allStatistic(dataSell, frame, ticker, 'Hit And Run', True)
#
#
# def hitAndRunIndicatorBackText():
#     # Create a list to store the threads
#     thread_list = []
#
#     for frame in ['15m', '30m', '1h']:
#         # Create a thread for each combination of ema and frame
#         th = threading.Thread(target=boost, args=(show_hit_and_run_data, const_app.tickers, frame))
#         thread_list.append(th)
#         th.start()
#
#     # Wait for all threads to complete
#     for thread in thread_list:
#         thread.join()
#
#     printStatistic()
