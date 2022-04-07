
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

    return data_RK
# }

def calcula_SMA(df_RK):#{
    sma_periodo = int(3)
    df_RK = ta_overlap.sma(close=df_RK[_HL2], length=sma_periodo, talib=True)
    # print("*** SMA: \n ", df_RK)
#}

def calcula_RSI(df_RK):#{
    rsi_periodo = int(16)
    df_RK = ta_momentum.rsi(close=df_RK[_HL2], length=rsi_periodo, scalar=None, talib=True)
    # print("*** RSI: \n ", df_RK)
#}

def calcula_STOCH(df_RK):#{
    #k:100 d:10 smooth:2
    fast_k = int(10) #Ideal:  100-10-2
    slow_d = int(3)  #tocada: 10-3-2
    smooth = int(2)

    high_column = df_RK.get(_HIGH)
    low_column = df_RK.get(_LOW)
    hl2_column = df_RK.get(_HL2)

    df_RK = ta_momentum.stoch(high=high_column, low=low_column, close=hl2_column, k=fast_k, d=slow_d, smooth_k=smooth)
    # print("*** STOCH_K: \n ", df_RK)
#}

def calcula_ADX(df_RK):#{
    high_column = df_RK.get(_HIGH)
    low_column = df_RK.get(_LOW)
    hl2_column = df_RK.get(_HL2)
    length_DI = int(16)
    lensig_ADX = int(16)
    df_RK = ta_trend.adx(high=high_column, low=low_column, close=hl2_column, length=length_DI, lensig=lensig_ADX)

    df_RK.columns = [i[0:3].lower() for i in df_RK.columns]  #adx dmp dmn
    print("*** ADX: \n ", df_RK)
#}

# main

df_RK = cargaDatosCSV();
calcula_SMA(df_RK)
calcula_RSI(df_RK)
calcula_STOCH(df_RK)
calcula_ADX(df_RK)