# encoding: utf-8
"""
@Project ： 
@File: main.py
@Author: liuwz
@time: 2022/2/10 6:34 下午
@desc: 
"""

import pandas as pd
import numpy as np

"""
- pandas.merge可根据一个或多个键将不同DataFrame中的行连接起来。SQL或其他关系型数据库的用户对此应该会比较熟悉，因为它实现的就是数据库的join操作。
- pandas.concat可以沿着一条轴将多个对象堆叠到一起。
- 实例方法combine_first可以将重复数据拼接在一起，用一个对象中的值填充另一个对象中的缺失值。
"""


"""pd.merge"""
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})

# 交集（内连接） merge会将重复列名当作key df1和df2都有key 列
df3 = pd.merge(df1, df2, on='key')
# print(df3)


df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})

# 如果没有重叠的列 也可以指定两个df的列进行合并
df5 = pd.merge(df3, df4, left_on='lkey', right_on='rkey')
# print(df5)


# how 指定连接方式 inner(默认) 使用两个表都有的键 left 使用左表的键 right 右表 outer 所有键
df6 = pd.merge(df1, df2, how='left')
# print(df6)

"""多对多连接产生的行的笛卡尔积"""
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                    'data2': range(5)})
df7 = pd.merge(df1, df2, how='inner')
# print(df7)

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})
df8 = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print(df8)

"""suffixes 增加重叠列明的后缀 默认后缀是x y 比如 key2_x key2_y 不好辨认这个列属于哪个原列"""
df9 = pd.merge(left, right, on='key1', suffixes=('_left', '_right'))
# df9 = pd.merge(left, right, on='key1')
print(df9)
