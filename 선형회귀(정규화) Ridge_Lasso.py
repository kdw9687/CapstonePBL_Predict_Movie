#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import seaborn as sns
pd.set_option('display.max_colwidth',None)
pd.set_option('display.max_rows',None)
data=pd.read_csv("/Users/kimdongwook/Desktop/캡스톤 디자인/데이터 판다스용완.csv")
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
import time
import datetime
start=time.time()


# In[2]:


data.dropna(inplace=True)


# In[3]:


data.drop(columns=['순번','장르','국적.1','연휴 및 기념일 상영 여부'],inplace=True)


# In[4]:


data.set_index('영화명',inplace=True)


# In[5]:


corr=data.corr()


# In[6]:


target=data['전국 관객수']
target.dropna(inplace=True)


# In[7]:


corr['전국 관객수']


# In[8]:


x=data.drop(columns=['전국 매출액','전국 관객수'])
y=target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=5)


# In[9]:


model=Ridge(alpha=0.001,max_iter=100000,normalize=True)
model.fit(x_train,y_train)
y_train_predict=model.predict(x_train)
y_test_predict=model.predict(x_test)
mse = mean_squared_error(y_test, y_test_predict)


# In[10]:


y_test_predict
k=pd.DataFrame(y_test_predict)
k


# In[11]:


mse**0.5


# In[12]:


r2_score(y_test,y_test_predict)


# In[13]:


model1=Lasso(alpha=0.1,max_iter=1000000,normalize=True)
model1.fit(x_train,y_train)
y_train_predict=model1.predict(x_train)
y_test_predict=model1.predict(x_test)
mse = mean_squared_error(y_train, y_train_predict)


# In[14]:


mse**0.5


# In[15]:


model1.score(x_test,y_test)


# In[16]:


r2_score(y_test,y_test_predict)


# In[17]:


k=pd.DataFrame(y_test_predict)
k


# In[18]:


sec = time.time()-start
times = str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]
print(times)

