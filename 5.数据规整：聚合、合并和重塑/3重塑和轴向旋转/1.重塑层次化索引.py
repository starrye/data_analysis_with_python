# encoding: utf-8
"""
@Project ： 
@File: 1.重塑层次化索引.py
@Author: liuwz
@time: 2022/2/21 12:00 下午
@desc: 
"""

import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index=pd.Index(['Ohio','Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'],
                    name='number'))
print(data)

# stack将一个DF转化为Series
result = data.stack()
print(result)
# unstack将一个Series转化为DF 前提是Series必须满足DF的格式 层次化索引转化为行列
DF1 = result.unstack()
# unstack默认操作的是最内层 所以0是state 也可以直接指定unstack哪一层
DF2 = result.unstack(0)
DF3 = result.unstack("state")
DF4 = result.unstack("number")
print(DF1)
print(DF2)
print(DF3)
print(DF4)
print('-'*50)

s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
# key设置额外层次索引
s3 = pd.concat([s1, s2], keys=['one', 'two'])
print(s3)

s3 = s3.unstack()
"""unstack 引起缺失值 但是stack可以过滤缺失值 当然也许你不需要他过滤 所以dropna=False就行"""
s4 = s3.stack(dropna=False)
print(s4)
print('-'*40)

df = pd.DataFrame({'left': result, 'right': result + 5},
                  columns=pd.Index(['left', 'right'], name='side'))
print(df)
print('-'*40)
result = df.unstack('state').stack('side')
print(result)