# encoding: utf-8
"""
@Project ：
@File: 2.Figure和Subplot.py
@Author: liuwz
@time: 2022/2/8 11:25 PM
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

"""matplotlib的图像都位于Figure对象中"""
fig = plt.figure()
# add_subplot() 图像应该是2×2的（即最多4张图） 1 表示选中第一张图
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

"""
hist:直方图
histogram:点图
"""
# bins：直方图中柱子的数量
# alpha: 透明度
ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
# 如果没有指定使用哪个小窗口图 则会在最后一个用过的subplot上进行绘制
# plt.plot(np.random.randn(50).cumsum(), 'k--')
# plt.show()

# 创建一个新的Figure对象 + 已创建的subplot对象的Numpy数组
# 这样可以轻松的对axes进行索引
fig, axes = plt.subplots(2, 3)
print(axes)

axes[0][1].hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
plt.show()

