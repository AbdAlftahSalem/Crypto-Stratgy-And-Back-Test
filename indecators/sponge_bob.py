import pandas_ta as ta


def SpongeBob(df, n1=10, n2=21, reaction_wt=1):
    ap = (df["high"] + df["low"] + df["close"]) / 3
    esa = ta.ema(ap, length=n1)
    d = ta.ema(abs(ap - esa), length=n1)
    ci = (ap - esa) / (0.015 * d)
    tci = ta.ema(ci, length=n2)
    wt1 = tci

    # slope = ta.slope(wt1, length=reaction_wt)
    #
    # direction = np.where(slope > 0, 1, np.where(slope < 0, -1, 0))
    #
    # pcol = pd.Series(index=df.index)

    # pcol.loc[direction > 0] = "green"
    # pcol.loc[direction < 0] = "red"
    df["Media WT"] = wt1
    df['Media WT'] = df['Media WT'].fillna(0)

    for i in range(1, len(df)):

        if int(df.loc[i, 'Media WT']) >= int(df.loc[i - 1, 'Media WT']):
            df.loc[i, 'color'] = 'green'
        else:
            df.loc[i, 'color'] = 'red'

    print(df)
