
import pandas as pd
import mplfinance as mpf
import pandas_ta.overlap as ta_overlap
import pandas_ta.momentum as ta_momentum
import pandas_ta.trend as ta_trend
from stocktrends import indicators

# variables de columnas de dataframe
_DATE = 'date'
_OPEN = 'open'
_CLOSE = 'close'
_HIGH = 'high'
_LOW = 'low'
_HL2 = 'hl2'
_SMA_RAPIDA = 'sma_rapida'
_SMA_LENTA = 'sma_lenta'
_RSI = 'rsi'
_SMA_RSI = 'sma_rsi'

def cargaDatosCSV():  # {
    df = pd.read_csv('price.csv')
    df.columns = [i.lower() for i in df.columns] #lower case a nombres de columnas
    df[_HL2] = (df[_HIGH] + df[_LOW])/2
    df.index = pd.DatetimeIndex(df[_DATE])
    print('**** df: \n', df)
    return df


    # df_new = pd.read_csv('price.csv')
    # df_new.columns = [i.lower() for i in df_new.columns]  #lower case a nombres de columnas
    # renko = indicators.Renko(df_new)
    # renko.brick_size = 50
    # renko.chart_type = indicators.Renko.PERIOD_CLOSE
    # data_RK = renko.get_ohlc_data()

    # # usados por las SMA
    # data_RK[_HL2] = (data_RK[_HIGH] + data_RK[_LOW])/2
    # data_RK.index = pd.DatetimeIndex(data_RK[_DATE])
    #
    # print('**** Renko', data_RK)
    #
    # return data_RK
# }

def calculoSMA():#{
    sma_rapida=int(3)
    df[_SMA_RAPIDA] = ta_overlap.sma(close=df[_HL2], length=sma_rapida, talib=True)

    sma_lenta=int(6)
    df[_SMA_LENTA] = ta_overlap.sma(close=df[_HL2], length=sma_lenta, talib=True)
    return df
#}

def calculosRSI():#{
    rsi_periodo=int(16)
    df[_RSI] = ta_momentum.rsi(close=df[_HL2], length=rsi_periodo, scalar=None, talib=True)
    df[_SMA_RSI] = ta_overlap.sma(close=df[_RSI], length=rsi_periodo, talib=True)
    # print(df.head())   #check primeros values
    # print(df.tail())  #check ultimos values
    return df
#}

def plot_all():#{
    # Plot de DataFrames
    fig = mpf.figure()
    ax1 = fig.add_subplot(2,1,1, style='binance')
    ax2 = fig.add_subplot(2,1,2, sharex=ax1, style='binance')
    ap = [ mpf.make_addplot(df[[_RSI,_SMA_RSI]],type='line', ax=ax2, ylabel=''),
           mpf.make_addplot(df[[_SMA_RAPIDA,_SMA_LENTA]], type='line', ax=ax1, ylabel='')
         ]

    # Segundo grafico
    #Hlines grafico
    anchoDibujo = int(df[_CLOSE].size)
    ax2.hlines(y=30,  xmin=0, xmax=anchoDibujo, colors='orange', linestyle='dotted', linewidth=2)
    ax2.hlines(y=50,  xmin=0, xmax=anchoDibujo, colors='grey', linestyle='dotted', linewidth=2)
    ax2.hlines(y=70,  xmin=0, xmax=anchoDibujo, colors='orange', linestyle='dotted', linewidth=2)

    # Titulos
    ax1.set_title('Precios', loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})
    ax2.set_title(_RSI, loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})

    #Referencias de lineas
    ax1.legend(loc='best')
    ax2.legend(loc='best')

    #size dibujo
    fig.set_figheight(10)
    fig.set_figwidth(anchoDibujo)

    #Ocultar "escala x" en ax1
    ax1.xaxis.set_visible(False)
    ax1.yaxis.set_visible(True)

    #Grilla
    ax1.grid(),ax2.grid()

    # Plot grafico
    mpf.plot(df, type='candle', ax=ax1, addplot=ap, xrotation=90, datetime_format='%Y-%m-%d')
    mpf.show()
#}

df = cargaDatosCSV()
df = calculoSMA()
df = calculosRSI()
plot_all()