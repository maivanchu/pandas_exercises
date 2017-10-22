
# coding: utf-8

# # US - Baby Names

# ### Introduction:
# 
# We are going to use a subset of [US Baby Names](https://www.kaggle.com/kaggle/us-baby-names) from Kaggle.  
# In the file it will be names from 2004 until 2014
# 
# 
# ### Step 1. Import the necessary libraries

# In[1]:

import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/Stats/US_Baby_Names/US_Baby_Names_right.csv). 

# ### Step 3. Assign it to a variable called baby_names.

# In[13]:

baby_names = pd.read_csv('US_Baby_Names_right.csv')


# ### Step 4. See the first 10 entries

# In[16]:

baby_names.head(10)


# ### Step 5. Delete the column 'Unnamed: 0' and 'Id'

# In[11]:

del baby_names['Id']


# In[9]:

baby_names.drop('Unnamed: 0', axis = 1, inplace = True)


# In[15]:

baby_names.drop(['Unnamed: 0', 'Id'], axis = 1, inplace = True)


# ### Step 6. Is there more male or female names in the dataset?

# In[18]:

baby_names['Gender'].value_counts()

baby_names['Gender'].value_counts()['F']
# ### Step 7. Group the dataset by name and assign to names

# In[23]:

baby_names.shape


# In[25]:

baby_names['Name'].unique().shape


# In[20]:

names = baby_names.groupby(by = 'Name').sum()
names.drop('Year', axis = 1, inplace = True)

# In[28]:

names.size


# In[22]:

names.head()

# ### Step 8. How many different names exist in the dataset?

# In[ ]:


baby_names['Name'].unique().shape
# ### Step 9. What is the name with most occurrences?

# In[ ]:
names['Count'].max()

names['Count'].idxmax()


names[ names['Count'] == names['Count'].max() ]
#baby_names['Name'].value_counts().head(10)

# ### Step 10. How many different names have the least occurrences?

# In[ ]:
#df = baby_names['Name'].value_counts().sort_values(ascending = True)
#df.loc[df == df.min()].shape[0]
       
names[ names['Count'] == names['Count'].min() ].shape[0]
# ### Step 11. What is the median name occurrence?

# In[ ]:

names[ names['Count'] == names['Count'].median() ]

#df.median()
#df.describe()['50%']

# ### Step 12. What is the standard deviation of names?

# In[ ]:

#df.describe()['std'].round()
#df.std().round()
names['Count'].std()

# ### Step 13. Get a summary with the mean, min, max, std and quartiles.

# In[ ]:


names.describe()
