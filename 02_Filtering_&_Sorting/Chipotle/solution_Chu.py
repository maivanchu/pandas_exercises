#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:39:34 2017

@author: chumai
"""

#%%
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10.0, 8.0)
#%%
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep = '\t')
#%%
chipo.head(10)
#%%
chipo.info()
#%%
chipo['price'] = chipo['item_price'].str.replace('$','')
chipo['price']  = chipo['price'].astype('float')
#%%
chipo.loc[ chipo['price'] > 10.0 ].shape[0]
#%%
len(chipo.loc[ chipo['price'] > 10.0 ])
#%%
len(chipo[ chipo['price'] > 10.0 ])


#%%
#chipo[['item_name', 'price']]
chipo.drop_duplicates(subset = ['item_name', 'price']).loc[ chipo['quantity'] == 1, ['item_name', 'price']]
#%%
#chipo[['item_name', 'price']].sort_values(by = 'item_name', ascending = True)
chipo.drop_duplicates(subset = ['item_name', 'price']).loc[ chipo['quantity'] == 1, ['item_name', 'price']].sort_values(by = 'item_name', ascending = True)
#%%
chipo.iloc[ chipo['price'].argmax()] 
#%%
chipo[['item_name', 'quantity', 'price']].sort_values(by = 'item_name', ascending = True)
#%%
chipo.groupby('item_name')['quantity'].count().loc['Veggie Salad Bowl']
#%%
chipo[ chipo['item_name'] == 'Veggie Salad Bowl' ].count()
len(chipo[ chipo['item_name'] == 'Veggie Salad Bowl' ])
#%%
chipo[ (chipo['item_name'] == 'Canned Soda' ) & (chipo['quantity'] > 1) ].count()
#%%
len(chipo[ (chipo['item_name'] == 'Canned Soda' ) & (chipo['quantity'] > 1) ])
#%%

#%%