# encoding: utf-8
"""
@Project ：
@File: 4.颜色、标记和线型.py
@Author: liuwz
@time: 2022/2/20 11:25 下午
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

# 颜色+线型 or linestyle+color
# plt.plot(np.random.randn(50).cumsum(), 'r--')
plt.plot(np.random.randn(50).cumsum(), color='red', linestyle='--')
# plt.show()

# +o or marker='0' 可以强调数据点
plt.plot(np.random.randn(50).cumsum(), 'ro--')
plt.show()

data = np.random.randn(30).cumsum()

# drawstyle：连线风格 默认是直线连接
plt.plot(data, 'k-', label='Default')
plt.plot(data, 'k--', drawstyle='steps-post',label='steps-post')
"""xlim 设置x轴取值范围
如果调用不带参数，返回当前的参数值，调用带参数，则设置参数值
ylim 同理
"""
#
plt.xlim([0,35],)
# legend： 图例
plt.legend(loc='best')
plt.show()