# encoding: utf-8
"""
@Project ：
@File: 1.main.py
@Author: liuwz
@time: 2021/12/26 12:17 下午
@desc: 
"""

# 原生随机漫步
import random

import numpy as np
from matplotlib import pyplot as plt

position = 0
walk = [position]
steps = 1000
for i in range(steps):

    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
# print(walk)

nsteps = 1000


draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
#print(walk.max())
#print(walk.min())

# 获取任一方向超过10m的时间(索引) argmax 返回第一个最大值(True)的索引 但是会扫描完数组
# print((np.abs(walk) >= 10).argmax())

# 一次模拟多个随机漫步

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
print(walks)
# 获取所有超过30或者-30的时间
hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)
# 利用布尔值获取所有超过30(abs)的行
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
# 超过30(abs)的平均步数
print(crossing_times.mean())

