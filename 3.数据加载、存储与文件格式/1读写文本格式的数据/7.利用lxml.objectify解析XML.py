# encoding: utf-8
"""
@Project ：
@File: 7.利用lxml.objectify解析XML.py
@Author: liuwz
@time: 2022/1/12 11:37 PM
@desc: 
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

from lxml import objectify

path = '../../datasets/mta_perf/Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()
print(root.INDICATOR)


data = []

skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',
               'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)
perf = pd.DataFrame(data)
print(perf.head())