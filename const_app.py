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

saveDataFolder = "E:\Crypto System\data\\"
"""
The folder path where the retrieved data will be saved.
"""
saveDataFolderIndicator = "E:\Crypto System\dataIndicator\\"
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

numberOfSuccessLongSignal = 0
numberOfSuccessShortSignal = 0

numberOfLoseLongSignal = 0
numberOfLoseShortSignal = 0

summationOfSuccessLongPCT = 0
summationOfSuccessShortPCT = 0

summationOfLoseLongPCT = 0
summationOfLoseShortPCT = 0

strategies = {
    "trend_following": {
        "indicator": {
            "ema": [10, 20, 50, 100, 200],
            "super_trend": [10, 3],
            "candlestick": [3],
        },
        "tp": {
            "short": {
                "tp5m": 2,
                "tp15m": 3,
                "tp30m": 4,
                "tp1h": 5,
                "tp4h": 6,
                "sl": 2,
            },
            "long": {
                "tp5m": 1,
                "tp15m": 1.5,
                "tp30m": 3,
                "tp1h": 3,
                "tp4h": 4,
                "sl": 1.5,
            },
        },
        "config": {
            "long": False,
            "short": True,
        }
    },
    "hit_and_run": {
        "indicator": {
            "sponge_bob": {
                "n1": 10,
                "n2": 21,
                "nsc": 53,
                "nsv": -53,
            },
        },
        "tp": {
            "short": {
                "tp5m": 1,
                "tp15m": 1.5,
                "tp30m": 2,
                "tp1h": 2.5,
                "tp4h": 3,
                "sl": 2,
            },

            "long": {
                "tp5m": 1,
                "tp15m": 1.5,
                "tp30m": 2,
                "tp1h": 2.5,
                "tp4h": 4,
                "sl": 2.5,
            },
        },
        "config": {
            "long": True,
            "short": False,
        },
    },
    "nwe": {
        "indicator": {
            "nadaraya_watson_envelope": [500, 8, 3, "close"],
            "candlestick": [3],
        },
        "tp": {
            "short": {
                "tp5m": 2,
                "tp15m": 3,
                "tp30m": 4,
                "tp1h": 5,
                "tp4h": 6,
                "sl": 2,
            },
            "long": {
                "tp5m": 1,
                "tp15m": 2,
                "tp30m": 3,
                "tp1h": 4,
                "tp4h": 5,
                "sl": 1.5,
            },
        },
        "config": {
            "long": True,
            "short": True,
        }
    },
    "hammer": {
        "tp": {
            "short": {
                "tp5m": 1,
                "tp15m": 1,
                "tp30m": 1,
                "tp1h": 1,
                "tp4h": 1,
                "sl": 1,
            },
            "long": {
                "tp5m": 1,
                "tp15m": 1,
                "tp30m": 1,
                "tp1h": 1,
                "tp4h": 1,
                "sl": 1,
            },
        },
        "config": {
            "long": True,
            "short": True,
        }
    },
}
