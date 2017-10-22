
# coding: utf-8

# # Housing Market

# ### Introduction:
# 
# This time we will create our own dataset with fictional numbers to describe a house market. As we are going to create random data don't try to reason of the numbers.
# 
# ### Step 1. Import the necessary libraries

# In[ ]:



import pandas as pd
import numpy as np
# ### Step 2. Create 3 differents Series, each of length 100, as follows: 
# 1. The first a random number from 1 to 4 
# 2. The second a random number from 1 to 3
# 3. The third a random number from 10,000 to 30,000

# In[ ]:

s1 = pd.Series( np.random.randint(1,4, size = 100))
s2 = pd.Series( np.random.randint(1,3, size = 100))
s3 = pd.Series( np.random.randint(10000,30000, size = 100))



# ### Step 3. Let's create a DataFrame by joinning the Series by column

# In[ ]:

df = pd.concat([s1,s2,s3], axis = 1)
#df = pd.concat([s1,s2,s3], axis = 1, joint = 'inner')
# ### Step 4. Change the name of the columns to bedrs, bathrs, price_sqr_meter

# In[ ]:

df.columns = ['bedrs', 'bathrs', 'price_sqr_meter']


# ### Step 5. Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'

# In[ ]:

df2 = pd.concat([s1,s2,s3], axis = 0)


# ### Step 6. Ops it seems it is going only until index 99. Is it true?

# In[ ]:

df2.index


# ### Step 7. Reindex the DataFrame so it goes from 0 to 299

# In[ ]:

df2 = pd.concat([s1,s2,s3], axis = 0, ignore_index = True)

