# encoding: utf-8
"""
@Project ： 
@File: 数学和统计方法.py
@Author: liuwz
@time: 2021/12/24 3:47 下午
@desc: 
"""
import numpy as np

a = np.arange(1, 13).reshape((3, 4))
# print(a)
# 求最大值的索引两种方式
print(np.argmin(a))
print(a.argmin())
# 求最大值的索引两种方式
print(np.argmax(a))
print(a.argmax())

# 平均值
print(np.mean(a))
print(a.mean())
print(np.average(a))

# 求中位数
print(np.median(a))

# 累计求和 第一个数是矩阵第一个数 第二数是矩阵第一个数与第二个数的和 依次类推
print(np.cumsum(a))
# 求差  第一个数是矩阵第二个数减去第一个数 第二数是矩阵第三个数减去第二个数 依次类推
print(np.diff(a))

# 逐行排序
b = np.arange(13, 1, -1).reshape((3, 4))
print(np.sort(b))

# 矩阵的转置的两种方式 行变列
print(np.transpose(a))
print(a.T)

# 矩阵的截取 clip(a,a_min,a_max),
# 先过滤所有小于a_min的数强制转化为a_min,再过滤所有大于a_max的数强制转化为a_max
print(np.clip(a, 3, 7))
