# encoding: utf-8
"""
@Project ：
@File: 8.计算指标_哑变量.py
@Author: liuwz
@time: 2022/1/23 10:51 AM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# 将分类变量（categorical variable）转换为“哑变量”或“指标矩阵”。

'''有k个不同的值 生成一个k列矩阵 值只有0 和 1 且只有一个1'''
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b','d'],
                   'data1': range(7)})
print(df)
print(pd.get_dummies(df['key']))

# 为列加前缀
dummies = pd.get_dummies(df['key'], prefix='key')
# df_with_dummy = df[['data1']].join(dummies)
print(dummies)

"""暂未理解"""
