
import pandas as pd

import pandas_ta.overlap as ta_overlap
import pandas_ta.momentum as ta_momentum

# Funcion SMA

def calcula_SMA():#{
    df = pd.read_csv('price.csv')
    df['HL_div_2'] = (df['High']+df['Low'])/2

    sma_periodo = int(3)
    df_res = ta_overlap.sma(close=df['HL_div_2'], length=sma_periodo, talib=True)
    print("*** SMA: \n ", df_res)
#}

def calcula_RSI():#{
    df = pd.read_csv('price.csv')
    df['HL_div_2'] = (df['High']+df['Low'])/2

    rsi_periodo = int(16)
    #df['RSI'] = df.ta.rsi(length=rsi_periodo, close='HL_div_2') # "key close" "value:open"
    df_res = ta_momentum.rsi(close=df['HL_div_2'], length=rsi_periodo, scalar=None, talib=True)
    print("*** RSI: \n ", df_res)
#}

def calcula_STOCH():#{
    df = pd.read_csv('price.csv')
    df['HL2'] = (df['High']+df['Low'])/2

    #k:100 d:10 smooth:2
    fast_k = int(10) #100
    slow_d = int(3)  #10
    smooth = int(2)

    high_column = df.get('High')
    low_column = df.get('Low')
    hl2_column = df.get('HL2')

    # df['STOCH_K'], df['STOCH_D'] = df.ta.stoch(fast_k, slow_d, high='High', low='Low', close='HL_div_2', append=True) # "key close" "value:open"
    # print("*** STOCH_K: \n ", df['STOCH_K'])
    df.ta.stoch
    #high, low, close, k=None, d=None, smooth_k=None
    df_res = ta_momentum.stoch(high=high_column, low=low_column, close=hl2_column, k=fast_k, d=slow_d, smooth_k=smooth)
    print("*** STOCH_K: \n ", df_res)

#}

# main
calcula_SMA()
#calcula_RSI()
#calcula_STOCH()