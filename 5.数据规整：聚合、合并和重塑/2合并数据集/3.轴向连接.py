# encoding: utf-8
"""
@Project ： 
@File: 轴向连接.py
@Author: liuwz
@time: 2022/2/16 6:26 下午
@desc: 
"""

import pandas as pd
import numpy as np

arr = np.arange(12).reshape((3, 4))

arr1 = np.concatenate([arr, arr], axis=1)
print(arr1)

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
"""concat axis=1转化为pd axis=0为Series"""
s4 = pd.concat([s1, s3])
s5 = pd.concat([s1, s2, s3], axis=1)
print(s4)
print(s5)

# join 连接方式
s6 = pd.concat([s1, s4], axis=1, join='inner')
print(s6)

# 额外创建一个层次化索引
result = pd.concat([s1, s1, s3], keys=['one','two', 'three'])
print(result)
print(result.unstack())

result1 = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'], axis=1)
print(result1)


df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                   columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                   columns=['three', 'four'])

df3 = pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])
print(df3)

"""如果传入的不是列表而是一个字典，则字典的键就会被当做keys选项的值"""
df4 = pd.concat({'level1': df1, 'level2': df2}, axis=1)
print(df4)

df5 = pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
          names=['upper', 'lower'])
print(df5)


df6 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'], index=['x', 'y', 'z'])
df7 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'], index=['x', 'y'])
# ignore_index ： 忽略索引
df8 = pd.concat([df6, df7], axis=0, ignore_index=True)
print(df8)

