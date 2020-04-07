#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd


# In[47]:


names = ['Bob','Jessica','Mary','John','Mel','Sam','Cathy','Henry','Lloyd']


# In[48]:


grades = [76,95,77,78,99,84,79,100,73]


# In[49]:


bs = [1,1,0,0,1,1,1,0,1]


# In[50]:


ms = [2,1,0,0,0,1,1,0,0]


# In[51]:


phd = [0,1,0,0,0,2,1,0,0]


# In[52]:


GradeList = zip(names,grades,bs,ms,phd)


# In[53]:


df = pd.DataFrame(data=GradeList,columns=['Names','Grades','BS','MS','PhD'])


# In[54]:


df


# In[55]:


df.loc[df['PhD']==0]['MS'].mean()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




