def vwaps_entry(current_candle, last_ris):
    long_condition = current_candle['close'] > last_ris['close'] > current_candle['low'] and current_candle[
        'trend_status'] > 0
    long_condition = long_condition and current_candle['close'] > current_candle['vwap50'] and current_candle['close'] > \
                     current_candle['vwap21'] and current_candle['low']

    if long_condition:
        return 1

    return 0
