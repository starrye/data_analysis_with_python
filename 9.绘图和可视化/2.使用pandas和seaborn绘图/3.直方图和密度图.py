# encoding: utf-8
"""
@Project ：
@File: 3.直方图和密度图.py
@Author: liuwz
@time: 2022/3/13 3:26 下午
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import seaborn as sns


"""Series plot.hist 对值频率进行离散化显示的柱状图"""
tips = pd.read_csv("../../examples/tips.csv")
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])

# plot.hist为Series生成直方图
tips['tip_pct'].plot.hist(bins=50)
plt.show()

"""plot.density 连续概率分布的估计图 与直方图相比 是连续的曲线 也能看出数据分布"""
tips['tip_pct'].plot.density()
plt.show()

"""sns.distplot 同时绘制直方图和密度图"""
# comp1 = np.random.normal(0, 1, size=200)
# comp2 = np.random.normal(10, 2, size=200)
# values = pd.Series(np.concatenate([comp1, comp2]))

sns.distplot(tips['tip_pct'], bins=100, color='k')
plt.show()




