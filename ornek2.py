"""dataset: https://www.kaggle.com/fazilbtopal/auto85
auto.csv kullanarak,
Veri setinde kaç tane araba markası vardır?
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("auto.csv")

markalar=df['make'].unique()
print("Veri setindeki araba markaları ",markalar)
print("Veri setindeki araba markalarının sayısı: ",markalar.size)





