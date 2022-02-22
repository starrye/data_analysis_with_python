# encoding: utf-8
"""
@Project ： 
@File: 2.将长格式旋转为宽格式.py
@Author: liuwz
@time: 2022/2/21 6:10 下午
@desc: 
"""

import pandas as pd
import numpy as np


data = pd.read_csv('../../examples/macrodata.csv')
print(data.head())

periods = pd.PeriodIndex(year=data.year, quarter=data.quarter,
                         name='date')
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)
data.index = periods.to_timestamp('D', 'end')
ldata = data.stack().reset_index().rename(columns={0: 'value'})
print(ldata)

# 前两个值分别用作行和列索引 第三个值为数据列
pivoted = ldata.pivot('date', 'item', 'value')

ldata['values2'] = np.random.randn(len(ldata))
print(ldata)
pivoted = ldata.pivot('date', 'item')
print(pivoted['value'][:5])

unstacked = ldata.set_index(['date', 'item']).unstack('item')
print(unstacked[:7])
