# encoding: utf-8
"""
@Project ： 
@File: 4.实例:用特定于分组的值填充缺失值.py
@Author: liuwz
@time: 2022/3/2 8:55 下午
@desc: 
"""

import pandas as pd
import numpy as np


s = pd.Series(np.random.randn(6))
s[::2] = np.nan
print(s)

s = s.fillna(s.mean())
print(s)


states = ['Ohio', 'New York', 'Vermont', 'Florida',
          'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = pd.Series(np.random.randn(8), index=states)
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
print(data)
result = data.groupby(group_key).mean()
print(result)

"""apply 应用匿名函数 使用分组平均值"""
fill_mean = lambda g: g.fillna(g.mean())
result = data.groupby(group_key).apply(fill_mean)
print(result)


fill_values = {'East': 0.5, 'West': -1}
fill_func = lambda g: g.fillna(fill_values[g.name])
result1 = data.groupby(group_key).apply(fill_func)
print(result1)

