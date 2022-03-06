# encoding: utf-8
"""
@Project ： 
@File: 4.根据索引级别分组.py
@Author: liuwz
@time: 2022/2/23 12:15 下午
@desc: 
"""

import pandas as pd
import numpy as np

columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                    [1, 3, 5, 1, 3]],
                                    names=['cty', 'tenor'])
hier_df = pd.DataFrame(np.random.randn(4, 5), columns=columns)
print(hier_df)

result = hier_df.groupby(level='cty', axis=1).count()
result1 = hier_df.groupby(level='tenor', axis=1).count()
print(result)
print(result1)