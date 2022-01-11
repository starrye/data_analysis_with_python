# encoding: utf-8
"""
@Project ：
@File: 基础方法.py
@Author: liuwz
@time: 2022/1/9 5:30 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# read_csv 有标题名
df = pd.read_csv("../../examples/ex1.csv")
print(df)

# read_table 需要指定 分隔符
df = pd.read_table("../../examples/ex1.csv", sep=',')
print(df)
# 没有标题行？ 则默认递增数字作为索引和列
df1 = pd.read_csv('../../examples/ex2.csv', header=None)
print(df1)
df2 = pd.read_csv('../../examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
print(df2)
# index_col 指定哪一列作为索引 可以为索引或者值 'message'/4
df3 = pd.read_csv('../../examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'], index_col='message')
print(df3)
# 相同的索引可以合并
df4 = pd.read_csv("../../examples/csv_mindex.csv", index_col=['key1', 'key2'])
print(df4)
print('-' * 30)


"""正则表达式作为分隔符"""
df5 = pd.read_table("../../examples/ex3.txt", sep=r"\s+")
print(df5)

"""文件内容复杂 可以skiprows跳过指定行"""
df6 = pd.read_table("../../examples/ex4.csv", skiprows=[0, 2, 3])
print(df6)

df7 = pd.read_csv("../../examples/ex5.csv")
print(df7)
print(pd.isna(df7))

df8 = pd.read_csv("../../examples/ex5.csv", na_values=["NULL"])
print(df8)



