# -*- coding: utf-8 -*-
"""
dataset: https://www.kaggle.com/fazilbtopal/auto85
auto.csv kullanarak,

Diesel olan sedan araba sayısı kaç tanedir?

"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("auto.csv",na_values=['?'])
print(df.columns)

dizel=df[df['fuel-type']=='diesel']
print("dizel araba sayısı: ",len(dizel))
ds=dizel.groupby(['body-style']).get_group('sedan')
print("dizel olan sedan araba sayısı: ",len(ds))
