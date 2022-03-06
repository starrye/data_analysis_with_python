# encoding: utf-8
"""
@Project ： 
@File: 5.JSON数据.py
@Author: liuwz
@time: 2022/1/12 7:48 下午
@desc: 
"""

import pandas as pd
import numpy as np

result = {'name': 'Wes',
 'pet': None,
 'places_lived': ['United States', 'Spain', 'Germany'],
 'siblings': [{'age': 30, 'name': 'Scott', 'pets': ['Zeus', 'Zuko']},
  {'age': 38, 'name': 'Katie', 'pets': ['Sixes', 'Stache', 'Cisco']}]}


# 只读取 name  age字段的值
sb = pd.DataFrame(result['siblings'], columns=['name', 'age'])
print(sb)


"""read_json 读取json文件"""
data = pd.read_json('../../examples/example.json')
print(type(data))

"""to_json 将DataFrame输出成json"""
print(data.to_json()) # 默认按照Series样式输出
print(data.to_json(orient='records'))
