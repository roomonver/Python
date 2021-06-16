# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns 
import numpy as np
from scipy import stats as stats

orig = pd.read_excel("OrigenDestino.xlsx",sheet_name="Nunoa")
# print(orig.TiempoViaje.describe())

tv = orig['TiempoViaje'][ (orig['TiempoViaje'].notna()) & (orig['TiempoViaje']>0)]
print( orig['TiempoViaje'])
sns.histplot(tv,bins=30)

'''
python usa una reparametrización diferente a la de R en cuanto a la distribución, 
por ello es necesario escalar el eje X multiplicando por el parametro rate, 
como muestra a continuación:
'''

shape = 1.60
rate = 0.04

eje_x = np.arange(0,700)
eje_y= rate * stats.gamma.pdf(x=rate*eje_x,a=shape,loc=0,scale=1)
print(eje_y)
sns.histplot(tv,bins=30,stat="density");
sns.lineplot( x=eje_x, y=eje_y,color='red')