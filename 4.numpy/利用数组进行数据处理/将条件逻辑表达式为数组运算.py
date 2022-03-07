# encoding: utf-8
"""
@Project ： 
@File: 将条件逻辑表达式为数组运算.py
@Author: liuwz
@time: 2021/12/23 5:33 下午
@desc: 
"""
import numpy as np

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])

yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])

cond = np.array([True, False, True, True, False])

# 列表推导式
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
# print(result)

# where
result = np.where(cond, xarr, yarr)
# print(result)

arr = np.random.randn(4, 4)
# print(arr > 0)
# 大于0都是2 小于0都是-2 类似 三目表达式
print(np.where(arr > 0, 2, -2))

# 大于0都是2 小于0则仍为arr数组 意味不变
print(np.where(arr > 0, 2, arr))
