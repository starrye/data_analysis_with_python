# encoding: utf-8
"""
@Project ：
@File: 索引对象.py
@Author: liuwz
@time: 2022/1/3 5:07 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index

print(index)
print(index[1:])

# index不可修改
# index[1] = 'd'  # x

# index共享
labels = pd.Index(np.arange(1, 4))

print(labels)

objs = pd.Series([-1,2,-3], index=labels)
print(objs)

print(objs.index is labels)

# index可以存在重复元素
dup_lables = pd.Index(['foo', 'var', 'foo'])
print(dup_lables)

