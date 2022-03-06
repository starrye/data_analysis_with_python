# encoding: utf-8
"""
@Project ：
@File: 6.添加图例.py
@Author: liuwz
@time: 2022/3/6 3:54 下午
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from numpy.random import randn

fig =plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(randn(1000).cumsum(), 'k', label="one")
ax.plot(randn(1000).cumsum(), 'k--', label="two")
ax.plot(randn(1000).cumsum(), 'k.', label="three")
"""
legend() 自动创建图例
如果图例中想要去掉一个或多个元素，不传label参数即可
"""
ax.legend(loc="best")   # best 自动选择一个最不碍事的位置
plt.show()



