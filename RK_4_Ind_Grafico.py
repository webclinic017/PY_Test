
import pandas as pd
import mplfinance as mpf
import pandas_ta.overlap as ta_overlap
import pandas_ta.momentum as ta_momentum
import pandas_ta.trend as ta_trend
from stocktrends import indicators

# variables
_BRICK_SIZE = 50
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
_STOCH_K = 'stochk'
_STOCH_D = 'stochd'
_ADX = 'adx'
_DMP = 'dmp'
_DMN = 'dmn'

def cargaDatosCSV():  # {
    # df = pd.read_csv('price.csv')
    # df.columns = [i.lower() for i in df.columns] #lower case a nombres de columnas
    # df[_HL2] = (df[_HIGH] + df[_LOW])/2
    # df.index = pd.DatetimeIndex(df[_DATE])
    # print('**** df: \n', df)
    # return df

    df_new = pd.read_csv('price.csv')
    df_new.columns = [i.lower() for i in df_new.columns]  #lower case a nombres de columnas
    renko = indicators.Renko(df_new)
    renko.brick_size = _BRICK_SIZE
    renko.chart_type = indicators.Renko.PERIOD_CLOSE
    data_RK = renko.get_ohlc_data()

    # usados por las SMA
    data_RK[_HL2] = (data_RK[_HIGH] + data_RK[_LOW])/2
    data_RK.index = pd.DatetimeIndex(data_RK[_DATE])

    data_RK['volume'] = 1

    if (len(data_RK[data_RK.index.duplicated()]) > 0):  # {
        print("*** cargaDatosCSV - Antes - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
        data_RK = data_RK.loc[~data_RK.index.duplicated(), :]
        print("*** cargaDatosCSV - Despues - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
    # }
    print("*** cargaDatosCSV - data_RK: \n ", data_RK)

    return data_RK
# }

def calculoSMA(data_RK):#{
    sma_rapida=int(3)
    data_RK[_SMA_RAPIDA] = ta_overlap.sma(close=data_RK[_HL2], length=sma_rapida, talib=True)

    sma_lenta=int(6)
    data_RK[_SMA_LENTA] = ta_overlap.sma(close=data_RK[_HL2], length=sma_lenta, talib=True)

    if (len(data_RK[data_RK.index.duplicated()]) > 0):  # {
        print("*** calculoSMA - Antes - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
        data_RK = data_RK.loc[~data_RK.index.duplicated(), :]
        print("*** calculoSMA - Despues - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
    # }

    # print("*** calculoSMA - data_RK: \n ", data_RK)
#}

def calculosRSI(data_RK):#{
    rsi_periodo=int(16)
    data_RK[_RSI] = ta_momentum.rsi(close=data_RK[_HL2], length=rsi_periodo, scalar=None, talib=True)
    data_RK[_SMA_RSI] = ta_overlap.sma(close=data_RK[_RSI], length=rsi_periodo, talib=True)
    # print(data_RK.head())   #check primeros values
    # print(data_RK.tail())  #check ultimos values

    if (len(data_RK[data_RK.index.duplicated()]) > 0):  # {
        print("*** calcula_RSI - Antes - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
        data_RK = data_RK.loc[~data_RK.index.duplicated(), :]
        print("*** calcula_RSI - Despues - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
    # }
    # print("*** calculosRSI - data_RK: \n ", data_RK)
#}

def calcula_STOCH(data_RK):#{
    #k:100 d:10 smooth:2
    fast_k = int(10) # JFM Ideal:  100-10-2
    slow_d = int(3)  # JFM tocada: 10-3-2
    smooth = int(2)

    high_column = data_RK.get(_HIGH)
    low_column = data_RK.get(_LOW)
    hl2_column = data_RK.get(_HL2)

    df_stoch = ta_momentum.stoch(high=high_column, low=low_column, close=hl2_column, k=fast_k,d=slow_d, smooth_k=smooth)
    df_stoch.columns = [i[0:6].lower() for i in df_stoch.columns]  # stochk  stochd

    # Tratamiento de duplicados
    if (len(df_stoch[df_stoch.index.duplicated()]) > 0):  # {
        print("*** calcula_STOCH - Antes - Row duplicados: ", df_stoch[df_stoch.index.duplicated()].head())
        df_stoch = df_stoch.loc[~df_stoch.index.duplicated(), :]
        print("*** calcula_STOCH - Despues - Row duplicados: ", df_stoch[df_stoch.index.duplicated()].head())
    # }

    data_RK[_STOCH_K] = df_stoch[_STOCH_K]
    data_RK[_STOCH_D] = df_stoch[_STOCH_D]

    df_new_size = data_RK.size
    llenarEspacios = 0
    if rk_size > df_new_size: #{
        llenarEspacios = rk_size - df_new_size
        print("*** LlenarEspacios STOCH: " + str(llenarEspacios) + " - data_RK.size:" + str(rk_size) + " - df_new_size.size:" + str(df_new_size))
    # }
    # print("*** calcula_STOCH - data_RK: \n ", data_RK)
#}

def calcula_ADX(df_RK):#{
    high_column = df_RK.get(_HIGH)
    low_column = df_RK.get(_LOW)
    hl2_column = df_RK.get(_HL2)
    length_DI = int(16)
    lensig_ADX = int(16)
    df_adx = ta_trend.adx(high=high_column, low=low_column, close=hl2_column, length=length_DI, lensig=lensig_ADX)
    df_adx.columns = [i[0:3].lower() for i in df_adx.columns]  #adx dmp dmn

    #Tratamiento de duplicados
    if (len(df_adx[df_adx.index.duplicated()]) > 0):  # {
        print("*** calcula_ADX - Antes - Row duplicados: ", df_adx[df_adx.index.duplicated()].head())
        df_stoch = df_stoch.loc[~df_stoch.index.duplicated(), :]
        print("*** calcula_ADX - Despues - Row duplicados: ", df_adx[df_adx.index.duplicated()].head())
    # }

    data_RK[_ADX] = df_adx[_ADX]
    data_RK[_DMP] = df_adx[_DMP]
    data_RK[_DMN] = df_adx[_DMN]

    df_new_size = data_RK.size
    llenarEspacios = 0
    if rk_size > df_new_size:  # {
        llenarEspacios = rk_size - df_new_size
        print("*** LlenarEspacios ADX: " + str(llenarEspacios) + " - data_RK.size:" + str(
            rk_size) + " - df_new_size.size:" + str(df_new_size))
    # }
    # print("*** calcula_STOCH - data_RK: \n ", data_RK)
#}

def plot_all(data_RK):#{
    # Plot de DataFrames
    fig = mpf.figure()
    ax1 = fig.add_subplot(4,1,1, style='binance')  # count=4, file=1, row=1...4
    ax2 = fig.add_subplot(4,1,2, sharex=ax1, style='binance')
    ax3 = fig.add_subplot(4,1,3, sharex=ax1, style='binance')
    ax4 = fig.add_subplot(4,1,4, sharex=ax1, style='binance')
    ap = [ mpf.make_addplot(data_RK[[_RSI,_SMA_RSI]],type='line', ax=ax2, ylabel=''),
           mpf.make_addplot(data_RK[[_STOCH_K,_STOCH_D]], type='line', ax=ax3, ylabel=''),
           mpf.make_addplot(data_RK[[_ADX,_DMP,_DMN]], type='line', ax=ax4, ylabel=''),
           mpf.make_addplot(data_RK[[_SMA_RAPIDA,_SMA_LENTA]], type='line', ax=ax1, ylabel='')
         ]

    #_ADX _DMP _DMN

    #Segundo grafico
    #Hlines grafico
    anchoDibujo = int(data_RK[_CLOSE].size)
    ax2.hlines(y=30,  xmin=0, xmax=anchoDibujo, colors='orange', linestyle='dotted', linewidth=2)
    ax2.hlines(y=50,  xmin=0, xmax=anchoDibujo, colors='grey', linestyle='dotted', linewidth=2)
    ax2.hlines(y=70,  xmin=0, xmax=anchoDibujo, colors='orange', linestyle='dotted', linewidth=2)

    #Titulos
    ax1.set_title('Precios', loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})
    ax2.set_title('RSI', loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})
    ax3.set_title('STOCH', loc="left", fontdict={'fontsize': 8, 'fontweight': 'bold', 'color': 'tab:blue'})
    ax4.set_title('ADX', loc="left", fontdict={'fontsize': 8, 'fontweight': 'bold', 'color': 'tab:blue'})

    #Referencias de lineas
    ax1.legend(loc='best')
    ax2.legend(loc='best')
    ax3.legend(loc='best')
    ax4.legend(loc='best')

    #Size dibujo
    fig.set_figheight(10)
    fig.set_figwidth(anchoDibujo)

    #Ocultar "escala x" en ax1
    ax1.xaxis.set_visible(False)
    ax2.xaxis.set_visible(False)
    ax3.xaxis.set_visible(False)
    ax4.xaxis.set_visible(True)
    # ax1.yaxis.set_visible(True)

    #Grilla
    ax1.grid(),ax2.grid(),ax3.grid(),ax4.grid()

    # print("plot_all \n :", data_RK.tail())

    #Plot grafico
    mpf.plot(data_RK, type='line', ax=ax1, addplot=ap, xrotation=90, datetime_format='%Y-%m-%d', linecolor='black')

    #Plot renko
    # mpf.plot(data_RK, type='renko', ax=ax1, xrotation=90, datetime_format='%Y-%m-%d', renko_params=dict(brick_size=_BRICK_SIZE))

    mpf.show()
#}

data_RK = cargaDatosCSV()
rk_size = data_RK.size

calculoSMA(data_RK)
calculosRSI(data_RK)
calcula_STOCH(data_RK)
calcula_ADX(data_RK)
plot_all(data_RK)