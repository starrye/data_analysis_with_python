# encoding: utf-8
"""
@Project ：
@File: 7.排列和随机采样.py
@Author: liuwz
@time: 2022/1/23 10:36 AM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

"""numpy.random.permutation函数 随机行重排列 df调用使用take方法"""
df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))

sampler = np.random.permutation(5)
print(sampler)

print(df)
print(df.take(sampler))

"""dataframe sample返回随机子集"""
print(df.sample(3))


