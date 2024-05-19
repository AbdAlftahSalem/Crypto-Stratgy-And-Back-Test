import math

from utils import util_back_test


def divide_df(df) -> list:
    """
    Divide a Data interval into smaller chunks of size 500.

    Args:
        df: The Data interval to be divided.

    Returns:
        A list of smaller Data intervals.

    """
    df_list = []
    for i in range(math.ceil(len(df) / 500)):
        df_list.append((df[i * 500:(i + 1) * 500]).reset_index())

    return df_list


def get_index(df, title, value):
    """
    Get the index of the first occurrence of a specific value in a Data interval column.

    Args:
        df: The Data interval to search in.
        title: The column name to search for the value.
        value: The value to find.

    Returns:
        The index of the first occurrence of the value in the column, or 'no match' if not found.

    """
    return next(iter(df[df[title] == value].index), 'no match')


def check_red_candle(candle):
    """
    Check if a candle represents a red candle (open > close).

    Args:
        candle: A dictionary representing the candle with 'open' and 'close' values.

    Returns:
        True if the candle is red, False otherwise.

    """
    if candle['open'] > candle["close"]:
        return True
    else:
        return False


def get_change(current, previous):
    """
    Calculate the percentage change between two values.

    Args:
        current: The current value.
        previous: The previous value.

    Returns:
        The percentage change rounded to 2 decimal places.

    """
    if current == previous:
        return 0
    try:
        return abs(round(((current - previous) / previous) * 100.0, 2))
    except ZeroDivisionError:
        return 0


def get_num_by_change(enterPrice, pct):
    """
    Calculate the resulting number by applying a percentage change to a given number.

    Args:
        enterPrice: The original number.
        pct: The percentage change.

    Returns:
        The resulting number after applying the percentage change.

    """
    return round(((enterPrice * pct) + (100 * enterPrice)) / 100, 5)


def search_in_array(array, value):
    """
    Check if a value is present in an array.

    Args:
        array: The array to search in.
        value: The value to search for.

    Returns:
        True if the value is found, False otherwise.

    """
    found = False
    for i in array:
        if i == value:
            found = True
            break
        else:
            found = False
    return found


def get_tp_sl_for_short(enter_candle, interval, strategy_name, using_atr_to_stop):
    atr = enter_candle['atr']
    if using_atr_to_stop:
        #  CALCULATE STOP AND PROFIT USING ATR /// 1.5:1
        stop = enter_candle['close'] + (atr * 1.5)
        change_stop = get_change(stop, enter_candle['close'])
        profit = get_num_by_change(enter_candle['close'], change_stop * -1.5)
    else:
        profit_pct = util_back_test.get_profit(strategy_name, interval, False)
        profit = get_num_by_change(enter_candle["close"], profit_pct * -1)
        stop = get_num_by_change(enter_candle["close"],
                                 (profit_pct / util_back_test.get_stop_lose(strategy_name, False)))
    return enter_candle, profit, stop


def get_tp_sl_for_long(enter_candle, interval, strategy_name, using_atr_to_stop):
    atr = enter_candle['atr']
    if using_atr_to_stop:
        #  CALCULATE STOP AND PROFIT USING ATR /// 1.5:1
        stop = enter_candle['close'] - (atr * 1.5)
        change_stop = get_change(stop, enter_candle['close'])
        profit = get_num_by_change(enter_candle['close'], change_stop * 1.5)
    else:
        profit_pct = util_back_test.get_profit(strategy_name, interval, True)
        profit = get_num_by_change(enter_candle["close"], profit_pct)
        stop = get_num_by_change(enter_candle["close"],
                                 ((profit_pct / util_back_test.get_stop_lose(strategy_name, True)) * -1))
    return enter_candle, profit, stop
