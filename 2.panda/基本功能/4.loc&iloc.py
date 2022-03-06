# encoding: utf-8
"""
@Project ：
@File: loc&iloc.py
@Author: liuwz
@time: 2022/1/3 6:19 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 针对DataFrame有loc轴标签 iloc 整数索引
data = pd.DataFrame(
    np.arange(16).reshape(
        (4, 4)), index=[
            'Ohio', 'Colorado', 'Utah', 'New York'], columns=[
                'one', 'two', 'three', 'four'])
# 选取行为Colorado 列为 two & three的数据
print(data.loc['Colorado', ['two', 'three']])
# 利用iloc和整数选取数据 为第3,4行 第5,1,2列
print(data.iloc[[2, 3], [3, 0, 1]])

# 选择第3行数据
print(data.iloc[2])
# 选择第4列数据
print(data.iloc[:, 3])
print('-'*30)
# 表达式 先取所有行和前3列 然后过滤three大于5的行
print(data.iloc[:, :3][data.three > 5])
# 标签与切片
print(data.loc[:"Utah", 'two'])

# !loc的索引包含末端 iloc的索引不包含末端
