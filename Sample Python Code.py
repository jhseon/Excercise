# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 08:19:05 2023

@author: KHU
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [2, 5, 4, 4, 0, 2, 7, 8, 8, 8, 1, 3]
df = pd.Series(data)
print('Sorted Values of df \n', df.sort_values())
df.mean()  #평균값 mean
df.median() # 중간값 median 
df.mode() # 최빈값 mode
df.std() #  표준편차 Standard Deviation
df.var() # 분산 Variance = std**2

plt.title("Histogram")

df.hist(bins=np.arange(df.min(), df.max()+1, 0.1), align='mid')

plt.scatter(df.mean(),3, color='red', s=20)
plt.annotate('Mean', (df.mean()+0.2,3) )

plt.scatter(df.mode(),3, color='red', s=20)
plt.annotate('Mode', (df.mode()+0.2,3) )

plt.xlabel('data')
plt.ylabel('Frequency')
