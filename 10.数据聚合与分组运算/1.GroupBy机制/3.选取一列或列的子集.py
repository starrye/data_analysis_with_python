# encoding: utf-8
"""
@Project ： 
@File: 3.选取一列或列的子集.py
@Author: liuwz
@time: 2022/2/22 6:15 下午
@desc: 
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})

# 注意[['xxx']]-> DF 和 ['xxx'] -> Series 得到的结果类型是不一样的
result = df.groupby(['key1', 'key2'])[['data2']]
print(result)
s_grouped = df.groupby(['key1', 'key2'])['data2']
print(s_grouped)


people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])

people.iloc[2:3, [1, 2]] = np.nan
print(people)

# 根据字典来构造分组,按列
mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f': 'orange'}
result = people.groupby(mapping, axis=1)
print(result.sum())

map_series = pd.Series(mapping)
result = people.groupby(map_series, axis=1)
print(result.sum())

# 如果依据python函数分组，那么任何被当作分组键的函数都会在各个索引值上调用一遍 然后把返回值当作分组名称 比如len 会对每一个index执行 然后把结果进行汇总
result = people.groupby(len).sum()
print(result)

# 函数 数组混合使用 这里的数组是和index关联的 先按照函数分组 然后再按照数组分组 形成多层次索引
key_list = ['one', 'two', 'three', 'two', 'two']
result = people.groupby([len, key_list]).sum()
print(result)