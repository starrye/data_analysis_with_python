# encoding: utf-8
"""
@Project ： 
@File: 1.重排和分级排序.py
@Author: liuwz
@time: 2022/2/8 4:44 下午
@desc: 
"""

import pandas as pd
import numpy as np

"""调整某条轴上各级别的顺序，或根据指定级别上的值对数据进行排序"""

"""swaplevel 互换"""
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])

frame.index.names = ['key1', 'key2']
frame = frame.swaplevel(0, 1)
print(frame)

"""sort_index 根据值对数据进行排序"""
frame1 = frame.sort_index(level=1)
print(frame1)

