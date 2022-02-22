# encoding: utf-8
"""
@Project ：
@File: 唯一值、值计数以及成员资格.py
@Author: liuwz
@time: 2022/1/9 4:46 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

# 去重
unique = obj.unique()
print(unique)

# 排序
# unique.sort()
# print(unique)

# 统计每个值出现次数
print(obj.value_counts())
print(pd.value_counts(obj.values, sort=False))

# 判断值是否存在 返回seria
print(obj.isin(['c']))
print(obj[obj.isin(['c'])])

# Index 有方法 get_indexer 获取索引数组
to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['a', 'b'])
# 获取to_match元素在unique_vals的位置 找不到元素-1
print(pd.Index(unique_vals).get_indexer(to_match))

# apply函数是根据某个func结果 以矩阵的形式展示
data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                    'Qu2': [2, 3, 1, 2, 3],
                         'Qu3': [1, 5, 2, 4, 4]})
print(data)
print(data.apply(pd.value_counts).fillna(0))