# encoding: utf-8
"""
@Project ：
@File: DataFrame.py
@Author: liuwz
@time: 2021/12/26 5:10 下午
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],index=['1', 'two', 'three', 'four','five', 'six'])

print(frame2['year'])

# loc 取指定名称行
print(frame2.loc['1'])

# 列赋值
frame2['debt'] = "test"
print(frame2)
# 如果通过列表或者数组赋值某个列 则长度一定要匹配
frame2['debt'] = np.arange(6.)
print(frame2)
# 通过Series赋值 可以指定index
val = pd.Series([-1.2, -1.1, -1.7], index=['two', 'three', 'five'])
frame2['debt'] = val
print(frame2)
print('-'*30)

# 添加新列
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

# 删除一列
del frame2['eastern']
print(frame2)
print('-'*30)
# 嵌套字典 外层做列 内层做行
data = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(data, index=[2000, 2001, 2002])
print(frame3)
print(frame3.T)

pdata = {'Ohio': frame3['Ohio'][:-1],'Nevada': frame3['Nevada'][:2]}
print(pd.DataFrame(pdata))

# values返回二维ndarray
print(frame3.values)
print(frame2.values)




