# encoding: utf-8
"""
@Project ：
@File: 4.散步图或点图.py
@Author: liuwz
@time: 2022/3/13 3:51 下午
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import seaborn as sns


marco = pd.read_csv('../../examples/macrodata.csv')
data = marco[['cpi', 'm1', 'tbilrate', 'unemp']]

trans_data = np.log(data).diff().dropna()
result = trans_data[-5:]
print(result)

"""sns regplot 回归线+点图"""
sns.regplot('m1', 'unemp', data=trans_data)
plt.title("Changes in log m1 versus lor unemp")

plt.show()

"""sns.pairplot 针对每个变量绘制散步图"""
sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})
plt.show()



