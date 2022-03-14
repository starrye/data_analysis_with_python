# encoding: utf-8
"""
@Project ： 
@File: 3.以'没有行索引'的形式返回聚合数据.py
@Author: liuwz
@time: 2022/3/1 11:41 上午
@desc: 
"""

import pandas as pd
import numpy as np


tips = pd.read_csv('../../examples/tips.csv')
"""as_index=False 取消索引 使用默认数字索引"""
result = tips.groupby(['day', 'smoker'], as_index=False).mean()
result1 = tips.groupby(['day', 'smoker'], as_index=True).mean()
print(result)
print(result1)
