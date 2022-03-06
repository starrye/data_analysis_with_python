# encoding: utf-8
"""
@Project ：
@File: 1.线型图.py
@Author: liuwz
@time: 2022/3/6 5:11 下午
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

"""series DF 都有plot方法用来生成线型图"""
s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
print(s)
s.plot()
plt.show()

"""DF的plot方法会在subplot中为各列绘制一条线，并自动创建图例"""
df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
                  columns=['A', 'B', 'C', 'D'],
                  index=np.arange(0, 100, 10))
# subplots 分开绘制 sharex 共享x轴(建立在分开绘制的基础上)
df.plot(subplots=True, sharex=True)
plt.show()

