# encoding: utf-8
"""
@Project ：
@File: 1.main.py
@Author: liuwz
@time: 2022/1/16 6:48 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])

print(string_data)
# isna isnull 没有区别
print(string_data.isna())

# python内置的None 也是NaN
string_data[0] = None
print(string_data.isna())

# string_data = string_data.dropna()
# inplace 原地操作
# string_data.dropna(inplace=True)
# ffill 填充和前面的值一样 bfill 和后面
string_data.bfill(inplace=True)
print(string_data)
