# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:50:28 2018

@author:  7961159@qq.com 李欣.............
"""


import numpy as np
import pandas as pd
from sklearn.model_selection import ShuffleSplit

#import visuals as vs
 
# load the Boston housing dataset

data = pd.read_csv('housing.csv')
#print(data)
prices = data['MEDV']
features = data.drop('MEDV',axis = 1)

print(data.head())

