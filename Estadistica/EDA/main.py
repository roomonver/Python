# -*- coding: utf-8 -*-

'''

Tipos de analasis

Analisis Descriptivo
Analisis Exploratorio
Analisis inferencial: certeza de si un evento pasa o no pasa.
Analisis Predictivos: Ocupar relaciones para determinar si puede pasar en el furuto.
analisis Causal


'''

import pandas as pd
from collections import Counter
import statistics as st
df = pd.read_csv('ESalud19.csv')

#Posicion
estaturaMedia = df['ESTATURA'].mean()
estaturaMediana = df['ESTATURA'].median()
print(df['ESTATURA'].describe())

#Dispersion
print( df['ESTATURA'].max() - df['ESTATURA'].min() )

q3 = df['ESTATURA'].quantile(0.75)
q1 = df['ESTATURA'].quantile(0.25)

iqr = q3 - q1
print(iqr)

var =  df['ESTATURA'].var()
print(var)

de =  df['ESTATURA'].std()
print(de)


asimetria = df['ESTATURA'].skew()
print(asimetria)

curtosis = df['ESTATURA'].kurt()
print(curtosis)

import matplotlib.pyplot as plot
# plot.boxplot(df['ESTATURA'])
# plot.show()


plot.hist(x=df['ESTATURA'], bins = 50)
plot.show()

df.boxplot(column =['ESTATURA'], grid = False)