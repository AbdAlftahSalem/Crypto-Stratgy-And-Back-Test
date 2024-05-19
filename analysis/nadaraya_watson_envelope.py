import numpy as np
import pandas as pd
from joblib import Parallel, delayed

from utils.util import divide_df


def nadaraya_watson_envelope(length, bandwidth, error_multiplier, source_data):
    indices = np.arange(length)
    weights = np.exp(-((np.subtract.outer(indices, indices) ** 2) / (bandwidth * bandwidth * 2)))

    weighted_sums = np.dot(weights, source_data)
    sum_of_weights = weights.sum(axis=1)

    envelope_values = weighted_sums / sum_of_weights

    mean_absolute_error = (np.abs(source_data - envelope_values).mean()) * error_multiplier

    upper_band = envelope_values + mean_absolute_error
    lower_band = envelope_values - mean_absolute_error

    cross_up = envelope_values[0] + mean_absolute_error
    cross_down = envelope_values[0] - mean_absolute_error

    return upper_band, lower_band, cross_up, cross_down


def apply_waston_envelope(df: pd.DataFrame):
    data = divide_df(df)

    def process_single(i):
        if len(i) > 499:
            close = i["close"]

            envelope = nadaraya_watson_envelope(500, 17, 4.0, close)
            upper, lower = envelope[:2]

            i["upper"] = upper
            i["lower"] = lower

            return i

    # Parallelize the processing of individual data chunks
    fullDF = Parallel(n_jobs=-1)(delayed(process_single)(i) for i in data if len(i) > 499)

    return pd.concat(fullDF, ignore_index=True)
