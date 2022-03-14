# encoding: utf-8
"""
@Project ： 
@File: 3.将宽格式旋转为长格式.py
@Author: liuwz
@time: 2022/2/21 8:21 下午
@desc: 
"""

import pandas as pd
import numpy as np


df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})
print(df)
"""melt: 合并多个列为一个新的DF"""
melted = pd.melt(df, ['key'])
print(melted)

reshaped = melted.pivot('key', 'variable', 'value')
print(reshaped)


result = reshaped.reset_index()
print(result)

result1 = pd.melt(df, id_vars=['key'], value_vars=['A', 'B'])
result2 = pd.melt(df, value_vars=['A', 'B', 'C'])
print(result1)
print(result2)

result3 = pd.melt(df, value_vars=['key', 'A', 'B'])
print(result3)