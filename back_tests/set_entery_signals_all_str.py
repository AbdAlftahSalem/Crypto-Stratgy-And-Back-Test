import pandas as pd
import pandas_ta as pd_ta

from analysis.support_and_resistant import get_support_and_resistant
from back_tests.nwe_back_test import nwe_entry
from back_tests.support_and_resistant_back_test import support_and_resistant_entry
from back_tests.vwap_back_test import vwaps_entry


def set_entry_signals_all_strategies(df: pd.DataFrame):
    # setup signal for strategies
    support_and_resistant = [0] * 3
    nwe_status_signal = [0] * 3
    vwap_status_signal = [0] * 3

    last_ris = None

    #  calc support_and_resistant
    df['support_and_resistant'] = get_support_and_resistant(df, 8, 8)

    for candle in range(len(df) - 3):
        current_candle_search = df.iloc[candle]
        prev_candle_search = df.iloc[candle - 1]
        prev_prev_candle_search = df.iloc[candle - 2]

        nwe_status_signal.append(nwe_entry(current_candle_search, prev_candle_search, prev_prev_candle_search))

        if current_candle_search['support_and_resistant'] < 0:
            last_ris = current_candle_search

        if last_ris is not None:
            vwap_status_signal.append(vwaps_entry(current_candle_search, last_ris))
            support_and_resistant.append(
                support_and_resistant_entry(current_candle_search, last_ris, prev_candle_search))
        else:
            vwap_status_signal.append(0)
            support_and_resistant.append(0)

    df['support_and_resistant_status_signal'] = support_and_resistant
    df['vwaps_status_signal'] = vwap_status_signal
    df['nwe_status_signal'] = nwe_status_signal
    df['atr'] = pd_ta.atr(df['high'], df['low'], df['close'])

    return df
