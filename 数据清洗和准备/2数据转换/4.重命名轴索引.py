# encoding: utf-8
"""
@Project ：
@File: 4.重命名轴索引.py
@Author: liuwz
@time: 2022/1/17 11:34 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

"""map函数对轴索引修改"""
transform = lambda x: x[:4].upper()

# data.index = data.index.map(transform)
# print(data.index)

"""rename直接对索引重命名"""
# data = data.rename(columns=str.upper)
# print(data)
# rename可以结合字典 replace可以原地修改
data = data.rename(index={'Ohio': 'INDIANA'},
            columns={'three': 'peekaboo'})
print(data)
