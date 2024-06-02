settings = {
    "get_data": False,
    "apply_strategy": False,
    "showStatistic": True,
    "startBackTest": True,
    "sendBackTestToTele": False,
    "saveBakeTestOutput": True,
    "tickers": ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "ADAUSDT"],
    "intervals": ["5m", "15m", "30m"],
    "saveDataFolder": "E:\Crypto System\data\\new",
    "saveDataFolderIndicator": "E:\Crypto System\dataIndicator\\",
    "ema": ["ema10", "ema20", "ema50", "ema100", "ema200"],
    "vwap": ["vwap21", "vwap50", "vwap100", "vwap200"],
}

strategies = {
    "nwe": {
        "tp": {
            "short": {
                "tp5m": 1,
                "tp15m": 2,
                "tp30m": 3,
                "tp1h": 4,
                "tp4h": 5,
                "sl": 1.5,
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
            'using_atr': False,
        },
        'intervals': ['5m', '15m', '30m']
    },
    "support_and_resistant": {
        "tp": {
            "short": {
                "tp5m": 1,
                "tp15m": 2,
                "tp30m": 3,
                "tp1h": 4,
                "tp4h": 5,
                "sl": 1.5,
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
            "short": False,
            'using_atr': False
        },
        'intervals': ['5m', '15m', '30m']
    },
    'vwaps': {
        "tp": {
            "short": {
                "tp5m": 1,
                "tp15m": 2,
                "tp30m": 3,
                "tp1h": 4,
                "tp4h": 5,
                "sl": 1.5,
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
            "short": False,
            'using_atr': True
        },
        "intervals": ["5m", "15m", "30m"],
    },
}
