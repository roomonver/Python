# -*- coding: utf-8 -*-

import pandas as pd

dfr = pd.read_csv('advertising.csv')
import numpy as np



def corr_Coeff(df, x, y):
    
    df['corrn'] = (df[x] - np.mean(df[x])) * (df[y]-np.mean(df[y]))
    df['corrX'] = (df[x]-np.mean(df[x]))**2
    df['corrY'] = (df[y]-np.mean(df[y]))**2
    
    corrPearson = sum(df['corrn']/np.sqrt(sum(df['corrX'])*sum(df['corrY'])))
    return(corrPearson)


'''
Para calulaar la correlacion entre variables
'''
corrPearsonDef = corr_Coeff(dfr, 'TV', 'Sales')

'''
para calcular la correlacion sobre todo el dataframe
'''
pdCorr = dfr.corr()



import matplotlib.pyplot as plt

plt.plot(dfr['TV'], dfr['Sales'],'ro')
plt.plot(dfr['Radio'], dfr['Sales'],'bo')
plt.plot(dfr['Newspaper'], dfr['Sales'],'go')
plt.title('Gasto en Publicidad vs Ventas del producto')


plt.matshow(dfr.corr())
