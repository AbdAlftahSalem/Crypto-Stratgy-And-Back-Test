from datetime import datetime

import pandas as pd

import const_app
from utils import util
from utils.db_service import back_test_path


def get_profit(strategy: str, interval: str, long: bool):
    """
    Get the profit percentage based on the given time interval and strategy.

    Returns:
        The profit percentage.

    """
    if interval == "5m":
        return const_app.strategies[strategy]["tp"]["long" if long else "short"]["tp5m"]

    elif interval == "15m":
        return const_app.strategies[strategy]["tp"]["long" if long else "short"]["tp15m"]

    elif interval == "30m":
        return const_app.strategies[strategy]["tp"]["long" if long else "short"]["tp30m"]

    elif interval == "1h":
        return const_app.strategies[strategy]["tp"]["long" if long else "short"]["tp1h"]

    elif interval == "4h":
        return const_app.strategies[strategy]["tp"]["long" if long else "short"]["tp4h"]


def get_stop_lose(strategy: str, long: bool):
    """
    Get the stop lose percentage based on the given interval and strategy.

    Returns:
        The stop lose percentage.

    """
    return const_app.strategies[strategy]["tp"]["long" if long else "short"]["sl"]


def get_trade_data(strategy, long, enter_candle, exit_candle, profit, stop, status, interval, message=''):
    """
    Get the trade data for a specific trade.

    Args:
        enter_candle: The enter candle data.
        exit_candle: The exit candle data.
        profit: The profit target.
        stop: The stop loss target.
        status: The trade status.
        interval: The time interval.
        strategy: The strategy name.
        long: The long status.
        message: The message add to data

    """

    if status == 'tp':
        change = util.get_change(profit, enter_candle['close'])
    else:
        change = -util.get_change(stop, enter_candle['close'])

    return {
        "strategy": strategy,
        "entry_date": enter_candle["date"],
        "out_date": exit_candle["date"],
        "enter_price": enter_candle["close"],
        "tp": profit,
        "sl": stop,
        'interval': interval,
        "status": status,
        "change": change,
        'strategy_long': long,
        'message': message
    }


def get_detail_df_signals(data):
    lose_num = 0
    win_num = 0
    all_change_win = 0
    all_change_lose = 0
    summ_diff_date = 0
    max_change_tp = 0
    max_change_sl = 0

    for i in data:
        entry_date = datetime.strptime(i["entry_date"], '%Y-%m-%d %H:%M:%S')
        out_date = datetime.strptime(i["out_date"], '%Y-%m-%d %H:%M:%S')

        summ_diff_date += (out_date - entry_date).total_seconds() / 3600

        if i["status"] == "tp":
            win_num += 1
            all_change_win += i["change"]
            if i["change"] >= max_change_tp:
                max_change_tp = i['change']

        else:
            lose_num += 1
            all_change_lose += i["change"]
            # wallet -= ((i["change"] / 100) * wallet)
            if max_change_sl > i["change"]:
                max_change_sl = i['change']

    pct_success = f"{round((win_num / (win_num + lose_num)) * 100, 2)}%"
    avg_waiting_time = summ_diff_date / len(data)

    return win_num, lose_num, round(all_change_win, 2), round(all_change_lose, 2), 100, pct_success, round(
        avg_waiting_time, 2), max_change_tp, max_change_sl


def all_statistic(data, interval, ticker, prefixMessage):
    if const_app.settings['saveBakeTestOutput']:
        df = pd.DataFrame(data["data"])
        df.to_csv(back_test_path + f"{ticker}-{interval}-{prefixMessage}.csv")
    # add_to_database(back_test_path + f"{ticker}-{interval}-{prefixMessage}.csv", pd.DataFrame(data["data"]))

    long_data = []
    short_data = []
    for i in data['data']:
        if i["strategy_long"]:
            long_data.append(i)
        else:
            short_data.append(i)

    # Calculate statistics for short trades

    if len(short_data) > 0:
        win_numShort, lose_numShort, change_winShort, change_loseShort, startWalletShort, pct_successShort, avgWaitingShort, max_change_tp_short, max_change_sl_short = get_detail_df_signals(
            short_data)
        message_short = f"{hide_strategy_name(prefixMessage)} || SHORT || Ticker : {ticker}\nInterval : {interval}\nWin number : {win_numShort}\nLose number : {lose_numShort}\nChange win : +{change_winShort} %\nChange lose : -{-change_loseShort} %\nSum Change : {round(change_winShort + change_loseShort, 2)} %\nMax Change win : {max_change_tp_short} %\nMax change lose : {max_change_sl_short} %\nPCT Success : {pct_successShort}\nAVG waiting time : {round(avgWaitingShort * 60, 2)} M ||| {avgWaitingShort} H ||| {round(avgWaitingShort / 24, 2)} D\n\n"
        print(message_short)

    if len(long_data) > 0:
        win_num_long, lose_num_long, change_win_long, change_lose_long, startWallet_long, pct_success_long, avgWaiting_long, max_change_tp_long, max_change_sl_long = get_detail_df_signals(
            long_data)
        message_long = f"{hide_strategy_name(prefixMessage)} || LONG || Ticker : {ticker}\nInterval : {interval}\nWin number : {win_num_long}\nLose number : {lose_num_long}\nChange win : +{change_win_long} %\nChange lose : -{-change_lose_long} %\nSum Change : {round(change_win_long + change_lose_long, 2)} %\nMax Change win : {max_change_tp_long} %\nMax change lose : {max_change_sl_long} %\nPCT Success : {pct_success_long}\nAVG waiting time : {round(avgWaiting_long * 60, 2)} M ||| {avgWaiting_long} H ||| {round(avgWaiting_long / 24, 2)} D\n\n"
        print(message_long)
    # if const_app.settings['sendBackTestToTele']:
    #     sendBackTestToTelegram(message_short)
    #     sendBackTestToTelegram(message_long)


