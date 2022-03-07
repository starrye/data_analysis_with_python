# encoding: utf-8
"""
@Project ：
@File: 2.填充缺失数据.py
@Author: liuwz
@time: 2022/1/16 7:09 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

"""fillna"""
df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = None
df.iloc[:2, 2] = None
print(df)

# print(df.fillna(0))
# 传入字典可以填充指定列
# print(df.fillna(({1: 0.5, 2: 1.0})))

print(df.fillna(method='bfill', limit=2))

data = pd.Series([1, None, 3.5, None, 7])
# 填充平均值
print(data.fillna(data.mean()))


