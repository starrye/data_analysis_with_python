# encoding: utf-8
"""
@Project ： 
@File: 3.分位数和桶分析.py
@Author: liuwz
@time: 2022/3/2 11:57 上午
@desc: 
"""

import pandas as pd
import numpy as np


frame = pd.DataFrame({'data1': np.random.randn(1000),
                      'data2': np.random.randn(1000)})

quartiles = pd.cut(frame.data1, 4)
print(quartiles[:10])


def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}


"""group 还能直接利用cut返回的Categories对象"""
grouped = frame.data2.groupby(quartiles)
print(grouped.apply(get_stats))

print(grouped.apply(get_stats).unstack())

grouping = pd.qcut(frame.data1, 10, labels=False)
print(pd.value_counts(grouping))
grouped = frame.data2.groupby(grouping)
print(grouped.apply(get_stats).unstack())