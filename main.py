import const_app
import get_data
from indecators.add_all_indecator_to_csv import add_all_indicator_to_csv
from strategies.hit_and_run.full_back_test import hitAndRunIndicatorBackText
from utils.send_to_tele import sentToTelegram

# Importing the 'get_data' module

# Importing the 'nextIndicatorBackText' function from 'full_back_test' module

# Checking the value of 'get_data' attribute in 'const_app' module to check to get data from binance or not
if const_app.get_data:
    # Calling the 'getDataForAllTickers' function from 'get_data' module to get data from binance and save it in .csv file
    get_data.getDataForAllTickers()

# apply all indicator to csv
if const_app.apply_strategy:
    add_all_indicator_to_csv()
    sentToTelegram("******************* \n\nFINISH GET DATA ******************* \n\n")

# Calling the 'nextIndicatorBackText' function from 'full_back_test' module to start testing
# nweIndicatorBackText()
# trendFollowingIndicatorBackText()
hitAndRunIndicatorBackText()
