# encoding: utf-8
"""
@Project ：
@File: 10.排序和排名.py
@Author: liuwz
@time: 2022/1/4 4:54 下午
@desc:
"""

import pandas as pd
import numpy as np

# Series的排序
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
# 按照index or values排序 NaN值会排到最后
print(obj.sort_index())
print(obj.sort_values())

# DF的排序
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
# index排序
print(frame.sort_index())
# 降序
print(frame.sort_index(axis=1, ascending=False))
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
# values排序 by 按照列值排序
print(frame.sort_values(by='b'))
print(frame.sort_values(by=['a', 'b']))
print('-' * 30)


# Series排名
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank(method="first"))  # 根据值在原数据中出现的顺序给出排名 先出现的排在前面 从小到大
print(obj.rank(ascending=False, method='max'))  # 降序

# DF排名
frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]})
# 列排序
print(frame.rank(axis='columns'))


