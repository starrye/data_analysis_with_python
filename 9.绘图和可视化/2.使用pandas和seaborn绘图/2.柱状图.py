# encoding: utf-8
"""
@Project ：
@File: 2.柱状图.py
@Author: liuwz
@time: 2022/3/6 5:30 下午
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

"""
bar():  水平的柱状图 
barh(): 垂直的柱状图
"""

# Series
fig, axes = plt.subplots(2, 1)
data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
data.plot.bar(ax=axes[0], color='k', alpha=0.7)
data.plot.barh(ax=axes[1], color='k', alpha=0.7)
plt.show()

# DF
df = pd.DataFrame(np.random.rand(6, 4),
                  index=['one', 'two', 'three', 'four', 'five', 'six'],
                  columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))

# print(df)
df.plot.bar()
plt.show()
# 设置stacked=True可以生成堆积柱状图
df.plot.barh(stacked=True, alpha=0.5)
plt.show()

tips = pd.read_csv('../../examples/tips.csv')
print(tips)
"""crosstab 按照day和size进行统计"""
party_counts = pd.crosstab(tips['day'], tips['size'])
print(party_counts)
# 去掉size=1 和 6的party
party_counts = party_counts.loc[:, 2:5]
# print(party_counts.sum(1))

"""
规格化 使各行和为1  便可以直接生成图表显示占比
div(sum(1)) 每个值对总数进行整除 计算百分比
这里sum(1)意味着统计纵轴 即保留行统计列 列相加
"""
party_pcts = party_counts.div(party_counts.sum(1), axis=0)
print(party_pcts)
party_pcts.plot.bar()
plt.show()


"""seaborn 指定x y轴 对data进行绘制 黑色线表示置信区间"""
import seaborn as sns
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
print(tips.head())
# hue 允许多使用一个分类值 将数据分离
sns.barplot(x='tip_pct', y='day', hue="time", data=tips, orient='h')

plt.show()
sns.set(style="whitegrid")
plt.show()
# sns继续学习


