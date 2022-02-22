# encoding: utf-8
"""
@Project ：
@File: 整数索引.py
@Author: liuwz
@time: 2022/1/3 6:31 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 整数索引请使用loc 和iloc
ser = pd.Series(np.arange(3.))
print(ser)
# 报错
# print(ser[-1])
print(ser[:1])
# loc索引包含末端
print(ser.loc[:1])
# iloc索引不包含末端
print(ser.iloc[:1])
