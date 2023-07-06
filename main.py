import const_app
import get_data
from full_back_test import nextIndicatorBackText

if const_app.get_data:
    get_data.getDataForAllTickers()

nextIndicatorBackText()
