# encoding: utf-8
"""
@Project ：
@File: 3.调整subplot周围的间距.py
@Author: liuwz
@time: 2022/2/20 11:05 下午
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

"""wspace,space用于控制宽度和高度的百分比
wspace:多张图左右之间的间距
space:多张图上下之间的间距
"""
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.show()