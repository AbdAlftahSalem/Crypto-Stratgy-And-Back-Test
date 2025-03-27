import datetime

from back_tests.set_entery_signals_all_str import set_entry_signals_all_strategies
from candlles_services import multi_candles
from strategies.nwe_strategy import nwe_strategy
from utils.boost_search import boost_search_strategies


def start_strategies(ticker, interval="5m", limit=1000):
    # df_5m, df_15m, df_30m = multi_candles.get_from_binance(ticker, interval, limit)
    df_15m = multi_candles.get_from_binance(ticker, interval, limit)

    # df_5m = set_entry_signals_all_strategies(df_5m)
    df_15m = set_entry_signals_all_strategies(df_15m)

    # df_30m = set_entry_signals_all_strategies(df_30m)

    if df_15m is not None and len(df_15m) > 10:
        # for strategies_status in ['nwe_status_signal', 'support_and_resistant_status_signal', 'vwaps_status_signal']:
        for strategies_status in ['nwe_status_signal']:
            # for locale_df in [df_5m, df_15m, df_30m]:
            for locale_df in [df_15m]:
                if locale_df.iloc[-1][strategies_status] != 0:

                    if strategies_status.startswith('nwe'):
                        nwe_strategy(ticker, interval, locale_df.iloc[-1])

                    # elif strategies_status.startswith('support'):
                    #     support_and_resistant_strategy(ticker, interval, locale_df.iloc[-1])
                    #
                    # elif strategies_status.startswith('vwaps'):
                    #     vwaps_strategy(ticker, interval, locale_df.iloc[-1])
    else:
        print(f"None in {ticker}")


def start_all_strategies():
    # tickers = read_from_database(tickers_path)
    tickers = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "KSMUSDT", "SOLUSDT", "AVAXUSDT", "ATOMUSDT", "LINKUSDT", "SANDUSDT",
               "MANAUSDT", "XRPUSDT", "ADAUSDT", "HBARUSDT", "GALAUSDT", "DYDXUSDT", "ARUUSDT", "DOGEUSDT", "TRXUSDT",
               "LTCUSDT", "ZECUSDT", "XLMUSDT", "IOTAUSDT", "ONTUSDT", "THETAUSDT", "SXPUSDT"]

    while True:
        if datetime.datetime.now().minute in [0, 15, 30, 45]:
            boost_search_strategies(start_strategies, tickers, '15m')
