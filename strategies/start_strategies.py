from back_tests.set_entery_signals_all_str import set_entry_signals_all_strategies
from candlles_services import multi_candles
from strategies.nwe_strategy import nwe_strategy
from strategies.support_and_resistant_strategy import support_and_resistant_strategy
from strategies.vwaps_strategy import vwaps_strategy
from utils.boost_search import boost_search
from utils.db_service import tickers_path, read_from_database


def start_strategies(ticker, interval="5m", limit=1000):
    df_5m, df_15m, df_30m = multi_candles.get_from_binance(ticker, interval, limit)

    df_5m = set_entry_signals_all_strategies(df_5m)
    df_15m = set_entry_signals_all_strategies(df_15m)
    df_30m = set_entry_signals_all_strategies(df_30m)

    for strategies_status in ['nwe_status_signal', 'support_and_resistant_status_signal', 'vwaps_status_signal']:
        for locale_df in [df_5m, df_15m, df_30m]:
            if locale_df.iloc[-1][strategies_status] != 0:

                if strategies_status.startswith('nwe'):
                    nwe_strategy(ticker, interval, locale_df.iloc[-1])

                elif strategies_status.startswith('support'):
                    support_and_resistant_strategy(ticker, interval, locale_df.iloc[-1])

                elif strategies_status.startswith('vwaps'):
                    vwaps_strategy(ticker, interval, locale_df.iloc[-1])


def start_all_strategies():
    tickers = read_from_database(tickers_path)
    boost_search(start_strategies, tickers, '5m')
