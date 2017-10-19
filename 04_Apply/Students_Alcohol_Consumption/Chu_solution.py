#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:11:16 2017

@author: chumai
"""

import pandas as pd
import numbers as nb
#url = 'https://github.com/guipsamora/pandas_exercises/blob/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
#df = pd.read_csv(url, sep = ',', error_bad_lines= False, header = 1)

df = pd.read_csv('student-mat.csv', sep = ',')

df.info()

df.describe()

df.head()

df.columns

df.loc[:,'school':'guardian']

#def capitalizestring(x):
#    return x.upper()

capitalizestring = lambda x: x.upper()

#df[['Mjob', 'Fjob']]= df[['Mjob', 'Fjob']].astype(str)
#df[['Mjob', 'Fjob']]= df[['Mjob', 'Fjob']].apply(capitalizestring)

df['Mjob']= df['Mjob'].apply(capitalizestring)
df['Fjob']= df['Fjob'].apply(capitalizestring)

df.tail()

legal = lambda x: x>18

df['legal_drinker'] = df['age'].apply(legal)

df['legal_drinker2'] = df['age'].map(legal)

df = df * 10

#mult10 = lambda x: x*10 for isinstance(x, nb.Number)

def mult10(x):
    if isinstance(x, nb.Number):
        return x*10
    else:
        return x

df = df.applymap(mult10) # different from apply alone