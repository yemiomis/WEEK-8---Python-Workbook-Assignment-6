#!/usr/bin/env python
# coding: utf-8

# In[77]:


import pandas as pd


# In[78]:


df = pd.read_csv(r"C:\Users\Envy 360\Desktop\learn-data-analysis-w-python-master\learn-data-analysis-w-python-master\datasets\gradedata.csv")


# In[79]:


df.head()


# In[80]:


import statsmodels.formula.api as sm


# In[84]:


df['gender_changed']=df.gender.map({'female': 1, 'male':0})


# In[85]:


df.head()


# In[86]:


result = sm.ols(formula='grade ~ exercise + hours + gender_changed',data=df).fit()


# In[87]:


result.summary()


# In[88]:


result = sm.ols(formula='grade ~ exercise + hours ',data=df).fit()


# In[89]:


result.summary()


# 

# In[ ]:


# no the R2 remains the same 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




