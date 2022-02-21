# encoding: utf-8
"""
@Project ： 
@File: 4。使用DF的列进行索引.py
@Author: liuwz
@time: 2022/2/10 12:00 下午
@desc: 
"""

import pandas as pd
import numpy as np

frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two',
                            'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3]})

print(frame)


"""set_index函数会将其一个或多个列转化为行索引，并返回一个新的df"""

# c重复值会合并
frame1 = frame.set_index(['c', 'd'])
print(frame1)

# drop=false 保留原列
frame2 = frame.set_index(['c', 'd'], drop=False)
print(frame2)


"""reset_index 和set_index相反 层次化索引的级别会被转移到列里面"""
frame3 = frame1.reset_index()
print(frame3)