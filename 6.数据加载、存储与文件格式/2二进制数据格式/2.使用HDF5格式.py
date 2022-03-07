# encoding: utf-8
"""
@Project ：
@File: 2.使用HDF5格式.py
@Author: liuwz
@time: 2022/1/12 11:56 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

"""HDF5支持分块读写"""

frame = pd.DataFrame({"a": np.random.randn(100)})

store = pd.HDFStore('mydata.h5')
store['obj1'] = frame
store['obj1_col'] = frame['a']

print(store['obj1'])

"""HDFStore 支持两种存储 fixed table(慢但支持特殊语法查询)"""
store.put('obj2', frame, format='table')
# 查询index大于9小于16的列
result = store.select('obj2', where=['index>=10 and index <= 15'])
print(result)
store.close()

# pd.read_hdf可以达到同样的效果
frame.to_hdf('mydata.h5', 'obj3', format='table')
result1 = pd.read_hdf('mydata.h5', 'obj3', where=['index>=10 and index <= 15'])
print(result1)
