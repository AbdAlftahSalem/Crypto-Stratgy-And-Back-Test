from tradingview_ta import *


def get_from_treading_view(tickers, interval):
    treading_view_data = []

    data = get_multiple_analysis(
        screener="crypto", interval=interval, symbols=tickers)
    for tickers in data:
        try:
            indicator = data[tickers].indicators
            tickers = tickers.replace("BINANCE:", "")
            treading_view_data.append({"ticker": tickers, "indicator": indicator})

        except:
            pass

    return treading_view_data
