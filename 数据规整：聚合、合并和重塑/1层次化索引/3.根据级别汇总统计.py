# encoding: utf-8
"""
@Project ： 
@File: 3.根据级别汇总统计.py
@Author: liuwz
@time: 2022/2/10 11:51 上午
@desc: 
"""

import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

print(frame)

"""groupby+sum 对轴求和"""
print(frame.groupby(level='key2').sum())
print(frame.groupby(level='color', axis=1).sum())


