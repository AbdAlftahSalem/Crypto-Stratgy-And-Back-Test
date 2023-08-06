# Importing the 'const_app' module
from back_test import const_app, get_data
from send_to_tele import sentToTelegram
# Importing the 'get_data' module

# Importing the 'nextIndicatorBackText' function from 'full_back_test' module
from back_test.full_back_test import nextIndicatorBackText

# Checking the value of 'get_data' attribute in 'const_app' module to check to get data from binance or not
if const_app.get_data:
    # Calling the 'getDataForAllTickers' function from 'get_data' module to get data from binance and save it in .csv file
    get_data.getDataForAllTickers()

sentToTelegram("******************* \n\nFINISH GET DATA ******************* \n\n")
# Calling the 'nextIndicatorBackText' function from 'full_back_test' module to start testing
# nextIndicatorBackText()
