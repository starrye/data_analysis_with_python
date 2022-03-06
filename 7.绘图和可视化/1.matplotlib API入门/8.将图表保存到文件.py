# encoding: utf-8
"""
@Project ：
@File: 8.将图表保存到文件.py
@Author: liuwz
@time: 2022/3/6 4:28 下午
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

"""plt.savefile将图表保存到文件/对象
dpi 分辨率 bbox_inches 图表需要保存的部分  常用tight用来剪除周围的空白部分
"""

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
plt.savefig("test.svg", dpi=400, bbox_inches="tight")
