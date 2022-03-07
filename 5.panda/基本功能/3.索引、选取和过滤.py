# encoding: utf-8
"""
@Project ：
@File: 索引、选取和过滤.py
@Author: liuwz
@time: 2022/1/3 6:07 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)

# 通过索引取值的几种方式
print(obj['b'])
print(obj[1])
# 索引的切片和python一样 不包含末端
print(obj[2:4])
# 注意标签的切片和python的不一样 是包含末端的
print(obj['a':'c'])
print(obj[['b', 'c']])
print(obj[[1, 3]])
print(obj[obj > 2])
print('-'*30)

# 标签切片赋值操作
obj['b':'c'] = [1, 2]
obj['b':'c'] = 5
print(obj)
print('-'*30)
# DataFrame 通过值选取 是获取列
data = pd.DataFrame(
    np.arange(16).reshape(
        (4, 4)), index=[
            'Ohio', 'Colorado', 'Utah', 'New York'], columns=[
                'one', 'two', 'three', 'four'])
print(data['one'])
print(data[['three', 'one']])
# 通过索引选取 如果是单值就是列 如果是切片或者表达式就是行
print(data[:2])
print(data[data['three'] > 5])
print(data < 5)
# 所有元素小于5的元素设为0
data[data < 5] = 0
print(data)


