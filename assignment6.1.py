#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd


# In[64]:


df = pd.read_csv(r"C:\Users\Envy 360\Desktop\learn-data-analysis-w-python-master\learn-data-analysis-w-python-master\datasets\gradedata.csv")


# In[65]:


df.head()


# In[66]:


df = df.sort_values(by='age', ascending=0)


# In[67]:


df.head()


# In[72]:


df = df.sort_values(by=['fname','age', 'grade'])


# In[71]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




