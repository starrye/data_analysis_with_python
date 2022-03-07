# encoding: utf-8
"""
@Project ：
@File: 算数运算和数据对齐.py
@Author: liuwz
@time: 2022/1/3 6:40 PM
@desc:
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Series
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
# 基于索引相加
s3 = s1 + s2
print(s3)

# DataFrame
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# 可以不同结构的DataFrame相加 自动按照索引对齐
df3 = df1 + df2
print(df3)

