import pandas
import pandas_ta

from utils.util import get_change, check_red_candle

ticker = 'SOLUSDT'
interval = '30m'
strategy = 'vwaps'
main_df = pandas.read_csv(f'E:\Crypto System\dataIndicator\\{ticker}-{interval}-indicators-new7.csv')
main_df['zscore_48'] = pandas_ta.zscore(main_df['close'], 48)
main_df['zscore_200'] = pandas_ta.zscore(main_df['close'], 200)
main_df['zscore_484'] = pandas_ta.zscore(main_df['close'], 484)
main_df['zscore_848'] = pandas_ta.zscore(main_df['close'], 848)

signals_df = pandas.read_csv(f"../database/backtest/{ticker}-{interval}-{strategy}.csv")
data_list = []

search_win_signal = False
search_in_long_only = True


def get_full_data():
    last_index = 0
    for signal in range(len(signals_df)):
        search_condition = signals_df.iloc[signal]['status'] == ("tp" if search_win_signal else 'sl')
        search_condition = search_condition and str(signals_df.iloc[signal]['strategy_long']) == str(
            search_in_long_only)
        if search_condition:
            for main in range(last_index, len(main_df)):
                if main_df.iloc[main]['date'] == signals_df.iloc[signal]['entry_date']:
                    data_list.append(main_df.iloc[main])
                    last_index = main
                    break


