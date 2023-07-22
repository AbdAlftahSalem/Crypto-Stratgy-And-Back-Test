import get_data
from python.strategy.data_adapter import get_30m_data, get_1h_data

df = get_data.getFromBinance("ETHUSDT", "15m", 800)
df30m = get_30m_data(df)
df1h = get_1h_data(df)
