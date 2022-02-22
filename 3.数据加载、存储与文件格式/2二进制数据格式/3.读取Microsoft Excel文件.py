# encoding: utf-8
"""
@Project ：
@File: 3.读取Microsoft Excel文件.py
@Author: liuwz
@time: 2022/1/13 11:49 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


"""pd.read_excel 读取excel"""
"""pd.ExcelFile 适用于一个文件中有多个工作表"""
xlxs = pd.ExcelFile('../../examples/ex1.xlsx')
xs = pd.read_excel(xlxs, sheet_name="Sheet1",header=0)  # 可以指定工作表
print(xs)

xs = pd.read_excel('../../examples/ex1.xlsx', sheet_name="Sheet1")
print(xs)


"""ExcelWriter + to_excel"""
writer = pd.ExcelWriter('../../examples/ex2.xlsx')
xs.to_excel(writer, 'Sheet1')
writer.save()

# 也可以直接to_excel
xs.to_excel('../../examples/ex2.xlsx', "Sheet1")