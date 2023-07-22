import math

import pandas as pd


def nadaraya_watson_envelope(length, bandwidth, error_multiplier, source_data):
    """
    Calculate the Nadaraya-Watson envelope.

    Args:
        length: The length of the envelope.
        bandwidth: The bandwidth parameter.
        error_multiplier: The multiplier for the mean absolute error.
        source_data: The source data.

    Returns:
        A tuple containing the upper band, lower band, cross-up, and cross-down values.
    """
    envelope_values = []

    for i in range(length):
        weighted_sum = 0.0
        sum_of_weights = 0.0

        for j in range(length):
            weight = math.exp(-(math.pow(i - j, 2) / (bandwidth * bandwidth * 2)))
            weighted_sum += float(source_data[j]) * float(weight)
            sum_of_weights += weight

        y = weighted_sum / sum_of_weights
        envelope_values.append(y)

    # Calculate mean absolute error
    source_data = pd.to_numeric(source_data, errors='coerce')
    mean_absolute_error = (source_data - pd.Series(envelope_values)).abs().mean() * error_multiplier

    # Calculate upper and lower bands
    upper_band = pd.Series(envelope_values) + mean_absolute_error
    lower_band = pd.Series(envelope_values) - mean_absolute_error

    # Calculate cross-up and cross-down values
    cross_up = envelope_values[0] + mean_absolute_error
    cross_down = envelope_values[0] - mean_absolute_error

    return upper_band, lower_band, cross_up, cross_down
