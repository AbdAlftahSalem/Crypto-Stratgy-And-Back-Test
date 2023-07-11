import math


def divideDf(df) -> list:
    """
    Divide a DataFrame into smaller chunks of size 500.

    Args:
        df: The DataFrame to be divided.

    Returns:
        A list of smaller DataFrames.

    """
    df_list = []
    for i in range(math.ceil(len(df) / 500)):
        df_list.append((df[i * 500:(i + 1) * 500]).reset_index())

    return df_list


def getIndex(df, title, value):
    """
    Get the index of the first occurrence of a specific value in a DataFrame column.

    Args:
        df: The DataFrame to search in.
        title: The column name to search for the value.
        value: The value to find.

    Returns:
        The index of the first occurrence of the value in the column, or 'no match' if not found.

    """
    return next(iter(df[df[title] == value].index), 'no match')


def checkRedCandle(candle):
    """
    Check if a candle represents a red candle (open > close).

    Args:
        candle: A dictionary representing the candle with 'open' and 'close' values.

    Returns:
        True if the candle is red, False otherwise.

    """
    if candle['open'] > candle["close"]:
        return True
    else:
        return False


def getChange(current, previous):
    """
    Calculate the percentage change between two values.

    Args:
        current: The current value.
        previous: The previous value.

    Returns:
        The percentage change rounded to 2 decimal places.

    """
    if current == previous:
        return 0
    try:
        return abs(round(((current - previous) / previous) * 100.0, 2))
    except ZeroDivisionError:
        return 0


def getNumByChange(enterPrice, pct):
    """
    Calculate the resulting number by applying a percentage change to a given number.

    Args:
        enterPrice: The original number.
        pct: The percentage change.

    Returns:
        The resulting number after applying the percentage change.

    """
    return round(((enterPrice * pct) + (100 * enterPrice)) / 100, 5)


def searchInArray(array, value):
    """
    Check if a value is present in an array.

    Args:
        array: The array to search in.
        value: The value to search for.

    Returns:
        True if the value is found, False otherwise.

    """
    found = False
    for i in array:
        if i == value:
            found = True
            break
        else:
            found = False
    return found
