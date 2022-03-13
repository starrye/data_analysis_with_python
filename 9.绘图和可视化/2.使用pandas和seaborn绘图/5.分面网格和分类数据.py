# encoding: utf-8
"""
@Project ：
@File: 5.分面网格和分类数据.py
@Author: liuwz
@time: 2022/3/13 4:22 下午
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import seaborn as sns

"""sns.factorplot 使用额外的分组维度"""
tips = pd.read_csv("../../examples/tips.csv")
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])


sns.factorplot(x='day', y='tip_pct', hue='time', col='smoker',
              kind='bar', data=tips[tips.tip_pct < 1])
plt.show()

sns.factorplot(x='day', y='tip_pct', row='time', col='smoker',
              kind='bar', data=tips[tips.tip_pct < 1])
plt.show()