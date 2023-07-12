get_data = False
"""
Flag to control whether to retrieve historical data or not.
"""

tickers = ["ETHUSDT", "SOLUSDT"]
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

ema = ["ema10", "ema20", "ema50", "ema100", "ema200"]
"""
List of Exponential Moving Average (EMA) periods to be calculated.
"""

"""
List of VWAP periods to be calculated.
"""
vwap = ["vwap21", "vwap50", "vwap21", "vwap100", "vwap200"]

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
"""
PCT TP change
"""

stopLosePCTFromTPPCT = 1
"""
# This variable will divide it from TP PCT
# if TP : 3 -> SL will be 3 / 2 = 1.5 . etc
"""

numberOfSuccessLongSignal = 0
numberOfSuccessShortSignal = 0

numberOfLoseLongSignal = 0
numberOfLoseShortSignal = 0

summationOfSuccessLongPCT = 0
summationOfSuccessShortPCT = 0

summationOfLoseLongPCT = 0
summationOfLoseShortPCT = 0
