def get_support_and_resistant(df, left_size, right_size):
    support_and_resistant = [0] * (left_size + right_size + 1)
    for i in range(left_size + 1, len(df) - right_size):
        left_df = df[i - left_size:i]
        right_df = df[i: i + right_size]

        current_low = df.iloc[i]['low']
        current_high = df.iloc[i]['high']

        min_low_left = min(left_df['low'])
        min_low_right = min(right_df['low'])

        max_high_left = max(left_df['high'])
        max_high_right = max(right_df['high'])

        if current_low <= min_low_left and current_low <= min_low_right:
            # RESISTANT LEVEL
            support_and_resistant.append(-1)

        elif current_high >= max_high_left and current_high >= max_high_right:
            # SUPPORT LEVEL
            support_and_resistant.append(1)

        else:
            # NORMAL CANDLE
            support_and_resistant.append(0)

    return support_and_resistant
