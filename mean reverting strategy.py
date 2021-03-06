import numpy as np
import pandas as pd
import tushare as ts
%matplotlib inline
import matploblib pyplot as plt
plt.style.use('seaborn')
import matplotlib as mpl

%pylab
data=ts.get_k_data('hs300',start='2020-01-01',end='2020-04-28')[['date','close']]
data.rename(columns={'close':'price'},inplace=True)
data['price'].plot(figsize(10,6))

data['return_cum']=np.log([data['price']/data['price'].shift(1))
SMA=50
data['SMA']=data['price'].rolling(SMA).mean()
threshold= 200                 # distance far enough from SMA to execute the MR strategy
data['distance'].dropna().plot(figsize(10,6),legend=True)
plt.axhline(threshold,color='r')
plt.axhline(-threshold,color='r')
plt.axhline(0,color='r')

data['signal']=np.where(data['gap']>threshold,-1,np.nan)
data['signal']=np.where(data['gap']<-threshold,1,data['signal'])
data['signal']=np.where(data['distance']*data['distance'].shift(1)<0,0,data['signal'])
data['signal']=data['signal'].ffill().fillna(0)
data['signal'].ix[SMA].plot(ylim=[-1.1,1,1].figsize(10,6))
