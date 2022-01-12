# encoding: utf-8
"""
@Project ：
@File: 逐块读取文本文件.py
@Author: liuwz
@time: 2022/1/11 11:44 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

"""读取大文件"""


result = pd.read_csv('../../examples/ex6.csv')
print(result)

# 指定读取前5行(避免读取整个文件)
cs2 = pd.read_csv('../../examples/ex6.csv', nrows=5)
print(cs2)


"""逐块读取文件 chunksize 返回TextParser对象 需要迭代"""
cs3 = pd.read_csv('../../examples/ex6.csv', chunksize=1000)
# TextParser有get_chunk方法可以读取任一大小块数据
print(cs3.get_chunk(10))
tot = pd.Series([], dtype=float)
for piece in cs3:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)
print(tot)
