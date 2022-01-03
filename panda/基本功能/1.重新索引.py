# encoding: utf-8
"""
@Project ：
@File: 1.重新索引.py
@Author: liuwz
@time: 2022/1/3 5:12 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


obj = pd.Series([4.5, 7.2, -5.3, 2], index=['d', 'b', 'a', 'c'])
# reindex 重新创建索引 如果某个索引不存在值则为空 NaN
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

# 重新索引如何插值处理
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 1, 3])
# ffill 自动填充为和前索引的值一样
obj4 = obj3.reindex(range(6), method="ffill")
print(obj4)

# 重新索引如何修改列 columns 但是和行索引一样也只能改变顺序而已 如果改变列 则值会变为NaN
obj5 = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
print(obj5)
obj6 = obj5.reindex(columns=["Texas", "i", "am"])
print(obj6)
