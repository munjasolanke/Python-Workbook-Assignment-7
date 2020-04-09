#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Python Workbook Assignment 7-1
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades'])
df.head()


# In[6]:


import matplotlib.pyplot as plt
plt.plot('Names','Grades',data=df)
y= df['Grades'][df['Names']=='Bob']
plt.annotate('Wow!',xy=('Bob',y.values),xytext=(y.index.values+0.4,y.values),arrowprops=dict(facecolor='black',shrink=0.05))
plt.show()


# In[ ]:




