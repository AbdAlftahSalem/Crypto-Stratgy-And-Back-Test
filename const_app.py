get_data = False
"""
Flag to control whether to retrieve historical data or not.
"""

apply_strategy = False
"""
Flag to control whether to apply strategy or not.
"""

tickers = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "ADAUSDT"]
"""
List of tickers for which historical data will be retrieved.
"""

intervals = ["5m", "15m", "30m", "1h", "4h"]
"""
List of intervals for which historical data will be retrieved.
"""

saveDataFolder = "E:\\Crypto System\\data2\\"
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

interval5mTpPCT = 3
interval15mTpPCT = 4
interval30mTpPCT = 5
interval1hTpPCT = 6
interval4hTpPCT = 7
"""
PCT TP change
"""

stopLosePCTFromTPPCT = 2
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

#  data for strategy

time_start_15m = [14, 29, 44, 59]
time_start_30m = [29, 59]
time_start_1h = [59]

tickers_search = ["SOLUSDT", "ETHUSDT", "SOLUSDT"]
