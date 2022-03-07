# encoding: utf-8
"""
@Project ：
@File: 5.离散化和面元划分.py
@Author: liuwz
@time: 2022/1/18 11:33 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


"""cut 划分不同的数据组"""
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

bins = [18, 25, 35, 60, 100]

# labels 设置"箱子"名称
cats = pd.cut(ages, bins, labels=['Youth', 'YoungAdult', 'MiddleAged', 'Senior'])
print(cats)

# codes 表示每个元素所在区间的索引
print(cats.codes)
# categories 表示所有区间
print(cats.categories)
"""value_counts 统计每个区间的个数"""
print(pd.value_counts(cats))

# right=False 可以右侧开端

# 如果不确定分组界限呢？ 给组数让其自动划分？
data = np.random.rand(20)
# 直接传入数字 让其根据最大值和最小值自动划分  precision 限定小数位数
cats = pd.cut(data, 4, precision=3)
print(cats)


"""qcut 根据数据的分布情况，
cut可能无法使各个面元中含有相同数量的数据点。
而qcut由于使用的是样本分位数，因此可以得到大小基本相等的面"""

data = np.random.randn(1000)
qcats = pd.qcut(data, 4)
cats= pd.cut(data, 4)
# print(cats)
print(pd.value_counts(qcats))
print(pd.value_counts(cats))