def get_statistic_for_strategy(strategy_name):
    all_win_signals = 0
    all_lose_signals = 0

    all_win_signals_short = 0
    all_lose_signals_short = 0

    all_win_signals_long = 0
    all_lose_signals_long = 0

    change_win_long = 0
    change_lose_long = 0

    change_win_short = 0
    change_lose_short = 0

    long_strategy_condition = const_app.strategies[strategy_name]['config']['long']
    short_strategy_condition = const_app.strategies[strategy_name]['config']['short']

    for ticker in const_app.settings['tickers']:
        for interval in const_app.settings['intervals']:
            try:
                df = pd.read_csv(f"database/backtest/{ticker}-{interval}-{strategy_name}.csv")
                for i in range(len(df)):
                    if df.iloc[i]['status'] == 'tp' and df.iloc[i]['strategy_long'] and long_strategy_condition:
                        all_win_signals += 1
                        all_win_signals_long += 1
                        change_win_long += df.iloc[i]['change']

                    elif df.iloc[i]['status'] == 'sl' and df.iloc[i]['strategy_long'] and long_strategy_condition:
                        all_lose_signals += 1
                        all_lose_signals_long += 1
                        change_lose_long += df.iloc[i]['change']

                    if df.iloc[i]['status'] == 'tp' and not df.iloc[i]['strategy_long'] and short_strategy_condition:
                        all_win_signals += 1
                        all_win_signals_short += 1
                        change_win_short += df.iloc[i]['change']

                    elif df.iloc[i]['status'] == 'sl' and not df.iloc[i]['strategy_long'] and short_strategy_condition:
                        all_lose_signals += 1
                        all_lose_signals_short += 1
                        change_lose_short += df.iloc[i]['change']

            except:
                pass

    all_pct_success = round((all_win_signals / (all_win_signals + all_lose_signals)) * 100, 2)

    if short_strategy_condition:
        short_pct_success = round((all_win_signals_short / (all_win_signals_short + all_lose_signals_short)) * 100, 2)

    if long_strategy_condition:
        long_pct_success = round((all_win_signals_long / (all_win_signals_long + all_lose_signals_long)) * 100, 2)

    message = f"***************************  FINAL STATISTIC FOR {hide_strategy_name(strategy_name)}  ***************************\n"
    message += f"TICKERS                              : {const_app.settings['tickers']}\n"
    message += f"INTERVALS                            : {const_app.settings['intervals']}\n\n"

    message += f"Number of all signals                : {all_lose_signals + all_win_signals}\n\n"
    if long_strategy_condition:
        message += f"Number of all long signals        : {all_lose_signals_long + all_win_signals_long}\n"
        message += f"Number of all win long signals    : {all_win_signals_long}\n"
        message += f"Number of all lose long signals   : {all_lose_signals_long}\n\n"

        message += f"Win change for long signals       : {round(change_win_long, 2)} %\n"
        message += f"Lose change for long signals      : {round(change_lose_long, 2)} %\n"

    if short_strategy_condition:
        message += f"Number of all short signals       : {all_lose_signals_short + all_win_signals_short}\n"
        message += f"Number of all win short signals   : {all_win_signals_short}\n"
        message += f"Number of all lose short signals  : {all_lose_signals_short}\n\n"

        message += f"Win change for short signals      : {round(change_win_short, 2)} %\n"
        message += f"Lose change for short signals     : {round(change_lose_short, 2)} %\n\n"

    message += f"PCT Success for {hide_strategy_name(strategy_name)}      : {all_pct_success} %\n"

    if long_strategy_condition:
        message += f"PCT Success for long signals      : {long_pct_success} %\n"

    if short_strategy_condition:
        message += f"PCT Success for short signals     : {short_pct_success} %\n"
    message += "********************************************************************************\n\n"

    print(message)


def hide_strategy_name(strategy_name: str):
    strategy_name_list = strategy_name.split("_")
    local_strategy = ''
    if len(strategy_name_list) > 1:
        for i in strategy_name_list:
            local_strategy += i[0]
        return local_strategy.upper()

    else:
        return (strategy_name[0] + strategy_name[-1]).upper()
