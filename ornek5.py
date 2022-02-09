# -*- coding: utf-8 -*-
"""
dataset: https://www.kaggle.com/fazilbtopal/auto85
auto.csv kullanarak,
Beygir gücü en fazla ve en az olan arabalar hangileridir?

"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("auto.csv",na_values=['?'])
print(df.columns)

print("beygir gücü buyukten kucuge")
print(df.sort_values(by='horsepower',ascending=False))
print("beygir gücü kucukten buyuge")
print(df.sort_values(by='horsepower'))
