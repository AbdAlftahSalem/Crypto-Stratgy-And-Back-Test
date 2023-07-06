import math


def divideDf(df) -> list:
    df_list = []
    for i in range(math.ceil(len(df) / 500)):
        df_list.append((df[i * 500:(i + 1) * 500]).reset_index())

    return df_list


def getIndex(df, title, value):
    return next(iter(df[df[title] == value].index), 'no match')


def checkRedCandle(candle):
    if candle['open'] > candle["close"]:
        return True
    else:
        return False


def getChange(current, previous):
    if current == previous:
        return 0
    try:
        return abs(round(((current - previous) / previous) * 100.0, 2))

    except ZeroDivisionError:
        return 0


def getNumByChange(enterPrice, pct):
    return round(((enterPrice * pct) + (100 * enterPrice)) / 100, 5)


def searchInArray(array, value):
    found = False
    for i in array:
        if i == value:
            found = True
            break
        else:
            found = False
    return found
