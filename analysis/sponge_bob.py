import numpy as np


def spongebob_indicator(df, n1=10, n2=21, nsc=53, nsv=-53, ventas_en_sobre_compra=True, compras_en_sobre_venta=True):
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)

    ap = (df['high'] + df['low'] + df['close']) / 3
    esa = ap.ewm(span=n1).mean()
    d = np.abs(ap - esa).ewm(span=n1).mean()
    ci = (ap - esa) / (0.015 * d)
    tci = ci.ewm(span=n2).mean()

    wt1 = tci
    wt2 = wt1.rolling(window=4).mean()

    direction = np.zeros_like(wt1)
    direction[wt1.diff(periods=1) > 0] = 1
    direction[wt1.diff(periods=1) < 0] = -1
    direction[1:] = np.where(direction[1:] == 0, direction[:-1], direction[1:])

    pcol = np.where(direction > 0, "#0AAC00", np.where(direction < 0, "#FF0000", np.nan))

    midpoint = (nsc + nsv) / 2
    ploff = (nsc - midpoint) / 8

    venta = np.logical_and(
        np.logical_and(wt1.shift() > wt2.shift(), wt1 >= nsc),
        ventas_en_sobre_compra
    )
    venta_1 = np.logical_and(
        wt1.shift() > wt2.shift(),
        ~ventas_en_sobre_compra
    )

    compra = np.logical_and(
        np.logical_and(wt1.shift() < wt2.shift(), wt1 <= nsv),
        compras_en_sobre_venta
    )
    compra_1 = np.logical_and(
        wt1.shift() < wt2.shift(),
        ~compras_en_sobre_venta
    )

    df["Media WT"] = wt1
    df["sponge_bob_short"] = np.where(venta, wt2.shift() + ploff, np.nan)
    df["sponge_bob_long"] = np.where(compra, wt2.shift() - ploff, np.nan)
    df["wt2"] = wt2
    df["venta_1"] = np.where(venta_1, wt2.shift() + ploff, np.nan)
    df["compra_1"] = np.where(compra_1, wt2.shift() - ploff, np.nan)
    df['pcol'] = pcol

    return df
