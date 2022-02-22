# encoding: utf-8
"""
@Project ：
@File: main.py
@Author: liuwz
@time: 2021/12/26 11:32 上午
@desc: 
"""
import numpy as np
from numpy.linalg import inv, qr

x = np.arange(1, 7).reshape(2, 3)
y = np.arange(8, 14).reshape(3, 2)

# dot 矩阵乘法
# print(x.dot(y)) # 等价 np.dot(x, y)

# @ 也可表示乘法
# print(x @ np.ones(3))

# 转置点积
X = np.arange(1, 5, dtype=float).reshape(2, 2)
mat = X.T.dot(X)
print(mat)
# inv 求逆矩阵
print(inv(mat))

# 逆矩阵与原矩阵的积为E
print(mat.dot(inv(mat)))

# QR正交三角分解法求 特征值和特征向量
q, r = qr(mat)
print(q, r)
