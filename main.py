# Importing the 'const_app' module
import const_app

# Importing the 'get_data' module
import get_data

# Importing the 'nextIndicatorBackText' function from 'full_back_test' module
from full_back_test import nextIndicatorBackText

# Checking the value of 'get_data' attribute in 'const_app' module to check to get data from binance or not
if const_app.get_data:
    # Calling the 'getDataForAllTickers' function from 'get_data' module to get data from binance and save it in .csv file
    get_data.getDataForAllTickers()

# Calling the 'nextIndicatorBackText' function from 'full_back_test' module to start testing
nextIndicatorBackText()
