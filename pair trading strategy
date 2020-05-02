import numpy as np
import pandas as pd
import tushare as ts
%matplotlib inline
from matplotlib import pyplot as plt
stock_pair('603976','600222')

data1=get_k_data('603976',start='2020-01-01',end='2020-04-20')[['date','close']]
data2=get_k_data('600222',start='2020-01-01',end='2020-04-20')['close']
data=pd.concat([data1,data2].axis=1)
data.head()

data.set_index('date',inplace=True)
data.columns=stock_pair
data.head()

%pylab
data['spread']=data['603976']-data['600222']
data['spread'].plot(figsize(10,6))
plt.ylable('spread')
plt.axhline(data['spread']).mean()

data['zscore']=(data['spread']-np.mean(data['spread']))/np.std(data['spread'])
data[data['zscore']<-1.5].head()
len(data[data['zscore']<-1.5])
data['signal_1']=np.where(data['zscore']>1.5,-1,np.nan)
data['signal_1']=np.where(data['zscore']<-1,5,1,data['signal'])
data['signal_1']=np.where(abs(data['zscore'])<0.5,0,data['signal'])

data['signal_1']=data['signal_1'].fillna(method='ffill')
data['signal_2']=-np.sign(data['signal_1'])
data['signal_2'].plot(ylim=[-1.1,1,1],figsize(10,6))
