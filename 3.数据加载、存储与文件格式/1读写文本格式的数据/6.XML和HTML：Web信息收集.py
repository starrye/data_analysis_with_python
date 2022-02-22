# encoding: utf-8
"""
@Project ：
@File: 6.XML和HTML：Web信息收集.py
@Author: liuwz
@time: 2022/1/12 11:21 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

tables = pd.read_html('../../examples/fdic_failed_bank_list.html')

failures = tables[0]
print(failures.info())

# to_datetime 转化为time用于计算 May 3, 2001 -> 2001-05-03
close_timestamps = pd.to_datetime(failures['Closing Date'])
# 按年份计算倒闭的银行数
print(close_timestamps.dt.year.value_counts())

