def search(zscore48, zscore200, zscore484, zscore848):
    if zscore200 <= -3 or zscore484 <= -3 or zscore848 <= -3:
        return True
    return False


def vwaps_entry(current_candle):
    long_condition = search(current_candle['zscore_48'], current_candle['zscore_200'], current_candle['zscore_484'],
                            current_candle['zscore_848'])

    # long_condition = long_condition and current_candle['vwap50'] > current_candle['vwap100']

    if long_condition:
        return 1

    return 0
