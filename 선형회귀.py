#!/usr/bin/env python
# coding: utf-8

# In[34]:


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
from sklearn.model_selection import cross_val_score
pd.options.display.float_format = '{:.0f}'.format
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score


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
m=pd.DataFrame(corr['전국 관객수'])


# In[9]:


x=data.drop(columns=['전국 매출액','전국 관객수'])
y=target
x.columns
len(x.columns)


# In[10]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=5)


# In[11]:


model=LinearRegression()
model.fit(x_train,y_train)


# In[12]:


y_test_prediction=model.predict(x_test)


# In[13]:


mse=mean_squared_error(y_test,y_test_prediction)


# In[14]:


mse**0.5


# In[15]:


k_fold_score = np.average(cross_val_score(model, x, y,cv=5))
k_fold_score


# In[16]:


model.score(x_test,y_test)


# In[18]:


k=pd.DataFrame(y_test_prediction)


# In[20]:


model.coef_


# In[26]:


model.intercept_


# In[31]:


m=model.predict(x_train)
m=pd.DataFrame(m)
n=pd.DataFrame(y_train)


# In[35]:


r2_score(m,n)


# In[ ]:




