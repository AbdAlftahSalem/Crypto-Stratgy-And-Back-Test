get_data = True
"""
Flag to control whether to retrieve historical data or not.
"""

tickers = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "MATICUSDT", "SOLUSDT", "DOTUSDT", "AVAXUSDT",
           "LINKUSDT"]
"""
List of tickers for which historical data will be retrieved.
"""

intervals = ["15m", "30m", "1h"]
"""
List of intervals for which historical data will be retrieved.
"""

saveDataFolder = "D:\\Python project\\nadaraya_watson_envelope\\data\\"
"""
The folder path where the retrieved data will be saved.
"""

ema = ["None", "EMA10", "EMA20", "EMA50", "EMA100", "EMA200"]
"""
List of Exponential Moving Average (EMA) periods to be calculated.
"""

allWin = 0
"""
Variable to keep track of the total number of wins.
"""

allLose = 0
"""
Variable to keep track of the total number of losses.
"""

messageToTele = ""
"""
Variable to store the message to be sent to Telegram.
"""

interval15mTpPCT = 1.5
interval30mTpPCT = 3
interval1hTpPCT = 5

# This variable will divide it from TP PCT
# if TP : 3 -> SL will be 3 / 2 = 1.5 . etc
stopLosePCTFromTPPCT = 2
