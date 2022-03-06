# encoding: utf-8
"""
@Project ：
@File: 01-快速的元素级别组函数.py
@Author: liuwz
@time: 2021/12/22 5:35 下午
@desc: 
"""
import numpy as np

arr = np.arange(10, dtype=float)

# 平方根 不修改arr本身的值
print("arr平方根:%s" % np.sqrt(arr))
print("arr:%s" % arr)
print("arr:%s" % np.sqrt(arr, arr))

# e的n次方
print(np.exp(arr))

x = np.random.randn(8)

y = np.random.randn(8)

# x和y中元素级别最大的元素
print(np.maximum(x, y))

arr = np.random.randn(7) * 5
remainder, whole_part = np.modf(arr)
print(remainder, whole_part)

