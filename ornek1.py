# -*- coding: utf-8 -*-
"""
dataset: https://www.kaggle.com/fazilbtopal/auto85
auto.csv kullanarak,
Her kolon için tanımlayıcı istatistiksel testlerini (min, max, std, median, mean) uygulayınız.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("auto.csv", na_values=['?'])
print(df.columns)

print("symboling için istatistikler: ",df.groupby(['symboling']).agg([np.mean,np.median,np.std]))
print("normalized-losses için istatistikler: ",df.groupby(['normalized-losses']).agg([np.mean,np.median,np.std]))
print("make için istatistikler: ",df.groupby(['make']).agg([np.mean,np.median,np.std]))
print("fuel-type için istatistikler: ",df.groupby(['fuel-type']).agg([np.mean,np.median,np.std]))
print("aspiration için istatistikler: ",df.groupby(['aspiration']).agg([np.mean,np.median,np.std]))
print("num-of-doors için istatistikler: ",df.groupby(['num-of-doors']).agg([np.mean,np.median,np.std]))
print("body-style için istatistikler: ",df.groupby(['body-style']).agg([np.mean,np.median,np.std]))
print("drive-wheels için istatistikler: ",df.groupby(['drive-wheels']).agg([np.mean,np.median,np.std]))

print("engine-location için istatistikler: ",df.groupby(['engine-location']).agg([np.mean,np.median,np.std]))
print("wheel-base için istatistikler: ",df.groupby(['wheel-base']).agg([np.mean,np.median,np.std]))
print("length için istatistikler: ",df.groupby(['length']).agg([np.mean,np.median,np.std]))
print("width için istatistikler: ",df.groupby(['width']).agg([np.mean,np.median,np.std]))
print("height için istatistikler: ",df.groupby(['height']).agg([np.mean,np.median,np.std]))
print("curb-weigh için istatistikler: ",df.groupby(['curb-weigh']).agg([np.mean,np.median,np.std]))

print("engine-type için istatistikler: ",df.groupby(['engine-type']).agg([np.mean,np.median,np.std]))
print("num-of-cylinders için istatistikler: ",df.groupby(['num-of-cylinders']).agg([np.mean,np.median,np.std]))
print("engine-size için istatistikler: ",df.groupby(['engine-size']).agg([np.mean,np.median,np.std]))
print("fuel-system için istatistikler: ",df.groupby(['fuel-system']).agg([np.mean,np.median,np.std]))
print("bore için istatistikler: ",df.groupby(['bore']).agg([np.mean,np.median,np.std]))
print("stroke için istatistikler: ",df.groupby(['stroke']).agg([np.mean,np.median,np.std]))

print("compression-ratio için istatistikler: ",df.groupby(['compression-ratio']).agg([np.mean,np.median,np.std]))
print("horsepower için istatistikler: ",df.groupby(['horsepower']).agg([np.mean,np.median,np.std]))
print("peak-rpm için istatistikler: ",df.groupby(['peak-rpm']).agg([np.mean,np.median,np.std]))
print("city-mpg için istatistikler: ",df.groupby(['city-mpg']).agg([np.mean,np.median,np.std]))
print("highway-mpg için istatistikler: ",df.groupby(['highway-mpg']).agg([np.mean,np.median,np.std]))
print("price için istatistikler: ",df.groupby(['price']).agg([np.mean,np.median,np.std]))
