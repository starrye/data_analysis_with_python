# encoding: utf-8
"""
@Project ： 
@File: 2.禁用分组键.py
@Author: liuwz
@time: 2022/3/2 11:53 上午
@desc: 
"""

import pandas as pd
import numpy as np

tips = pd.read_csv('../../examples/tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']


def top(df, n=5, column="tip_pct"):
    return df.sort_values(by=column)[-n:]

# group_keys=False 关闭分组索引(分组键)
result = tips.groupby('smoker', group_keys=False).apply(top)
result1 = tips.groupby('smoker', group_keys=True).apply(top)
print(result)
print(result1)
