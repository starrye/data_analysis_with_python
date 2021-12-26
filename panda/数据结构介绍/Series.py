# encoding: utf-8
"""
@Project ：
@File: Series.py
@Author: liuwz
@time: 2021/12/26 4:18 下午
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = pd.Series([4, 7, -5, 3])

# 第一列索引，第二列数据
print(obj)
print(obj.values)
print(obj.index)

# 为数据指定索引
obj2 = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
print(obj2)

# 通过索引取值和改值 类似字典， 使用默认索引时则类似 列表
print(obj2['a'])
obj2['a'] = 5
print(obj2['a'])
print(obj2[['a', 'c', 'd']])
print("-"*30)

# 简单运算
print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))

# 直接将一个字典转为Series对象
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)
# 创建Series对象时传入自定义顺序的key
obj4 = pd.Series(sdata, index=['California', 'Ohio', 'Oregon', 'Texas'])
print(obj4)

# 判断空值和非空值
print(pd.isnull(obj4))  # obj4.isnull()
print(pd.notnull(obj4))

# 两个Series运算 类似 sql join 有相同值则累加 缺失则记录为NaN
print(obj3 + obj4)

# Series 本身和索引都具有一个name属性
obj4.name = "population"
obj4.index.name = "state"
print(obj4)


