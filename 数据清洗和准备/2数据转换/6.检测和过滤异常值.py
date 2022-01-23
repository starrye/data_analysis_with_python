# encoding: utf-8
"""
@Project ：
@File: 6.检测和过滤异常值.py
@Author: liuwz
@time: 2022/1/23 10:22 AM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe())

col = data[2]
print(col[np.abs(col) > 3])

# 含有超过3或者-3的值的行 any 是指任一列超过3就把行选取
print(data[(np.abs(data) > 3).any(1)])

# sign: <0:-1 0:0 >0:1
data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())

