# encoding: utf-8
"""
@Project ：
@File: test.py
@Author: liuwz
@time: 2022/1/20 11:08 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

file = '~/work/ln/doc/sec_group.csv'
data = pd.read_csv('~/work/ln/doc/sec_group.csv')
inbounds = data['inbounds'][0]
print(inbounds)


# import csv
# with open('~/work/ln/doc/sec_group.csv') as f:
#     reader = csv.reader(f)
#     column=[row[0] for row in reader]
#     print(column)
