# encoding: utf-8
"""
@Project ： 
@File: 2.索引上的合并.py
@Author: liuwz
@time: 2022/2/11 6:44 下午
@desc: 
"""

import pandas as pd
import numpy as np

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                      'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

"""on:具体索引名 index:bool"""
df1 = pd.merge(left1, right1, left_on='key', right_index=True)
print(df1)


left2 = pd.DataFrame({'group_val': range(2)}, index=['a', 'b'])
right2 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': [2, 4, 5, 6, 7, 8]})
df2 = pd.merge(left2, right2, right_on='key', left_index=True, how='outer')
# 调整列顺序
df2 = df2[['key', 'value', 'group_val']]
print(df2)


"""多层次索引合并"""
lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio',
                               'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio',
                              'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])


df3 = pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
print(df3)


lefth2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                     index=['a', 'c', 'e'],
                     columns=['Ohio', 'Nevada'])
righth2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                      index=['b', 'c', 'd', 'e'],
                      columns=['Missouri', 'Alabama'])
print('-'*30)
df4 = pd.merge(lefth2, righth2, how='outer', left_index=True, right_index=True)
print(df4)
print('-'*30)
"""join方法"""
df5 = righth2.join(lefth2, how='outer')
print(df5)

another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                       index=['a', 'c', 'e', 'f'],
                       columns=['New York','Oregon'])

df6 = lefth2.join([righth2, another])
print(df6)

