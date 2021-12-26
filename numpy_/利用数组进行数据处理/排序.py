# encoding: utf-8
"""
@Project ：
@File: 排序.py
@Author: liuwz
@time: 2021/12/25 6:38 下午
@desc: 
"""

# 逐行排序
import numpy as np

arr = np.random.randn(6)

# sort排序 原地排序
arr.sort()
print(arr)

# 任意轴排序
arr = np.random.randn(5, 3)
print(arr)
# np.sort() 是进行副本排序 不会改变原数组
print(np.sort(arr))

# sort(0) 纵轴排序 sort(1) 横轴排序
arr.sort(0)
print(arr)


