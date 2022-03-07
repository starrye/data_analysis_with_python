# encoding: utf-8
"""
@Project ： 
@File: 数学和统计方法.py
@Author: liuwz
@time: 2021/12/24 3:47 下午
@desc: 
"""
import numpy as np

a = np.arange(0, 9).reshape((3, 3))
# 求最小值的索引两种方式
print(np.argmin(a))
print(a.argmin())
print('-'*30)

# 求最大值的索引两种方式
print(np.argmax(a))
print(a.argmax())
print('-'*30)

# 平均值
print(np.mean(a))
print(a.mean())
print(np.average(a))
print("行平均值:%s" % a.mean(axis=1))
print("列平均值:%s" % a.mean(axis=0))
print('-'*30)

# 求中位数
print(np.median(a))

# 累计求和 第一个数是矩阵第一个数 第二数是矩阵第一个数与第二个数的和 依次类推
print("累加函数:%s" % np.cumsum(a))
print(a)
print("横向累加:%s" % a.cumsum(axis=0))
print("纵向累积:%s" % a.cumprod(axis=1))
# 求差  第一个数是矩阵第二个数减去第一个数 第二数是矩阵第三个数减去第二个数 依次类推
print(np.diff(a))


# 矩阵的转置的两种方式 行变列
print(np.transpose(a))
print(a.T)

# 矩阵的截取 clip(a,a_min,a_max),
# 先过滤所有小于a_min的数强制转化为a_min,再过滤所有大于a_max的数强制转化为a_max
print(np.clip(a, 3, 7))
