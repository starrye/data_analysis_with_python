# encoding: utf-8
"""
@Project ：
@File: 1.main.py
@Author: liuwz
@time: 2021/12/26 11:25 上午
@desc: 
"""
import numpy as np

arr = np.arange(10)
arr1 = np.arange(10, 20)
# save 二进制存文件 生成npy文件
np.save("test_arr", arr)

# load 读取npy二进制文件
arr_read = np.load("test_arr.npy")
print(arr_read)

# savez 保存多个数组，并以关键字参数的形式传入 读取时也需要使用参数，类似字典的读取
np.savez("arr_archive.npz", a=arr, b=arr1)

arch = np.load("arr_archive.npz")
print(arch["a"])
print(arch["b"])
