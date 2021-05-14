# -*- coding: utf-8 -*-
from scipy.stats import kurtosis

dataList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( 'curtosis: {}'.format( kurtosis(dataList) ))


print('curtosis Negativa se llama Leptocúrtica')
print('curtosis 0 se llama Mesocúrtica')
print('curtosis Positiva se llama Platicúrtica')


dataTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print( 'Simetrica: {}'.format( kurtosis(dataTuple) ))


import pandas as pd
dataFrame = pd.DataFrame(dataList, columns =['valores'])
print(type(dataFrame))
print("Media del dataFrame usando Statistics es : % s " % (kurtosis(dataFrame['valores'])))