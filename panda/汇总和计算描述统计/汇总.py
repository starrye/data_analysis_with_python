# encoding: utf-8
"""
@Project ：
@File: 汇总.py
@Author: liuwz
@time: 2022/1/5 11:36 PM
@desc:
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
print(df)

# DF sum对列求和返回Series
print(df.sum())
# 行求和
print(df.sum(axis=1))

# 均值 NA会被忽略(排除缺失值) 可以通过skipna禁用选项 意思就是设置False 则表示有Na值会使和为Na则均值也为Na
print(df.mean(axis=1, skipna=False))

# 返回max/min值的索引
print(df.idxmax())
print(df.idxmin())

# 对行累计求和
print(df.cumsum())

# 多项汇总 包含 count max min std...
print(df.describe())

# Series 多项汇总 包含 count unique top...
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj.describe())
