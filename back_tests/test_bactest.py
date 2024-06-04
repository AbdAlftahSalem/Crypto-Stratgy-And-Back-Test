"""

THIS FILE TO TEST AND NEW STRATEGIES OR CHANGE IN ANY PREVIOUS STRATEGY .......,

"""
import pandas
import pandas_ta

from back_tests.nwe_back_test import nwe_entry
from back_tests.template_back_test import template_bak_test
from back_tests.vwap_back_test import vwaps_entry
from utils.util_back_test import all_statistic

ticker = 'SOLUSDT'
interval = '30m'
strategy = 'vwaps'
last_ris = None
support_and_resistant_signals = [0] * 3

df = pandas.read_csv(f'E:\Crypto System\dataIndicator\\{ticker}-{interval}-indicators-new7.csv')
df['zscore_48'] = pandas_ta.zscore(df['close'], 48)
df['zscore_200'] = pandas_ta.zscore(df['close'], 200)
df['zscore_484'] = pandas_ta.zscore(df['close'], 484)
df['zscore_848'] = pandas_ta.zscore(df['close'], 848)

print("1- FINISH READ DF")

for x in range(len(df) - 3):
    current_candle_search = df.iloc[x]
    prev_candle_search = df.iloc[x - 1]
    prev_prev_candle_search = df.iloc[x - 2]
    pre_prev_prev_candle_search = df.iloc[x - 3]

    support_and_resistant_signals.append(vwaps_entry(current_candle_search))

print(f"2- START BACKTEST FOR {strategy} . {ticker} . {interval}\n\n")
df[f'{strategy}_status_signal'] = support_and_resistant_signals
data = template_bak_test(df, strategy, ticker, interval)
all_statistic(data, interval, ticker, strategy)
