# encoding: utf-8
"""
@Project ：
@File: 丢弃指定轴上的项.py
@Author: liuwz
@time: 2022/1/3 5:29 PM
@desc:
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
# drop 删除行(索引)
obj2 = obj.drop('c')
print(obj2)

# drop 批量删除行
obj3 = obj.drop(['a', 'd'])
print(obj3)

# DataFrame drop删除行用法和Series一样
data = pd.DataFrame(
    np.arange(16).reshape(
        (4, 4)), index=[
            'Ohio', 'Colorado', 'Utah', 'New York'], columns=[
                'one', 'two', 'three', 'four'])
print(data)

data2 = data.drop(['Colorado', 'Utah'])
print(data2)

# 通过axis=1 or axis=columns删除列
data3 = data.drop(['two', 'four'], axis=1)
print(data3)

# inplace 原地修改对象 无法撤回
data.drop('Ohio', inplace=True)
print(data)
