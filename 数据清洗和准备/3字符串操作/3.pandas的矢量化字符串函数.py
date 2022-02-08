# encoding: utf-8
"""
@Project ： 
@File: 3.pandas的矢量化字符串函数.py
@Author: liuwz
@time: 2022/2/8 4:27 下午
@desc: 
"""
import re

import pandas as pd
import numpy as np

data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 'Wes': np.nan}
data = pd.Series(data)

print(data.isna())

# 通过Series的str属性即可访问这些方法 跳过NA值
result = data.str.contains("gmail")
print(result)

# 正则表达式
pattern = '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})'
result1 = data.str.findall(pattern, flags=re.IGNORECASE)
print(result1)

# 元素获取 索引
print(data.str.get(1))
print(data.str[1])
print(data.str[:])

# 元素拼接
print(data.str.cat(sep="#"))
