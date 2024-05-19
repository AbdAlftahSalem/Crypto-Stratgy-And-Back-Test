import json
from datetime import datetime

from utils.send_to_tele import setup_messages, send_signals_to_telegram

back_test_path = 'database/backtest/'
open_signal_path = 'database/open_signals.json'
tickers_path = 'database/tickers.json'


def send_to_database(ticker, enter_price, interval, profit, stop, isLong, strategy_name):
    message = setup_messages(ticker, enter_price, profit, stop, interval, "Long" if isLong else "Short")

    send_signals_to_telegram(message)

    save_signal(ticker, enter_price, profit, stop, interval, strategy_name, "Long" if isLong else "Short")


def create_back_test_model(ticker, interval, profit_num, lose_um, strategy_name, total_lose_pct, total_win_pct,
                           total_change,
                           pct_success, strategy_type):
    return {
        "ticker": ticker,
        "interval": interval,
        "profit_num": profit_num,
        "lose_num": lose_um,
        "strategy_name": strategy_name,
        "total_lose_pct": total_lose_pct,
        "total_win_pct": total_win_pct,
        "total_change": total_change,
        "pct_success": pct_success,
        "start_date": "",
        "end_date": "",
        "strategy_type": strategy_type
    }


def save_signal(ticker, enter_price, take_profit, stop_loss, interval, strategy_name, signal_type):
    data = {
        "ticker": ticker,
        "enter_price": enter_price,
        "take_profit": take_profit,
        "stop_loss": stop_loss,
        "interval": interval,
        "enter_date": str(datetime.now().year) + " - " + str(datetime.now().month) + " - " + str(
            datetime.now().day) + " // " + str(datetime.now().hour) + " - " + str(datetime.now().minute),
        "strategy_name": strategy_name,
        "signal_type": signal_type,
        "status": "open"
    }
    add_to_database(open_signal_path, data)
    # requests.post(createSignalUrl, data)


def add_to_database(file_name, data):
    print("You need setup database .........")


def read_from_database(file_name):
    print("You need setup database .........")
