import const_app
from utils.db_service import send_to_database
from utils.util import get_tp_sl_for_long, get_tp_sl_for_short


def nwe_strategy(ticker, interval, candle):
    if candle['nwe_status_signal'] > 0:
        enter_candle, profit, stop = get_tp_sl_for_long(candle, interval, 'nwe',
                                                        const_app.settings['nwe']['config']['using_atr'])

        send_to_database(ticker, candle["close"], interval, profit, stop, True, "nwe")

    if candle['nwe_status_signal'] < 0:
        enter_candle, profit, stop = get_tp_sl_for_short(candle, interval, 'nwe',
                                                         const_app.settings['nwe']['config']['using_atr'])

        send_to_database(ticker, candle["close"], interval, profit, stop, False, "nwe")
