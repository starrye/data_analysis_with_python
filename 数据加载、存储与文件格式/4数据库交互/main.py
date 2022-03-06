# encoding: utf-8
"""
@Project ：
@File: 1.main.py
@Author: liuwz
@time: 2022/1/16 6:29 PM
@desc:
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import sqlite3

query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
 c REAL,        d INTEGER
 );
"""

con = sqlite3.connect('mydata.sqlite')

# con.execute(query)

# con.commit()

data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

# con.executemany(stmt, data)
# con.commit()

"""1/从数据库获取数据导入"""
# 先获取数据
cursor = con.execute('select * from test')
rows = cursor.fetchall()
# 然后导入DF 注意需要列名
df = pd.DataFrame(rows, columns=[x[0] for x in cursor.description])

# print(df)


"""2/read_sql"""
import sqlalchemy as sqla
db = sqla.create_engine("sqlite:///mydata.sqlite")

rs = pd.read_sql("select * from test", db)
print(rs)
