import pandas as pd

import const_app
from back_tests.show_back_test_output import thread_output
from utils.util import get_tp_sl_for_long, get_tp_sl_for_short
from utils.util_back_test import get_trade_data, hide_strategy_name


def template_bak_test(df: pd.DataFrame, strategy_name, ticker: str, interval: str = '30m'):
    search_profit = False
    search_long_profit = False
    search_short_profit = False
    profit = 0
    stop = 0
    enter_candle = df.iloc[0]
    output = {"ticker": ticker, "interval": interval, "profit_num": 0, "lose_num": 0, "strategy_name": strategy_name,
              "start_date": df.iloc[0]["date"], "end_date": df.iloc[-1]["date"], "data": []}

    using_atr_to_stop = const_app.strategies[strategy_name]['config']['using_atr']
    for i in range(len(df)):

        long_condition = df.iloc[i][f'{strategy_name}_status_signal'] > 0 and not search_profit and \
                         const_app.strategies[strategy_name]['config']['long']
        short_condition = df.iloc[i][f'{strategy_name}_status_signal'] < 0 and not search_profit and \
                          const_app.strategies[strategy_name]['config']['short']

        if long_condition:
            enter_candle, profit, stop = get_tp_sl_for_long(df.iloc[i], interval, strategy_name, using_atr_to_stop)

            search_profit = True
            search_long_profit = True

            continue

        elif short_condition:
            enter_candle, profit, stop = get_tp_sl_for_short(df.iloc[i], interval, strategy_name, using_atr_to_stop)

            search_profit = True
            search_short_profit = True

            continue

        if search_profit:

            if search_short_profit:
                if df.iloc[i]["low"] <= profit:
                    output["data"].append(
                        get_trade_data(strategy_name, False, enter_candle, df.iloc[i], profit, stop, "tp", interval))
                    output["profit_num"] += 1
                    search_profit = False
                    search_short_profit = False
                    i += 1

                    continue

                elif df.iloc[i]["close"] >= stop:
                    output["data"].append(
                        get_trade_data(strategy_name, False, enter_candle, df.iloc[i], profit, stop, "sl",
                                       interval))
                    output["lose_num"] += 1
                    search_profit = False
                    search_short_profit = False

                    i += 1
                    continue

            if search_long_profit:
                if df.iloc[i]["high"] >= profit:
                    output["data"].append(
                        get_trade_data(strategy_name, True, enter_candle, df.iloc[i], profit, stop, "tp", interval)
                    )
                    output["profit_num"] += 1
                    search_profit = False
                    search_long_profit = False
                    i += 1
                    continue


                elif df.iloc[i]["close"] <= stop:
                    output["data"].append(
                        get_trade_data(strategy_name, True, enter_candle, df.iloc[i], profit, stop, "sl", interval)
                    )
                    output["lose_num"] += 1
                    search_profit = False
                    search_long_profit = False
                    i += 1
                    continue

    return output


def show_back_test_data(strategy_name: str):
    print(
        f"↗️ Start {hide_strategy_name(strategy_name)} strategy for tickers : {const_app.settings['tickers']}")
    thread_output(strategy_name)
