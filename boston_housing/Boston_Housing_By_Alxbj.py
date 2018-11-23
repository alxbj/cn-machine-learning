# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:50:28 2018
@author:  7961159@qq.com alxbj.............
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import ShuffleSplit
 # load the Boston housing dataset
data = pd.read_csv('housing.csv')
"""特征 'RM'， 'LSTAT'，和 'PTRATIO'，给我们提供了每个数据点的数量相关的信息。
目标变量：'MEDV'，是我们希望预测的变量。
他们分别被存在 features 和 prices 两个变量名中。
"""
prices = data['MEDV']
features = data.drop('MEDV',axis = 1)
print("Boston housing dataset has {} data points with {} variables each.".format(*data.shape))

"""编程训练"""
#  Minimum price of the data
minimum_price = np.min(prices)

#  Maximum price of the data
maximum_price = np.max(prices)

#  Mean price of the data
mean_price = np.mean(prices)

#  Median price of the data
median_price = np.median(prices)

#  Standard deviation of prices of the data
std_price = np.std(prices)

# Show the calculated statistics
print("Statistics for Boston housing dataset:\n")
print("Minimum price: ${:.2f}".format(minimum_price)) 
print("Maximum price: ${:.2f}".format(maximum_price))
print("Mean price: ${:.2f}".format(mean_price))
print("Median price ${:.2f}".format(median_price))
print("Standard deviation of prices: ${:.2f}".format(std_price))
