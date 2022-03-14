# encoding: utf-8
"""
@Project ：
@File: 3.替换值.py
@Author: liuwz
@time: 2022/1/16 7:34 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = pd.Series([1., -999., 2., -999., -1000., 3.])

"""replace 替换产生新的Series 和python内置的replace相似"""
data_new = data.replace(-999, np.nan)
print(data_new)

# 一次替换多个值
data_new = data.replace([-999, -1000], np.nan)
print(data_new)

# 多个值替换多个值
data_new = data.replace([-999, -1000], [np.nan, 0])
print(data_new)

# 也可以是个字典
data_new = data.replace({-999: np.nan, -1000: 0})
print(data_new)



