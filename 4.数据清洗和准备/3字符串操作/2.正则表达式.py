# encoding: utf-8
"""
@Project ： 
@File: 2.正则表达式.py
@Author: liuwz
@time: 2022/2/7 4:55 下午
@desc: 
"""

import pandas as pd
import numpy as np

import re
text = "foo    bar\t baz  \tqux"
# 正则表达式会先被编译，然后再在text上调用其split方法
result = re.split('\s+', text)
print(result)

regex = re.compile('\s+')
result1 = regex.split(text)
print(result1)



text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

# re.IGNORECASE makes the regex case-insensitive
regex = re.compile(pattern, flags=re.IGNORECASE)
result3 = regex.findall(text)
print(result3)

# search 返回在原字符串中的起始和结束位置
m = regex.search(text)
print(text[m.start(): m.end()])

# sub替换
print(regex.sub('REDACTED', text))

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)
print(regex.findall(text))