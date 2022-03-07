# encoding: utf-8
"""
@Project ： 
@File: 3.将数据写出到文本格式.py
@Author: liuwz
@time: 2022/1/12 6:04 下午
@desc: 
"""
import sys

import pandas as pd
import numpy as np

data = pd.read_csv("../../examples/ex5.csv")

print(data)

"""to_csv 将数据写到一个 默认以逗号分割的文件"""
# data.to_csv("out.csv")

# sep设置分割符
data.to_csv(sys.stdout, sep="|")
print('-'*30)
# na_rep 其他值表示缺失值
data.to_csv(sys.stdout, sep="|", na_rep="None")
print('-'*30)
# 禁用行列的标签
data.to_csv(sys.stdout, sep="|", na_rep="None", header=False, index=False)

# 指定列名
data.to_csv(sys.stdout, sep="#", na_rep="None", index=False, columns=['a', 'b', 'c'])



# Series的to_csv方法
print('-'*30)
dates = pd.date_range("1/1/2022", periods=7)
ts = pd.Series(np.arange(7), index=dates)

ts.to_csv(sys.stdout)

