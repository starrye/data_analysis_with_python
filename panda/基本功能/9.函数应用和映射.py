# encoding: utf-8
"""
@Project ： 
@File: 9.函数应用和映射.py
@Author: liuwz
@time: 2022/1/4 4:32 下午
@desc: 
"""

import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

# numpy方法操作pd对象
frame = np.abs(frame)
print(frame)


# 将函数应用到由各列或行所形成的一维数组上 apply
f = lambda x:x.max() - x.min()

frame1 = frame.apply(f)  # 每一列最大值减去最小值
print(frame1)

frame2 = frame.apply(f, axis=1)  # 每一行最大值减去最小值
print(frame2)


# 返回多个值组成的Series
def f(x):
   return pd.Series([x.min(), x.max()], index=["min", 'max'])

frame3 = frame.apply(f)
print(frame3)

# 格式化浮点数保留位数？ applymap
format = lambda x: '%.2f' % x
frame4 = frame.applymap(format)
print(frame4)

# map只能应用于某一行/列
# frame5 = frame.iloc[1].map(format)
frame5 = frame.iloc[:, 1].map(format)
print(frame5)