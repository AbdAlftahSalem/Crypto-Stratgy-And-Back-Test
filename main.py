# import const_app
# from analysis.applay_indicator_to_csv import add_all_indicator_to_csv
# from back_tests.template_back_test import show_back_test_data
# from candlles_services import multi_candles
# from utils.send_to_tele import send_message_to_telegram
# from utils.util_back_test import get_statistic_for_strategy
#
# # Checking the value of 'get_data' attribute in 'const_app' module to check to get data from binance or not
# if const_app.settings['get_data']:
#     print("🔃 Start Get Data ...")
#     multi_candles.get_data_for_all_tickers()
#     print("🚀 Finish Get Data ...")
#
# # apply all indicator to csv
# if const_app.settings['apply_strategy']:
#     print("🔃 Start apply indicators for tickers ...")
#     add_all_indicator_to_csv()
#     send_message_to_telegram("🚀 FINISH APPLY INDICATORS FOR TICKERS")
#
# if const_app.settings['startBackTest']:
#     # # Calling backtest functions
#     # show_back_test_data('nwe')
#     # show_back_test_data('support_and_resistant')
#     show_back_test_data('vwaps')
#
# if const_app.settings['showStatistic']:
#     # get_statistic_for_strategy("nwe")
#     # get_statistic_for_strategy("support_and_resistant")
#     get_statistic_for_strategy("vwaps")
#
#
#         df.to_csv(f'E:\Crypto System\dataIndicator\\{i}-{j}-indicators-new7.csv')
#         print(f"FINISH {i} , {j}")
