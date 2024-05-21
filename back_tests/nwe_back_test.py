from utils.util import get_change


def nwe_entry(current_candle_search, prev_candle_search, prev_prev_candle_search):
    # if long signal return 1
    if nwe_long_entry_condition(current_candle_search, prev_candle_search, prev_prev_candle_search):
        return 1

    # if short signal return -1
    elif nwe_Short_entry_condition(current_candle_search, prev_candle_search, prev_prev_candle_search):
        return -1

    # return 0 if no signal
    return 0


def nwe_Short_entry_condition(enter_candle_search, prev_candle_search, prev_prev_candle_search):
    condition = candle_condition(enter_candle_search, True)
    # condition = (enter_candleSearch["high"] > enter_candleSearch["upper"])
    #
    # # check if high prev candle is greater than high current candle and greater than prev prev candle high and close prev prev candle is lower than prev candle close
    # condition = (condition and
    #              prev_prev_candle_search["high"] > prev_candle_search["high"] > enter_candleSearch["high"])
    return condition


def nwe_long_entry_condition(current_candle_search, prev_candle_search, prev_prev_candle_search):
    # check if low is less than lower
    condition = candle_condition(current_candle_search, False)

    # # check if low prev candle is less than low current candle and less than prev prev candle low and close prev prev candle is upper than prev candle close
    # condition = (condition and
    #              prev_prev_candle_search["low"] < prev_candle_search["low"] < current_candle_search["low"])
    return condition


def candle_condition(candle, upper=True):
    if upper:
        return candle['close'] > candle['upper']

    return candle['close'] < candle['lower']
