# encoding: utf-8
"""
@Project ： 
@File: 1.main.py
@Author: liuwz
@time: 2022/2/8 4:45 下午
@desc: 
"""

import pandas as pd
import numpy as np

data = pd.Series(np.random.randn(9),
                 index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                        [1, 2, 3, 1, 3, 1, 2, 2, 3]])

# print(data.index)
# 通过索引读取元素的几种方式
print(data['b'])
print(data['b':'c'])
print(data.loc[['b', 'c']])


"""unstack可以将Series数据安排到一个DataFrame中"""
print(data.unstack())
"""stack可以将DF数据安排到一个Series中"""
print(data.unstack().stack())



frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])
frame.index.names = ['key1', 'key2']
print(frame['Ohio'])
print(frame.loc['a'])

