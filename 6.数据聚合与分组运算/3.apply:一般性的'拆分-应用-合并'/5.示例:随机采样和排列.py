# encoding: utf-8
"""
@Project ： 
@File: 5.示例:随机采样和排列.py
@Author: liuwz
@time: 2022/3/3 11:17 上午
@desc: 
"""

import pandas as pd
import numpy as np



suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1, 11)) + [10] * 3) * 4
base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q']
cards = []
for suit in suits:
    cards.extend(str(num) + suit for num in base_names)
deck = pd.Series(card_val, index=cards)
print(deck)

"""sample 随机抽取"""
def draw(deck, n=5):
    return deck.sample(n)


result = draw(deck)
print(result)

"""groupby 应用匿名函数 然后 apply应用函数 先分组然后抽取"""
get_suit = lambda card: card[-1] # last letter is suit
result1 = deck.groupby(get_suit).apply(draw, n=2)
print(result1)

