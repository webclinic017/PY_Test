#
# import pandas as pd
# from stocktrends import indicators
#
# df = pd.read_csv('price.csv')
# df.columns = [i.lower() for i in df.columns]
# print("*** df: \n", df)
#
# renko = indicators.Renko(df)
# renko.brick_size = 100
# renko.chart_type = indicators.Renko.PERIOD_CLOSE
# data_RK = renko.get_ohlc_data()
# print('\n **** Renko', data_RK)

# # Ejemplo velas
# import finplot as fplt
# import yfinance
# df = yfinance.download('AAPL',interval="1d")
# fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])
# fplt.show()

# # Ejemplo Renko
# import finplot as fplt
# import yfinance as yf

# df = yf.download('BNO', '2020-01-01')
# # setup dark mode, and red/green candles
# w = fplt.foreground = '#eef'
# b = fplt.background = fplt.odd_plot_background = '#242320'
# fplt.candle_bull_color = fplt.volume_bull_color = fplt.candle_bull_body_color = fplt.volume_bull_body_color = '#352'
# fplt.candle_bear_color = fplt.volume_bear_color = '#810'
# fplt.cross_hair_color = w+'a'
#
# # plot renko + renko-transformed volume
# ax,axv = fplt.create_plot('US Brent Oil Renko [dark mode]', rows=2, maximize=False)
# plot = fplt.renko(df[['Close','Volume']], ax=ax) # let renko transform volume by passing it in as an extra column
# df_renko = plot.datasrc.df # names of new renko columns are time, open, close, high, low and whatever extras you pass in
# fplt.volume_ocv(df_renko[['time','open','close','Volume']], ax=axv)
# fplt.show()





