# encoding: utf-8
"""
@Project ： 
@File: 11.带有重复标签的轴索引.py
@Author: liuwz
@time: 2022/1/4 7:45 下午
@desc: 
"""

import pandas as pd
import numpy as np

# Series
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj)

# is_unique 查看索引是否唯一
print(obj.index.is_unique)

# 重复索引返回一个Series
print(obj['a'])


# DF
df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(df.loc['a'])