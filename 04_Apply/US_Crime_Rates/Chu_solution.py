#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 22:06:06 2017

@author: chumai
"""

import pandas as pd

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv'

crime = pd.read_csv(url, sep = ',')

crime.head(10)

crime.dtypes

crime.describe()

crime.info()


crime['Year'] = pd.to_datetime(crime['Year'], format = '%Y')


crime.set_index('Year', inplace = True)

crime.drop('Total', axis = 1, inplace = True)

del crime['Total']


crimes = crime.resample('10AS').sum()

crimes['Population'] = crime.resample('10AS')['Population'].max()


crimes.idxmax(axis=0)
crimes.idxmin(axis=0)

ratio = crimes.iloc[:,1:].div(crimes['Population'], axis= 0)
ratio.idxmax(axis=0)
ratio.idxmin(axis=0)