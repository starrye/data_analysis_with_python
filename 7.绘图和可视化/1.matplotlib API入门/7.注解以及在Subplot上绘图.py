# encoding: utf-8
"""
@Project ：
@File: 7.注解以及在Subplot上绘图.py
@Author: liuwz
@time: 2022/3/6 4:00 下午
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from numpy.random import randn
from datetime import datetime


"""额外的注解和文字可以通过text arrow annotate函数进行添加"""
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

data = pd.read_csv('../../examples/spx.csv', index_col=0, parse_dates=True)
spx = data["SPX"]

spx.plot(ax=ax, style='k-')

crisis_data = [
    (datetime(2007, 10, 11), 'Peak of bull market'),
    (datetime(2008, 3, 12), 'Bear Stearns Fails'),
    (datetime(2008, 9, 15), 'Lehman Bankruptcy')
]
for date, label in crisis_data:
    """ annotate : xy 箭头到线的距离 越大越远，
                   xytext: 文字到线的距离 越大越远，
                   arrowprops: 文字的属性
                   horizontalalgnment: 箭头位于文字的哪边
                   
    """
    ax.annotate(label, xy=(date, spx.asof(date) + 75),
                xytext=(date, spx.asof(date) + 225),
                arrowprops=dict(facecolor='black', headwidth=4, width=2,
                                headlength=4),
                horizontalalignment='left', verticalalignment='center')


ax.set_xlim(['1/1/2007', '1/1/2011'])
ax.set_ylim([600, 1800])

ax.set_title('Important dates in the 2008-2009 financial crisis')
plt.show()

"""绘制块 比如矩形 三角形等"""
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# (x,y)：x,y坐标起始位置 长度 宽度 颜色 透明度
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
# (x,y) 圆心坐标 半径 颜色 透明度
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.1)
# 三个顶点坐标 颜色 透明度
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
                   color='g', alpha=0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)
plt.show()
