# -*- coding: utf-8 -*-
import statistics 


dataList = [1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10]
print(type(dataList))
print("Media de la lista es : % s " % (statistics.mean(dataList)))

dataTuple = (1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10)
print(type(dataTuple))
print("Media de la tupla es : % s " % (statistics.mean(dataTuple)))

dataSet = set([1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10])
print(type(dataSet))
print("Media de la un conjunto es : % s " % (statistics.mean(dataSet)))

import pandas as pd
dataFrame = pd.DataFrame(dataList, columns =['valores'])
print(type(dataFrame))
print("Media del dataFrame usando Statistics es : % s " % (statistics.mean(dataFrame['valores'])))

print("Media del dataFrame útilizando mean() es : % s " % dataFrame['valores'].mean())