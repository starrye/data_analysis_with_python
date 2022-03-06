# encoding: utf-8
"""
@Project ：
@File: 2.利用函数或映射进行数据转换.py
@Author: liuwz
@time: 2022/1/16 7:25 PM
@desc:
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                              'Pastrami', 'corned beef', 'Bacon',
                              'pastrami', 'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

print(data)

# 想要添加一列表示 食物的来源
food_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}

"""Series map方法接受函数或者字典 来进行添加"""
# 先将data数据里面的food数据首字母大写改成小写 不然映射对应不上
lowercased = data['food'].str.lower()

data['animal'] = lowercased.map(food_to_animal)
print(data)

"""函数添加"""
data['animal'] = data['food'].map(lambda x: food_to_animal[x.lower()])
print(data)
