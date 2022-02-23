# encoding: utf-8
"""
@Project ： 
@File: 2.对分组进行迭代.py
@Author: liuwz
@time: 2022/2/22 5:54 下午
@desc: 
"""

import pandas as pd
import numpy as np

"""GroupBy 支持迭代 产生一组 二元元组"""
df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
for name, group in df.groupby('key1'):
    print(name)
    print(group)

# 多重键 第一个元素是键值组成的元组
for name, group in df.groupby(['key1','key2']):
    print(name)
    print(group)

# 转化为字典
pieces = dict(list(df.groupby('key1')))
print(pieces)

# groupby默认是在axis=0上分组的 那么对列分组
grouped = df.groupby(df.dtypes, axis=1)
for dtype, group in grouped:
    print(dtype)
    print(group)

