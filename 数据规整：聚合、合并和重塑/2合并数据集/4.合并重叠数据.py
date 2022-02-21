# encoding: utf-8
"""
@Project ： 
@File: 4.合并重叠数据.py
@Author: liuwz
@time: 2022/2/21 11:34 上午
@desc: 
"""

import pandas as pd
import numpy as np

a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a), dtype=np.float64),
              index=['f', 'e', 'd', 'c', 'b', 'a'])

result = np.where(pd.isnull(a), b, a)
print(result)

"""combine_first: 用传递对象中的数据填补调用对象中缺失的数据"""
result1 = b[:-2].combine_first(a)
print(result1)

# 也可用于DF数据的合并

df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],
                    'b': [np.nan, 2., np.nan, 6.],
                    'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],
                    'b': [np.nan, 3., 4., 6., 8.]})

df3 = df1.combine_first(df2)
df4 = df2.combine_first(df1)
print(df3)
print(df4)