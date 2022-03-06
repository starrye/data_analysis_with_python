# encoding: utf-8
"""
@Project ：
@File: 1.main.py
@Author: liuwz
@time: 2021/12/26 12:08 下午
@desc: 
"""

# normal 标准正态分布的数组
import numpy as np

sam = np.random.normal(size=(4, 4))
print(sam)

# 伪随机数 因为通过算法基于随机数生成器种子，在确定性的条件下生成的，使用seed更改随机数生成种子
np.random.seed(1234)

# 或者使用RandomState 生成一个用全局随机器隔离的随机数组
rng = np.random.RandomState(234)

print(rng.randn(10))

