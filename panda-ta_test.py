
import pandas as pd
import pandas_ta as ta

# Funcion SMA
def calcula_SMA():
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


def calcula_RSI():
    df = pd.read_csv('price.csv')
    df['HL_div_2'] = (df['High']+df['Low'])/2

    rsi_periodo = int(16)
    df['RSI'] = df.ta.rsi(length=rsi_periodo, close='HL_div_2') # "key close" "value:open"

    print("*** SMA: \n ", df['RSI'])


# main
# calcula_SMA()
calcula_RSI()