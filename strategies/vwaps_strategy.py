import const_app
from utils.db_service import send_to_database
from utils.util import get_tp_sl_for_long, get_tp_sl_for_short


def vwaps_strategy(ticker, interval, candle):
    if candle['vwaps_signal_status'] > 0:
        enter_candle, profit, stop = get_tp_sl_for_long(candle, interval, 'vwaps',
                                                        const_app.settings['vwaps']['config']['using_atr'])

        send_to_database(ticker, candle["close"], interval, profit, stop, True, "vwaps")

    if candle['vwaps_signal_status'] < 0:
        enter_candle, profit, stop = get_tp_sl_for_short(candle, interval, 'vwaps',
                                                         const_app.settings['vwaps']['config']['using_atr'])

        send_to_database(ticker, candle["close"], interval, profit, stop, False, "vwaps")
