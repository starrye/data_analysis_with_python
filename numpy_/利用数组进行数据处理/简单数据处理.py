# encoding: utf-8
"""
@Project ：
@File: 简单数据处理.py
@Author: liuwz
@time: 2021/12/23 5:01 下午
@desc: 
"""
import numpy_ as np
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.01)

xs, ys = np.meshgrid(points, points)

# print(ys)

print(xs ** 2 + ys ** 2)

z = np.sqrt(xs ** 2 + ys ** 2)

print(z)



plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()

plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

plt.show()