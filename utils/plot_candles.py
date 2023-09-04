import matplotlib.pyplot as plt
import pandas as pd


def plot_with_signals(df, output, save_path=None):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot candlesticks
    df['date'] = pd.to_datetime(df['date'])
    candle_colors = df.apply(lambda x: 'g' if x['close'] > x['open'] else 'r', axis=1)
    ax.bar(df['date'], df['high'] - df['low'], bottom=df['low'], width=0.2, color=candle_colors, align='center')

    for data in output['data']:
        entry_date = data['entryDate']
        out_date = data['outDate']
        enter_price = data['enter_price']
        status = data['status']

        entry_candle = df[df['date'] == entry_date].iloc[0]
        if entry_date != out_date:
            out_candle = df[df['date'] == out_date].iloc[0]

        arrow_color = 'g' if status == 'tp' else 'r'
        arrow_xy = (entry_candle['date'], entry_candle['low'])

        ax.annotate('',
                    xy=arrow_xy,
                    xytext=(arrow_xy[0], arrow_xy[1] - 10),
                    arrowprops=dict(arrowstyle=f'-|>', color=arrow_color))

        if status == 'tp' and entry_date != out_date:
            ax.annotate('*',
                        xy=arrow_xy,
                        xytext=(arrow_xy[0], arrow_xy[1] - 18),
                        color='g', weight='bold')

    ax.xaxis.set_major_formatter(plt.FixedFormatter(df['date'].dt.strftime('%Y-%m-%d')))
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'Candlesticks with Entry Signals for {output["ticker"]} ({output["frame"]})')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, format='svg')
        print(f"Plot saved as {save_path}")
    else:
        plt.show()

# plot_with_signals(df, dataLong, save_path=f"{const_app.saveDataFolderIndicator}{ticker}-{frame}-long.svg")
