
# coding: utf-8

# # Ex2 - Filtering and Sorting Data

# This time we are going to pull data directly from the internet.
# 
# ### Step 1. Import the necessary libraries

# In[1]:

import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/jokecamp/FootballData/master/Euro%202012/Euro%202012%20stats%20TEAM.csv). 

# ### Step 3. Assign it to a variable called euro12.

# In[ ]:
url = 'https://raw.githubusercontent.com/jokecamp/FootballData/master/Euro%202012/Euro%202012%20stats%20TEAM.csv'
euro12 = pd.read_csv(url)

euro12.info()
#%%
euro12.head()
euro12.columns.tolist()

euro12.columns.sort_values().tolist()

#%%


# ### Step 4. Select only the Goal column.

# In[ ]:

euro12['Goals']


# ### Step 5. How many team participated in the Euro2012?

# In[ ]:

euro12['Team'].size

euro12.shape[0]
# ### Step 6. What is the number of columns in the dataset?

# In[ ]:

euro12.shape[1]


# ### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

# In[ ]:

discipline = euro12[['Team','Yellow Cards', 'Red Cards']]


# ### Step 8. Sort the teams by Red Cards, then to Yellow Cards

# In[ ]:

discipline.sort_values(by = ['Red Cards','Yellow Cards' ], ascending = True)

discipline.sort_values(by = ['Red Cards','Yellow Cards' ], ascending = False)

discipline.sort_values(by = ['Red Cards','Yellow Cards' ], ascending = [True, False])


# ### Step 9. Calculate the mean Yellow Cards given per Team

# In[ ]:

discipline.mean()
discipline.mean().apply(round)


# ### Step 10. Filter teams that scored more than 6 goals

# In[ ]:


euro12[ euro12['Goals'] > 6  ][['Team','Goals']]

# ### Step 11. Select the teams that start with G

# In[ ]:


euro12 [ euro12['Team'].str.startswith('G') ]['Team']

# ### Step 12. Select the first 7 columns

# In[ ]:

euro12.columns[0:7]

euro12[  euro12.columns[0:7] ]

euro12.iloc[:, 0:7]
# ### Step 13. Select all columns except the last 3.

# In[ ]:

euro12.columns[:-3]
euro12.iloc[:, 0:-3]
euro12.iloc[:, :-3]
# ### Step 14. Present only the Shooting Accuracy from England, Italy and Russia

# In[ ]:

euro12[euro12['Team'].isin(['England','Italy', 'Russia']) ][['Team','Shooting Accuracy']]
euro12[euro12['Team'] == 'England'][['Team','Shooting Accuracy']]
