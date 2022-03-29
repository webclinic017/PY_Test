
import pandas as pd
import pandas_ta
import pandas_ta.momentum as ta_mom

# Funcion SMA

def calcula_SMA():#{
    df = pd.read_csv('price.csv')

    # df['SMA'] = df.ta.sma(length=5, offset=None, close="open") # "key close" "value:open"
    # print("*** Usando Open: \n" , df['SMA'])
    #
    # df['SMA_'] = df.ta.sma(length=5, offset=None)
    # print("*** Usando clolse: \n", df['SMA_'])

    df['HL_div_2'] = (df['High']+df['Low'])/2
    sma_periodo = int(3)
    df['SMA'] = df.ta.sma(length=sma_periodo, offset=None, close="HL_div_2") # "key close" "value:open"
    print("*** SMA: \n ", df['SM'])
#}

def calcula_RSI():#{
    df = pd.read_csv('price.csv')
    df['HL_div_2'] = (df['High']+df['Low'])/2
    rsi_periodo = int(16)
    df['RSI'] = df.ta.rsi(length=rsi_periodo, close='HL_div_2') # "key close" "value:open"
    print("*** SMA: \n ", df['RSI'])
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
    df_res = pandas_ta.momentum.stoch(high=high_column, low=low_column, close=hl2_column, k=fast_k, d=slow_d, smooth_k=smooth)
    print("*** STOCH_K: \n ", df_res)

#}

# main
# calcula_SMA()
# calcula_RSI()
calcula_STOCH()