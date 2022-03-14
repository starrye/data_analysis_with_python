# encoding: utf-8
"""
@Project ：
@File: 1.main.py
@Author: liuwz
@time: 2022/2/28 11:46 上午
@desc:
"""

import pandas as pd
import numpy as np


df = pd.DataFrame({'data1': np.random.randn(5),
                  'data2': np.random.randn(5),
                   'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one']})

print(df)

"""quantile 计算分位数 何为分位数 即通过一个值 将数据分成两类,这个基准值就是分位数"""
grouped = df.groupby('key1')
print(grouped['data1'])
result = grouped['data1'].quantile(0.9)
print(result)

"""aggregate 使用自己的聚合函数"""
def peak_to_peak(arr):
    return arr.max() - arr.min()
result = grouped.aggregate(peak_to_peak)
print(result)

result = grouped.describe()
print(result)