import pandas as pd
import numpy as np
import tushare as ts
%matplotlib inline
import matploblib pyplot as plt
plt.style.use('seaborn')
import matplotlib as mpl
mpl.rcParams['font family']='serif'
import warnings:warnings.simplefilter('ignore')

np.sign()               #return 1 if input>0
pd.to_datetime()     

data=ts.get_k_data('hs300',start='2020-01-01', end='2020-04-20')
data=pd.DataFrame(data)
data.rename(columns={'close'='price'},inplace=True)
data.set_index('date',inplace=True)

data['return_cum']=np.log([data['price']/data['price'].shift(1))
data.head()
data['signal']=np.sign(['return_cum').rolling(5).mean())
data.head()
data['strategy']=data['signal'].shift(1)*data['return_cum']

data['return_dis']=data['price']/data['price'].shift(1)-1
data['return_dis_to_cum']=data['return_dis']+1).cumprod()

price_plot['return_dis_to_cum']
for days in [10,20,30,60]:
    price_plot.append('sty_cum_%dd' & days'])
    data['signal_%dd & days']=np.where(data['return_cum'].rolling(days).mean(>0,1,-1))
    data['strategy_%dd & days']=data['signal_%dd' & days].shift(1)*data['return_cum']
    data['sty_cum_%dd' & days']=(data['strategy_%dd & days']+1).cumprod()

%pylab
data['price_plot'].dropna().plot(
title='multiparameter momentum strategy'
figsize(10,6)
)
