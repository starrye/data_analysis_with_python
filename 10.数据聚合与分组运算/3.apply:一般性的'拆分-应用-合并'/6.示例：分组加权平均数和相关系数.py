# encoding: utf-8
"""
@Project ： 
@File: 6.示例：分组加权平均数和相关系数.py
@Author: liuwz
@time: 2022/3/3 11:49 上午
@desc: 
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'category': ['a', 'a', 'a', 'a',
                                'b', 'b', 'b', 'b'],
                   'data': np.arange(1, 9),
                   'weights': [1,2,1,2,1,2,1,2]})

"""
计算加权平均数 average(data, weights=xx)  按照每个参数的权重值计算平均值
当前权重/总权重 * data  即为平均值
"""
#print(df)
grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])
result = grouped.apply(get_wavg)
#print(result)


close_px = pd.read_csv("../../examples/stock_px_2.csv", parse_dates=True, index_col=0)
print(close_px)

"""相关系数：统计两个变量之间的线性相关关系，如果-1 负相关 1 正相关 0 不相关"""
"""计算日收益率与spx之间的相关系数
"""
spx_corr = lambda x: x.corrwith(x['SPX'])
# 1/计算收益率日百分比
# pct_change: Percentage change between the current and a prior element.
# for example : (908.59-909.03)/909.03
rets = close_px.pct_change().dropna()
# 2/按年分组
get_year = lambda x: x.year
grouped = rets.groupby(get_year)
# 3/计算相关系数
result = grouped.apply(spx_corr)
print(result)

"""计算列之间的相关系数"""
result = grouped.apply(lambda g: g["AAPL"].corr(g["MSFT"]))
print(result)

