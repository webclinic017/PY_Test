
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

    sma_rapida=int(3)
    df['SMA_rapida'] = df.ta.sma(length=sma_rapida, offset=None, close="HL_div_2") # "key close" "value:open"

    print("*** SMA_rapida: \n ", df['SMA_rapida'])

# main
# calcula_SMA()