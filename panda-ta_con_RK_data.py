
import pandas as pd
import mplfinance as mpf
import pandas_ta.overlap as ta_overlap
import pandas_ta.momentum as ta_momentum
import pandas_ta.trend as ta_trend
from stocktrends import indicators

# Funcion SMA
from stocktrends import indicators

#Constantes
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
    # print('**** Renko', data_RK)

    if (len(data_RK[data_RK.index.duplicated()]) > 0):  # {
        print("*** cargaDatosCSV - Antes - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
        data_RK = data_RK.loc[~data_RK.index.duplicated(), :]
        print("*** cargaDatosCSV - Despues - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
    # }
    return data_RK
# }

def calcula_SMA(data_RK):#{
    sma_periodo = int(3)
    data_RK[_SMA_RAPIDA] = ta_overlap.sma(close=data_RK[_HL2], length=sma_periodo, talib=True)

    # df_new_size = data_RK.size
    # llenarEspacios = 0
    # if rk_size > df_new_size :  # {
    #     llenarEspacios = rk_size - df_new_size
    #     print("*** LlenarEspacios SMA: " + str(llenarEspacios) + " - data_RK.size:" + str(rk_size) + " - df_new_size.size:" + str(df_new_size))
    # # }

    if (len(data_RK[data_RK.index.duplicated()]) > 0):  # {
        print("*** calcula_SMA - Antes - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
        data_RK = data_RK.loc[~data_RK.index.duplicated(), :]
        print("*** calcula_SMA - Despues - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
    # }
    # print("*** SMA: \n ", data_RK)
#}

def calcula_RSI(data_RK):#{
    rsi_periodo = int(16)
    data_RK = ta_momentum.rsi(close=data_RK[_HL2], length=rsi_periodo, scalar=None, talib=True)

    if (len(data_RK[data_RK.index.duplicated()]) > 0):  # {
        print("*** calcula_RSI - Antes - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
        data_RK = data_RK.loc[~data_RK.index.duplicated(), :]
        print("*** calcula_RSI - Despues - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
    # }

    # print("*** RSI: \n ", data_RK)
#}

def calcula_STOCH(data_RK):#{
    #k:100 d:10 smooth:2
    fast_k = int(10) #Ideal:  100-10-2
    slow_d = int(3)  #tocada: 10-3-2
    smooth = int(2)

    high_column = data_RK.get(_HIGH)
    low_column = data_RK.get(_LOW)
    hl2_column = data_RK.get(_HL2)

    df_stoch = ta_momentum.stoch(high=high_column, low=low_column, close=hl2_column, k=fast_k,d=slow_d, smooth_k=smooth)
    df_stoch.columns = [i[0:6].lower() for i in df_stoch.columns]  # stochk  stochd

    if (len(data_RK[data_RK.index.duplicated()]) > 0):  # {
        print("*** calcula_STOCH - Antes - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
        df_stoch = df_stoch.loc[~df_stoch.index.duplicated(), :]
        print("*** calcula_STOCH - Despues - Row duplicados: ", data_RK[data_RK.index.duplicated()].head())
    # }

    # print("*** df_stoch: \n ", df_stoch.head())

    data_RK[_STOCH_K] = df_stoch[_STOCH_K]
    data_RK[_STOCH_D] = df_stoch[_STOCH_D]

    df_new_size = data_RK.size
    llenarEspacios = 0
    if rk_size > df_new_size: #{
        llenarEspacios = rk_size - df_new_size
        print("*** LlenarEspacios STOCH: " + str(llenarEspacios) + " - data_RK.size:" + str(rk_size) + " - df_new_size.size:" + str(df_new_size))
    # }
    print("*** STOCH_K: \n ", data_RK.head())
#}

def calcula_ADX(data_RK):#{
    high_column = data_RK.get(_HIGH)
    low_column = data_RK.get(_LOW)
    hl2_column = data_RK.get(_HL2)
    length_DI = int(16)
    lensig_ADX = int(16)
    data_RK = ta_trend.adx(high=high_column, low=low_column, close=hl2_column, length=length_DI, lensig=lensig_ADX)

    data_RK.columns = [i[0:3].lower() for i in data_RK.columns]  #adx dmp dmn
    print("*** ADX: \n ", data_RK)
#}

# main

data_RK = cargaDatosCSV();
rk_size = data_RK.size

calcula_SMA(data_RK)
calcula_RSI(data_RK)
calcula_STOCH(data_RK)
# calcula_ADX(data_RK)