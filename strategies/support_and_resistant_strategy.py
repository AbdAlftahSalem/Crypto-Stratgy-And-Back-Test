import const_app
from utils.db_service import send_to_database
from utils.util import get_tp_sl_for_long, get_tp_sl_for_short


def support_and_resistant_strategy(ticker, interval, candle):
    if candle['support_and_resistant_signal_status'] > 0:
        enter_candle, profit, stop = get_tp_sl_for_long(candle, interval, 'support_and_resistant',
                                                        const_app.settings['support_and_resistant']['config'][
                                                            'using_atr'])

        send_to_database(ticker, candle["close"], interval, profit, stop, True, "support_and_resistant")

    if candle['support_and_resistant_signal_status'] < 0:
        enter_candle, profit, stop = get_tp_sl_for_short(candle, interval, 'support_and_resistant',
                                                         const_app.settings['support_and_resistant']['config'][
                                                             'using_atr'])

        send_to_database(ticker, candle["close"], interval, profit, stop, False, "support_and_resistant")
