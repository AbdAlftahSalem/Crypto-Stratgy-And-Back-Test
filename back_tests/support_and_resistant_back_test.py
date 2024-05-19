def support_and_resistant_entry(candle, last_resistant, pre_candle):
    long_cond = candle['close'] > last_resistant['close'] > candle['low'] and candle[
        'trend_status'] > 0
    short_cond = candle['close'] < last_resistant['close'] < candle['high'] and candle['trend_status'] < 0

    if long_cond:
        return 1

    elif short_cond:
        return -1

    else:
        return 0
