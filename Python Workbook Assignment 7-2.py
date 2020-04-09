#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Python Workbook Assignment 7-2
import matplotlib.pyplot as plt
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grades = [76,95,77,78,99]
GradeList = zip(status,grades)
df = pd.DataFrame(data = GradeList,columns=['Status', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')


# In[6]:


df2 = df.set_index(df['Status'])
df2.plot(kind="bar")

