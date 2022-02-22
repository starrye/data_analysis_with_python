# encoding: utf-8
"""
@Project ：
@File: 1.基础方法.py
@Author: liuwz
@time: 2022/1/12 11:50 PM
@desc: 
"""
import sys

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


frame = pd.read_csv('../../examples/ex1.csv')

"""python内置pickle 用于短期存储二进制格式， 因为下个版本可能就无法unpickle出来"""
frame.to_pickle('frame_pickle')

pickle_frame = pd.read_pickle('frame_pickle')
print(pickle_frame)

"""
pandas内置 HDF5 和 MessagePack可以存储二进制数据格式
bcolz 可压缩的列存储二进制格式
"""





