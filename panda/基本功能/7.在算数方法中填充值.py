# encoding: utf-8
"""
@Project ：
@File: 7.在算数方法中填充值.py
@Author: liuwz
@time: 2022/1/3 6:50 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
# 如何填充空值
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
# 产生空值
df3 = df1 + df2
print(df3)

# add方法 fill_value 先填充再进行add  ！！
df4 = df1.add(df2, fill_value=0)

print(df1)
df5 = df1.reindex(columns=df2.columns, fill_value=0)
print(df5)

