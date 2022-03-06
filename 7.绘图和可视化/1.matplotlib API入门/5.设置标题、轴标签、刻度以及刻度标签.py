# encoding: utf-8
"""
@Project ：
@File: 5.设置标题、轴标签、刻度以及刻度标签.py
@Author: liuwz
@time: 2022/2/27 11:22 上午
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
# plt.show()

"""set_xticks 设置x轴取值范围 使用数组
set_xticklabels 设置x轴取值范围 使用任何其他值形式"""
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
# plt.show()
# rotation: 标签倾斜角度 fontsize: 标签大小
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=10, fontsize='small')
# plt.show()

"""set_title 设置标题
set_xlabel 设置x轴名称
set_ylabel 设置y轴名称"""
ax.set_title("My first plot")
ax.set_xlabel("i'm x-axis")
ax.set_ylabel("i'm y-axis")
# plt.show()

"""set 统一设置标签 轴名称"""
parms = {
    'title': "my my my plot",
    'xlabel': "x x x lable",
    'ylabel': "y y y lable"
}
ax.set(**parms)
plt.show()
