# encoding: utf-8
"""
@Project ：
@File: 唯一化以及其他的集合逻辑.py
@Author: liuwz
@time: 2021/12/26 11:11 上午
@desc: 
"""
import numpy as np

names = np.array(['Joe', 'Bob', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

# unique 去重并排序
names = np.unique(names)
print(names)

# intersect1d 返回公共元素 并排序
x = np.arange(5)
y = np.arange(3, 8)
print(np.intersect1d(x, y))

# in1d 返回一个bool数组 表示一个数组中的值是否在另一个数组中
print(np.in1d(x, y))

# setdiff1d 返回集合的差，元素在x中不在y中
print(np.setdiff1d(x, y))

# 返回对称差：只存在一个数组的元素(不同时存在于两个数组)
print(np.setxor1d(x, y))