def get_statistic():
    sum_cci = 0
    sum_mfi = 0
    sum_rsi = 0

    max_cci = 0
    max_mfi = 0
    max_rsi = 0

    min_cci = 0
    min_mfi = 0
    min_rsi = 0

    sum_change_vwap21 = 0
    sum_change_vwap50 = 0
    sum_change_vwap100 = 0
    sum_change_vwap200 = 0

    max_change_vwap21 = 0
    max_change_vwap50 = 0
    max_change_vwap100 = 0
    max_change_vwap200 = 0

    min_change_vwap21 = 1000
    min_change_vwap50 = 1000
    min_change_vwap100 = 1000
    min_change_vwap200 = 1000

    sum_change_ema10 = 0
    sum_change_ema20 = 0
    sum_change_ema50 = 0
    sum_change_ema100 = 0
    sum_change_ema200 = 0

    max_change_ema10 = 0
    max_change_ema20 = 0
    max_change_ema50 = 0
    max_change_ema100 = 0
    max_change_ema200 = 0

    min_change_ema10 = 10000
    min_change_ema20 = 10000
    min_change_ema50 = 10000
    min_change_ema100 = 10000
    min_change_ema200 = 10000

    number_of_super_trend_above = 0
    number_of_super_trend_below = 0

    number_of_green_candle_entry = 0
    number_of_red_candle_entry = 0

    sponge_bob_long = 0

    max_zscore48 = 0
    min_zscore48 = 0
    sum_zscore48 = 0

    max_zscore200 = 0
    min_zscore200 = 0
    sum_zscore200 = 0

    max_zscore484 = 0
    min_zscore484 = 0
    sum_zscore484 = 0

    max_zscore848 = 0
    min_zscore848 = 0
    sum_zscore848 = 0

    if len(data_list) > 0:
        for i in data_list:
            #######################################################
            sum_cci += i['cci']
            sum_mfi += i['mfi']
            sum_rsi += i['rsi']

            max_cci, min_cci = max_and_min(i['cci'], max_cci, min_cci)
            #######################################################

            max_mfi, min_mfi = max_and_min(i['mfi'], max_mfi, min_mfi)
            #######################################################

            max_rsi, min_rsi = max_and_min(i['rsi'], max_rsi, min_rsi)
            #######################################################
            change_vwap21 = get_change(i['close'], i['vwap21'])
            change_vwap50 = get_change(i['close'], i['vwap50'])
            change_vwap100 = get_change(i['close'], i['vwap100'])
            change_vwap200 = get_change(i['close'], i['vwap200'])

            sum_change_vwap21 += change_vwap21
            sum_change_vwap50 += change_vwap50
            sum_change_vwap100 += change_vwap100
            sum_change_vwap200 += change_vwap200

            max_change_vwap21, min_change_vwap21 = max_and_min(change_vwap21, max_change_vwap21, min_change_vwap21)
            max_change_vwap50, min_change_vwap50 = max_and_min(change_vwap50, max_change_vwap50, min_change_vwap50)
            max_change_vwap100, min_change_vwap100 = max_and_min(change_vwap100, max_change_vwap100, min_change_vwap100)
            max_change_vwap200, min_change_vwap200 = max_and_min(change_vwap200, max_change_vwap200, min_change_vwap200)

            ##################################################3#######################
            change_ema10 = get_change(i['close'], i['ema10'])
            change_ema20 = get_change(i['close'], i['ema20'])
            change_ema50 = get_change(i['close'], i['ema50'])
            change_ema100 = get_change(i['close'], i['ema100'])
            change_ema200 = get_change(i['close'], i['ema200'])

            max_change_ema10, min_change_ema10 = max_and_min(change_ema10, max_change_ema10, min_change_ema10)
            max_change_ema20, min_change_ema20 = max_and_min(change_ema20, max_change_ema20, min_change_ema20)
            max_change_ema50, min_change_ema50 = max_and_min(change_ema50, max_change_ema50, min_change_ema50)
            max_change_ema100, min_change_ema100 = max_and_min(change_ema100, max_change_ema100, min_change_ema100)
            max_change_ema200, min_change_ema200 = max_and_min(change_ema200, max_change_ema200, min_change_ema200)

            sum_change_ema10 += change_ema10
            sum_change_ema20 += change_ema20
            sum_change_ema50 += change_ema50
            sum_change_ema100 += change_ema100
            sum_change_ema200 += change_ema200

            sum_zscore48 = i['zscore_48']
            max_zscore48, min_zscore48 = max_and_min(i['zscore_48'], max_zscore48, min_zscore48)

            sum_zscore200 = i['zscore_200']
            max_zscore200, min_zscore200 = max_and_min(i['zscore_200'], max_zscore200, min_zscore200)

            sum_zscore484 = i['zscore_484']
            max_zscore484, min_zscore484 = max_and_min(i['zscore_484'], max_zscore484, min_zscore484)

            sum_zscore848 = i['zscore_848']
            max_zscore848, min_zscore848 = max_and_min(i['zscore_848'], max_zscore848, min_zscore848)

            if i['superTrend'] > i['close']:
                number_of_super_trend_above += 1

            else:
                number_of_super_trend_below += 1

            if check_red_candle(i):
                number_of_red_candle_entry += 1
            else:
                number_of_green_candle_entry += 1

            sponge_bob_long += i['sponge_bob_long']

        message = f'⚡⚡ {ticker} || {interval} || {"LONG" if search_in_long_only else "SHORT"} || {"WIN SIGNALS" if search_win_signal else "LOSE SIGNALS"} ⚡⚡\n\n'
        message += f"AVG CCI : {sum_cci / len(data_list)}\n"
        message += f"MAX CCI : {max_cci}\n"
        message += f"MIN CCI : {max_cci}\n\n"

        message += f"AVG MFI : {sum_mfi / len(data_list)}\n"
        message += f"MAX MFI : {max_mfi}\n"
        message += f"MIN MFI : {min_mfi}\n\n"

        message += f"AVG RSI : {sum_rsi / len(data_list)}\n"
        message += f"MAX RSI : {max_rsi / len(data_list)}\n"
        message += f"MIN RSI : {min_rsi / len(data_list)}\n\n"

        message += f"AVG change vwap21 : {sum_change_vwap21 / len(data_list)}\n"
        message += f"MAX change vwap21 : {max_change_vwap21}\n"
        message += f"MIN change vwap21 : {min_change_vwap21}\n\n"

        message += f"AVG change vwap50 : {sum_change_vwap50 / len(data_list)}\n"
        message += f"MAX change vwap50 : {max_change_vwap50}\n"
        message += f"MIN change vwap50 : {min_change_vwap50}\n\n"

        message += f"AVG change vwap100 : {sum_change_vwap100 / len(data_list)}\n"
        message += f"MAX change vwap100 : {max_change_vwap100}\n"
        message += f"MIN change vwap100 : {min_change_vwap100}\n\n"

        message += f"AVG change vwap200 : {sum_change_vwap200 / len(data_list)}\n\n"
        message += f"MAX change vwap200 : {max_change_vwap200}\n"
        message += f"MIN change vwap200 : {min_change_vwap200}\n\n"

        message += f"AVG change ema10 : {sum_change_ema10 / len(data_list)}\n"
        message += f"MAX change ema10 : {max_change_ema10}\n"
        message += f"MIN change ema10 : {min_change_ema10}\n\n"

        message += f"AVG change ema20 : {sum_change_ema20 / len(data_list)}\n"
        message += f"MAX change ema20 : {max_change_ema20}\n"
        message += f"MIN change ema20 : {min_change_ema20}\n\n"

        message += f"AVG change ema50 : {sum_change_ema50 / len(data_list)}\n"
        message += f"MAX change ema50 : {max_change_ema50}\n"
        message += f"MIN change ema50 : {min_change_ema50}\n\n"

        message += f"AVG change ema100 : {sum_change_ema100 / len(data_list)}\n"
        message += f"MAX change ema100 : {max_change_ema100}\n"
        message += f"MIN change ema100 : {min_change_ema100}\n\n"

        message += f"AVG change ema200 : {sum_change_ema200 / len(data_list)}\n"
        message += f"MAX change ema200 : {max_change_ema200}\n"
        message += f"MIN change ema200 : {min_change_ema200}\n\n"

        message += f"Number of signal above super trend : {number_of_super_trend_above}\n"
        message += f"number_of_super_trend_below super trend : {number_of_super_trend_below}\n\n"

        message += f"Number of green candle entry : {number_of_green_candle_entry}\n"
        message += f"Number of red candle entry : {number_of_red_candle_entry}\n\n"

        message += f"Sponge bob long : {sponge_bob_long / len(data_list)}\n\n"

        message += f"AVG change zscore48 : {sum_zscore48 / len(data_list)}\n"
        message += f"MAX change zscore48 : {max_zscore48}\n"
        message += f"MIN change zscore48 : {min_zscore48}\n\n"

        message += f"AVG change zscore200 : {sum_zscore200 / len(data_list)}\n"
        message += f"MAX change zscore200 : {max_zscore200}\n"
        message += f"MIN change zscore200 : {min_zscore200}\n\n"

        message += f"AVG change zscore484 : {sum_zscore484 / len(data_list)}\n"
        message += f"MAX change zscore484 : {max_zscore484}\n"
        message += f"MIN change zscore484 : {min_zscore484}\n\n"

        message += f"AVG change zscore848 : {sum_zscore848 / len(data_list)}\n"
        message += f"MAX change zscore848 : {max_zscore848}\n"
        message += f"MIN change zscore848 : {min_zscore848}\n\n"

        print(message)
    else:
        print("NO DATA FOUND .....")


def max_and_min(main_value, max_value, min_value):
    if main_value > max_value:
        max_value = main_value
    if main_value < min_value:
        min_value = main_value

    return max_value, min_value


get_full_data()
get_statistic()

"""
"""
