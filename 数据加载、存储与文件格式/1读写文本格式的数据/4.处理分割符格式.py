# encoding: utf-8
"""
@Project ： 
@File: 4.处理分割符格式.py
@Author: liuwz
@time: 2022/1/12 7:27 下午
@desc: 
"""

import pandas as pd
import numpy as np
import csv

f = open('../../examples/ex7.csv')

"""csv.reader 读取csv文件 生成一个可迭代对象"""
reader = csv.reader(f)
print(reader)

for line in reader:
    print(line)

with open('../../examples/ex7.csv') as f:
   lines = list(csv.reader(f))
header, data = line[0], line[1:]
data_dict = {h: v for h, v in zip(header, zip(*data))}


# 自定义csv格式
class my_dialect(csv.Dialect):
    lineterminator = '\n'  # 写操作的行结束符
    delimiter = ';'  # 用于分割字段的单字符字符串 默认为 ,
    quotechar = ','  # 用于带有特殊符号的字段的引用符号 默认 "
    quoting = csv.QUOTE_MINIMAL  # 引用范围  QUOTE_MINIMAL 表示只引用带有类似分割符之类特殊字符的字段
f = open('../../examples/ex7.csv')
reader = csv.reader(f, dialect=my_dialect)
print(list(reader))

with open('mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one', 'two', 'three'))
    writer.writerow(('1', '2', '3'))
    writer.writerow(('4', '5', '6'))
    writer.writerow(('7', '8', '9'))

# cs1 = pd.read_csv("../../examples/ex7.csv")
# print(cs1)