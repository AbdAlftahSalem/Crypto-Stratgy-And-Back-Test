"""

THIS FILE TO TEST AND NEW STRATEGIES OR CHANGE IN ANY PREVIOUS STRATEGY .......,

"""
import pandas

from back_tests.nwe_back_test import nwe_entry
from back_tests.template_back_test import template_bak_test
from utils.util_back_test import all_statistic

ticker = 'SOLUSDT'
interval = '30m'
strategy = 'nwe'
last_ris = None
support_and_resistant_signals = [0] * 3

df = pandas.read_csv(f'E:\Crypto System\dataIndicator\\{ticker}-{interval}-indicators-new7.csv')

print("FINISH STAGE 1")

for x in range(len(df) - 3):
    current_candle_search = df.iloc[x]
    prev_candle_search = df.iloc[x - 1]
    prev_prev_candle_search = df.iloc[x - 2]
    pre_prev_prev_candle_search = df.iloc[x - 3]

    support_and_resistant_signals.append(nwe_entry(current_candle_search, prev_candle_search, prev_candle_search))

print("START")
df[f'{strategy}_status_signal'] = support_and_resistant_signals
print(df[f'{strategy}_status_signal'])
data = template_bak_test(df, strategy, ticker, interval)
all_statistic(data, interval, ticker, strategy)
