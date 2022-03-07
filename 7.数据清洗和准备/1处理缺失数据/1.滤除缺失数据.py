# encoding: utf-8
"""
@Project ：
@File: 1.滤除缺失数据.py
@Author: liuwz
@time: 2022/1/16 6:58 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy import nan as NA


data = pd.Series([1, NA, 3.5, NA, 7])
# 结果一致
# print(data.dropna())
# print(data[data.notnull()])


data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
                     [NA, NA, NA], [NA, 6.5, 3.]])
print(data)

# 删除含有NaN的行
cleaned = data.dropna()
print(cleaned)

# 参数how = 'all' 可以只丢弃完全是NaN的行
cleaned1 = data.dropna(how='all')
print(cleaned1)

data[2] = None
cleaned2 = data.dropna(axis=1, how='all')
print(cleaned2)

# 如果你觉得行中非NaN值不超过一定个数 就有必要留下
"""thresh 只要非NaN值不超过这个值 行就会被留下"""
cleaned3 = data.dropna(thresh=1)
print(cleaned3)

