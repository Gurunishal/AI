#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


data =pd.read_csv('train.csv')


# In[11]:


data.head()


# In[12]:


a = data.iloc[3,1:].values

a=a.reshape(28,28).astype('uint8')
plt.imshow(a)


# In[18]:


df_x = data.iloc[:,1:]
df_y = data.iloc[:,0]


# In[22]:


x_train,x_test,y_train,y_test = train_test_split(df_x, df_y, test_size = 0.2, random_state=4)


# In[23]:


y_train.head()


# In[24]:


rf= RandomForestClassifier(n_estimators=100)


# In[25]:


rf.fit(x_train, y_train)


# In[26]:


pred = rf.predict(x_test)


# In[27]:


pred


# In[28]:


s = y_test.values

count = 0
for i in range(len(pred)):
    if pred[i] == s[i]:
        count = count +1


# In[32]:


count


# In[33]:


len(pred)


# In[31]:


8076/8400

