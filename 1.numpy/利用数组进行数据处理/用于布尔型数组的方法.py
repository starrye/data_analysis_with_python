# encoding: utf-8
"""
@Project ：
@File: 用于布尔型数组的方法.py
@Author: liuwz
@time: 2021/12/25 6:30 下午
@desc: 
"""
import numpy as np

arr = np.random.randn(100)
print("数组中大于0的个数: %s " % (arr > 0).sum())
# any 判断数组中是否存在一个或多个True
print(any(arr > 0))
# all 判断数组中是否值都为True
print(all(arr > 0))


