from utils.util import getChange, getNumByChange


def check_hit_resistant(df, mainValue, secondValue):
    for i in range(len(df)):
        if df.iloc[i]["high"] >= secondValue:
            return True

    return False


def check_hit_support(df, mainValue, secondValue):
    for i in range(len(df)):
        if df.iloc[i]["low"] <= secondValue:
            return True

    return False


def get_resistant(df):
    # get max 7 high price
    df_sorted = df.sort_values(by=['high'], ascending=False)
    df_max_7_high = df_sorted.head(10)
    resistant = []

    # loop in main df and df_max_7_high

    for i in range(len(df_max_7_high)):
        main_value = df_max_7_high.iloc[i]["high"]

        # get index for df_max_7_high from main df
        index = df.index[df['date'] == df_max_7_high.iloc[i]['date']].tolist()[0]

        if not check_hit_resistant(df[index + 1:], main_value, main_value):
            changeFromCurrent = getChange(main_value, df.iloc[-1]["close"])
            resistant.append(
                {'main_value': main_value, 'second_value': df_max_7_high.iloc[i]["low"], 'change': changeFromCurrent,
                 "date": df_max_7_high.iloc[i]["date"]})

    return resistant


def get_support(df):
    # get min 7 low price
    df_sorted = df.sort_values(by=['low'], ascending=True)
    df_min_7_low = df_sorted.head(10)
    support = []

    # loop in main df and df_min_7_low
    for i in range(len(df_min_7_low)):
        main_value = df_min_7_low.iloc[i]["low"]

        # get index for df_min_7_low from main df
        index = df.index[df['date'] == df_min_7_low.iloc[i]['date']].tolist()[0]

        if not check_hit_support(df[index + 1:], main_value, main_value):
            changeFromCurrent = getChange(main_value, df.iloc[-1]["close"])
            support.append(
                {'main_value': main_value, 'second_value': df_min_7_low.iloc[i]['high'], 'change': changeFromCurrent,
                 "date": df_min_7_low.iloc[i]["date"]})

    return support


# Back test for support and resistant strategy
def backtest_support_and_resistant(df, interval, ticker):
    i = 300
    signals = []

    while i < len(df):
        support = get_support(df[i - 300:i])
        resistant = get_resistant(df[i - 300:i])

        if len(resistant) > 0:
            main_value = resistant[-1]["main_value"]
            second_value = resistant[-1]["second_value"]

            while i < len(df):
                if df.iloc[i]["high"] >= second_value:
                    tp = getNumByChange(df.iloc[i]["high"], -1.5)
                    sl = getNumByChange(df.iloc[i]["high"], 1)
                    print("Short Signal")
                    print("Main Value: ", main_value)
                    print("Second Value: ", second_value)
                    print("Date main value: ", resistant[-1]["date"])
                    print("Enter Date: ", df.iloc[i]["date"])
                    print("Enter Price: ", df.iloc[i]["high"])
                    print("Take Profit: ", tp)
                    print("Stop Loss: ", sl)
                    print()
                    print()
                    print()

                    signals.append({
                        "main_value": main_value,
                        "second_value": second_value,
                        "date_main_value": resistant[-1]["date"],
                        "enter_date": df.iloc[i]["date"],
                        "enter_price": df.iloc[i]["high"],
                        "tp": tp,
                        "sl": sl,
                    })

                i += 1

        i += 1

    return signals
