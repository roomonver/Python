# -*- coding: utf-8 -*-

import statistics 


dataList = [1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7,7,7, 8, 9, 10]
print(type(dataList))
print("Moda de la lista es : % s " % (statistics.mode(dataList)))


dataTuple = (1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10)
print(type(dataTuple))
print("Moda de la tupla es : % s " % (statistics.mode(dataTuple)))

dataSet = set([1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10])
print(type(dataSet))
print("Moda de la un conjunto es : % s " % (statistics.mode(dataSet)))

import pandas as pd
dataFrame = pd.DataFrame(dataList, columns =['valores'])
print(type(dataFrame))
print("Moda del dataFrame usando Statistics es : % s " % (statistics.mode(dataFrame['valores'])))
print("Moda del dataFrame útilizando mode() es : {} ".format(dataFrame['valores'].mode().values[0]))
