import math

import pandas as pd


def nadaraya_watson_envelope(length, h, mult, src):
    y = []

    for i in range(length):
        sum = 0.
        sumw = 0.

        for j in range(length):
            w = math.exp(-(math.pow(i - j, 2) / (h * h * 2)))
            sum += src[j] * w
            sumw += w

        y2 = sum / sumw
        y.append(y2)

    mae = (src - pd.Series(y)).abs().mean() * mult

    upper = pd.Series(y) + mae
    lower = pd.Series(y) - mae

    cross_up = y[0] + mae
    cross_dn = y[0] - mae

    return upper, lower, cross_up, cross_dn
