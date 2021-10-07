import pandas as pd
import numpy
import mplfinance as mpf


def func(fsymbol, charttype):

    filename = "static/sto.png"

    df = pd.read_json("StockoList.json")

    df.set_index('date')
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df.index = pd.DatetimeIndex(df['date'])

    dk = df.loc[df['symbol']==fsymbol]

    if charttype != "":
        mpf.plot(dk, type = charttype, savefig=filename, style="binance")

    else:
        mpf.plot(dk, savefig=filename,  tight_layout=True, style="binance")




