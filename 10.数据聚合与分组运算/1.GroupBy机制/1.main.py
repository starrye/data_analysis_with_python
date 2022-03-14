# encoding: utf-8
"""
@Project ： 
@File: 1.GroupBy机制.py
@Author: liuwz
@time: 2022/2/22 5:18 下午
@desc: 
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
print(df)

"""groupby 产生一个对象 可以调用函数进行运算"""
grouped = df['data1'].groupby(df['key1'])
print(grouped.mean())

# 传入多个对象进行分组
means = df['data1'].groupby([df['key1'], df['key2']]).mean()
print(means)
print(means.unstack())

# 分组对象也可以是任何长度的数组（不在原DF中）
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
result = df['data1'].groupby([states, years]).mean()
print(result)

result = df.groupby('key1').mean() # 这里没有key2 因为key2不是数值列 所以被排除了
result = df.groupby(['key1', 'key2']).mean()
print(result)

"""size 返回分组大小"""
size = df.groupby(['key1', 'key2']).size()
print(size)
