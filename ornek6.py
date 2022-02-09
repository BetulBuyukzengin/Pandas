# -*- coding: utf-8 -*-
"""
dataset: https://www.kaggle.com/fazilbtopal/auto85
auto.csv kullanarak,

Motor yeri önde olan araba markalarının kaç tanesi benzini (gas) yakıt olarak kullanmaktadır?
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("auto.csv",na_values=['?'])
print(df.columns)

on_motor=df[df['engine-location']=='front']
print("motoru önde  olan marka sayısı ",len(on_motor))
motorlu_g=on_motor.groupby(['fuel-type']).get_group('gas')
print("motoru önde  olan gas kullanan marka sayısı",len(motorlu_g))
