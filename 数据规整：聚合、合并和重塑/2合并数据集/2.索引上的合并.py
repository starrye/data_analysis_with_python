# encoding: utf-8
"""
@Project ： 
@File: 2.索引上的合并.py
@Author: liuwz
@time: 2022/2/11 6:44 下午
@desc: 
"""

import pandas as pd
import numpy as np

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                      'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

"""left_on + right_index  or  right_on + left_index"""
df1 = pd.merge(left1, right1, left_on='key', right_index=True)
print(df1)
