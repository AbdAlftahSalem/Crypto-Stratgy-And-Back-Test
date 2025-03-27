"""

THIS FILE TO TEST AND NEW STRATEGIES OR CHANGE IN ANY PREVIOUS STRATEGY .......,

"""
import pandas

from back_tests.template_back_test import template_bak_test
from utils.util import get_change, check_red_candle
from utils.util_back_test import all_statistic

ticker = 'ETHUSDT'
interval = '15m'
strategy = 'support_and_resistant'
last_ris = None

df = pandas.read_csv(f'E:\Crypto System\dataIndicator\\{ticker}-{interval}-indicators-new7.csv')

support_and_resistant = [0] * 100

for candle_index in range(100, len(df)):
    prev_df = df[candle_index - 100:candle_index]

    # get min low
    min_prev_df = min(prev_df['low'])

    current_candle_search = df.iloc[candle_index]

    if current_candle_search['close'] > min_prev_df > current_candle_search['low'] and not check_red_candle(current_candle_search):
        print(f"Find entry at : {current_candle_search['low']} || Entry Level is : {min_prev_df}")
        support_and_resistant.append(1)
    else:
        support_and_resistant.append(0)

df[f'{strategy}_status_signal'] = support_and_resistant

print(f"2- START BACKTEST FOR {strategy} . {ticker} . {interval}\n\n")
df[f'{strategy}_status_signal'] = support_and_resistant
data = template_bak_test(df, strategy, ticker, interval)
all_statistic(data, interval, ticker, strategy)
