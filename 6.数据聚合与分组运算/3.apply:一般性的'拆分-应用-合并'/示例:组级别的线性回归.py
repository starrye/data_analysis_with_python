# encoding: utf-8
"""
@Project ： 
@File: 示例:组级别的线性回归.py
@Author: liuwz
@time: 2022/3/7 6:08 下午
@desc: 
"""

import pandas as pd
import numpy as np


import statsmodels.api as sm
"""最小二乘法 拟合线性回归"""
def regress(data, yvar, xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params

