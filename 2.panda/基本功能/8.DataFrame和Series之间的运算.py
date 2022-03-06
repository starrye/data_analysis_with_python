# encoding: utf-8
"""
@Project ：
@File: 8.DataFrame和Series之间的运算.py
@Author: liuwz
@time: 2022/1/4 3:49 下午
@desc:
"""
import numpy as np
import pandas as pd


arr = np.arange(12.).reshape((3, 4))
print(arr)

# 每行都减去第一行  广播！
print(arr - arr[0])


frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])

series = frame.iloc[0]
print(series)

# 每行都减去第一行
result = frame - series
print(result)

print('-'*30)
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(series2)
print(frame)
# 并集 行广播
print(series2+frame)

# 如果需要列 广播 则指明列
series3 = frame.iloc[:, 1]
# series3 = frame['d']
result = frame.sub(series3, axis=0)
print(result)


