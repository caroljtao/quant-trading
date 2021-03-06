%matplotlib inline
import matplotlib.pyplot as plt
import seaborn
import matplotlib as mpl

import numpy as np
import pandas as pd
import tushare as ts

data=ts.get_k_data('hs300',start='2020-01-01',end='2020-04-24')   #to get the candlestick chart's data 
data.head()  
data.rename(columns={'close':'price'},inplace=True)
data.set_index('date',Inplace =True)

data['SMA_10']=data['price'].rolling(10).mean()  #calculate the 10-day moving average
data['SMA_60']=data['price'].rolling(60).mean()  #calculate the 60-day moving average
data.tail()

%pylab
data[['price','SMA_10','SMA_60']].plot((fig.size(10,6))    #plot the closing price, 10-day and 60-day moving average trends.
data['return_cum']=np.log(data['price']/data['price'].shift(1)) #calculate the cummulative returns.
data['return_dis']=data['price'].pct_change                 #calculate the discrete returns
data['return_cum'].hist(bins=35)                                #plot the histogram of cumulative returns

data['signal']=np.where(data['SMA_10']>data['SMA_60'],1,-1)   #set the strategy for trading, when it returns 1, make a "long" decision,else make a "short" decision.
data.dropna(Inplace=True)
data['return_cum'].cumsum().apply(np.exp).plot(figsize(10,6))
data['signal'].plot(ylim=[-1.1,1.1],title='trading signal')

data['strategy']=data['signal'].shift(1)*data['signal']
data[['return_cum','strategy']].sum()
data[['return_cum','strategy']].cumsum().apply(np.exp).plot(figsize(10,6))

data[['return_cum','strategy']].mean()*252**0.5       #calculate the annualized volatility
data['return_cum'].cumsum.apply(np.exp)

data['cummax']=data['return_cum'].cummax()            #retracement strategy
data[['return_cum','cummax']].plot(figsize(10,6))
drawdown=data['cummax']-data['return_cum']
drawdown.max()                                        #find the largest retracement

temp=drawdown[drawdown==0]
periods=(temp.index[:1].to_datetime() -(temp.index[-1:].to_datetime())
periods.max()
               
hs300['10-60']=data['SMA_10']-data['SMA_60']            
hs300['10-60'].plot()
SD = 50                                               #set a distance between SMA10 and SMA60 lines to remove the noise
hs300['signal_optimal']=np.where(data['10-60']>SD,1,0)                       # "0" means taking no action, that is noise.
hs300['signal_optimal']=np.where(data['10-60']<-SD,-1,hs300['signal_optimal'])
hs300['signal_optimal'].value_counts()
