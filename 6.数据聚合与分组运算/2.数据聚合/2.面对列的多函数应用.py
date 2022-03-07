# encoding: utf-8
"""
@Project ： 
@File: 2.面对列的多函数应用.py
@Author: liuwz
@time: 2022/3/1 11:20 上午
@desc: 
"""

import pandas as pd
import numpy as np


tips = pd.read_csv('../../examples/tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

print(tips[:6])

"""对相同的列一次应用多个函数"""
grouped = tips.groupby(['day', 'smoker'])
grouped_pct = grouped['tip_pct']
print(grouped_pct.agg('mean'))  # = grouped_pct.mean()


def peak_to_peak(arr):
    return arr.max() - arr.min()

result = grouped_pct.agg(['mean', 'std', peak_to_peak])
# print(result)

# 重命名列名？ 只需要 使用一个二元组 前面为名字 后面为函数
result = grouped_pct.agg([('new_mean', 'mean'), ('new_std', 'std'), ('ptp', peak_to_peak)])
print(result)


"""对不同的列使用相同的聚合函数"""
funtions = ['count', 'mean', 'max']
#funtions = [('new_count','count'), ('new_mean', 'mean'), ('new_std', 'std')]

result = grouped['tip_pct', 'total_bill'].agg(funtions)
print(result)

"""对一列或者多列应用不同的聚合函数：字典映射"""
result = grouped.agg({'tip': 'max', 'size': 'sum'})
print(result)

result = grouped.agg({'tip_pct' : ['min', 'max', 'mean', 'std'],
             'size' : 'sum'})
print(result)
