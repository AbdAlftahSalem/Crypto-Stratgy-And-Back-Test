"""

THIS FILE TO TEST AND NEW STRATEGIES OR CHANGE IN ANY PREVIOUS STRATEGY .......,

"""
import pandas

from back_tests.template_back_test import template_bak_test
from back_tests.vwap_back_test import vwaps_entry
from utils.util_back_test import all_statistic

ticker = 'SOLUSDT'
interval = '30m'
strategy = 'vwaps'
last_ris = None

df = pandas.read_csv(f'E:\Crypto System\dataIndicator\\{ticker}-{interval}-indicators-new7.csv')

support_and_resistant = [0] * 3

for candle in range(len(df) - 3):
    current_candle_search = df.iloc[candle]
    prev_candle_search = df.iloc[candle - 1]
    prev_prev_candle_search = df.iloc[candle - 2]

    if current_candle_search['support_and_resistant'] < 0:
        last_ris = current_candle_search

    if last_ris is not None:
        support_and_resistant.append(vwaps_entry(current_candle_search, last_ris))
    else:
        support_and_resistant.append(0)

df[f'{strategy}_status_signal'] = support_and_resistant

print(f"2- START BACKTEST FOR {strategy} . {ticker} . {interval}\n\n")
df[f'{strategy}_status_signal'] = support_and_resistant
data = template_bak_test(df, strategy, ticker, interval)
all_statistic(data, interval, ticker, strategy)
