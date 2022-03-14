# encoding: utf-8
"""
@Project ： 
@File: 1.main.py
@Author: liuwz
@time: 2022/3/2 11:20 上午
@desc: 
"""

import pandas as pd
import numpy as np


tips = pd.read_csv('../../examples/tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']


def top(df, n=5, column="tip_pct"):
    return df.sort_values(by=column)[-n:]


"""apply 在分组后应用统计函数"""
result = top(tips, n=5)
print(result)

result = tips.groupby('smoker').apply(top)
print(result)

"""如果传给apply的函数能够接受其他参数或关键字，则可以将这些内容放在函数名后面一并传入"""
result = tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill')
print(result)

