def get_support_and_resistant(df, left_size, right_size):
    if df is None or df.empty:
        raise ValueError("DataFrame is None or empty in get_support_and_resistant")

    if 'low' not in df.columns or 'high' not in df.columns:
        raise ValueError("Columns 'low' and 'high' are missing in DataFrame")

    support_and_resistant = [0] * (left_size + right_size + 1)

    for i in range(left_size + 1, len(df) - right_size):
        left_df = df.iloc[i - left_size:i]
        right_df = df.iloc[i: i + right_size]

        current_low = df.iloc[i]['low']
        current_high = df.iloc[i]['high']

        min_low_left = min(left_df['low'])
        min_low_right = min(right_df['low'])

        max_high_left = max(left_df['high'])
        max_high_right = max(right_df['high'])

        if current_low <= min_low_left and current_low <= min_low_right:
            support_and_resistant.append(-1)
        elif current_high >= max_high_left and current_high >= max_high_right:
            support_and_resistant.append(1)
        else:
            support_and_resistant.append(0)

    return support_and_resistant
