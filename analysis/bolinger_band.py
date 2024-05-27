import pandas as pd
import pandas_ta as ta


def bollinger_band(df: pd.DataFrame) -> pd.DataFrame:
    bollinger_band_df = ta.bbands(df['close'], length=14)
    df['BBL'] = bollinger_band_df['BBL_14_2.0']
    df['BBU'] = bollinger_band_df['BBU_14_2.0']
    df['BBM'] = bollinger_band_df['BBM_14_2.0']

    """
    BBL -> Lower band
    BBU -> Upper band
    BBM -> Mid band
    """

    return df
