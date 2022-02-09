# -*- coding: utf-8 -*-
"""
dataset: https://www.kaggle.com/fazilbtopal/auto85
auto.csv kullanarak,

En pahalı ve en ucuz araba markaları hangileridir?
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("auto.csv",na_values=['?'])
print(df.columns)

print("fiyatlar",df['price'])

print("buyukten kucuge fiyat listesi:")
print(df.sort_values(by='price',ascending=False))
print("kucukten büyüğe fiyat listesi:")
print(df.sort_values(by='price'))
