
# coding: utf-8

# # MPG Cars

# ### Introduction:
# 
# The following exercise utilizes data from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Auto+MPG)
# 
# ### Step 1. Import the necessary libraries

# In[ ]:


import pandas as pd

# ### Step 2. Import the first dataset [cars1](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/Merge/Auto_MPG/cars1.csv) and [cars2](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/Merge/Auto_MPG/cars2.csv).  

#    ### Step 3. Assign each to a to a variable called cars1 and cars2

# In[ ]:

cars1 = pd.read_csv('cars1.csv')

cars2 = pd.read_csv('cars2.csv')
# ### Step 4. Ops it seems our first dataset has some unnamed blank columns, fix cars1

# In[ ]:

for k in range(9,14):
    print('k = %d'%k)
    print(cars1['Unnamed: '+ '%d'%k].unique())

cars1.dropna(axis = 1, how = 'all', inplace = True)
# ### Step 5. What is the number of observations in each dataset?

# In[ ]:

cars1.shape

cars2.shape

# ### Step 6. Join cars1 and cars2 into a single DataFrame called cars

# In[ ]:

cars = pd.concat([cars1, cars2], axis = 0, ignore_index = True)


# ### Step 7. Ops there is a column missing, called owners. Create a random number Series from 15,000 to 73,000.

# In[ ]:
import numpy as np
owners = pd.Series(data = np.random.randint(15000, high = 73000, size = cars.shape[0] ))
owners.name = 'owners'

# ### Step 8. Add the column owners to cars

# In[ ]:

cars = pd.concat([cars,owners], axis = 1)

#%% fastest way to add a column to a dataframe
cars['owners'] = np.random.randint(15000, high = 73000, size = cars.shape[0] )


