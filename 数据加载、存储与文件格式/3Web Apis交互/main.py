# encoding: utf-8
"""
@Project ：
@File: main.py
@Author: liuwz
@time: 2022/1/16 6:24 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import requests
"""requests"""

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'

resp = requests.get(url)

# json方法会返回一个json字典
data = resp.json()
# print(data)
# print(data[0]['title'])

"""数据导入Dataframe"""
issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
print(issues.head(10))