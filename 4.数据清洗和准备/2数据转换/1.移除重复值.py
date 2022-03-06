# encoding: utf-8
"""
@Project ：
@File: 1.移除重复值.py
@Author: liuwz
@time: 2022/1/16 7:18 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)

# duplicated 查看某行是否重复
print(data.duplicated())

"""drop_duplicates 返回去重后的DF"""
print(data.drop_duplicates())

# 根据指定列去重过滤 keep 表示是保留重复的第一个元素呢 还是保留最后一个元素呢
print(data.drop_duplicates(['k1', 'k2'], keep='last'))
# 如果根据k1过滤 那么后面的4行都要删除
print(data.drop_duplicates(['k1']))


