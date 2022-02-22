# encoding: utf-8
"""
@Project ：
@File: 相关系数与协方差.py
@Author: liuwz
@time: 2022/1/9 3:32 PM
@desc: 
"""
# import numpy as np
# import pandas as pd
# from pandas import Series, DataFrame
# import pandas_datareader.data as web
#
# all_data = {ticker: web.get_data_yahoo(ticker)
#             for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}
#
# price = pd.DataFrame({ticker: data['Adj Close']
#                      for ticker, data in all_data.items()})
# volume = pd.DataFrame({ticker: data['Volume']
#                       for ticker, data in all_data.items()})
#
# returns = price.pct_change()
# print(returns.tail())