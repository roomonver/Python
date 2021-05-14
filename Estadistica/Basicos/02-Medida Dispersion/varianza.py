# -*- coding: utf-8 -*-
import statistics 


dataList = [1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10]
print(type(dataList))
print("Varianza de la lista es : % s " % (statistics.variance(dataList)))

meanValue = statistics.mean(dataList)
varianza = statistics.variance(dataList, meanValue) 
print("Varianza de la lista con la media es : % s " % (varianza))


dataTuple = (1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10)
print(type(dataTuple))
print("Varianza de la tupla es : % s " % (statistics.variance(dataTuple)))

meanValue = statistics.mean(dataTuple)
varianza = statistics.variance(dataTuple, meanValue) 
print("Varianza de la tupla con la media es : % s " % (varianza))


dataSet = set([1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10])
print(type(dataSet))
print("Varianza de la un conjunto es : % s " % (statistics.variance(dataSet)))

meanValue = statistics.mean(dataSet)
varianza = statistics.variance(dataSet, meanValue) 
print("Varianza del conjunto con la media es : % s " % (varianza))

import pandas as pd
dataFrame = pd.DataFrame(dataList, columns =['valores'])
print(type(dataFrame))
print("Varianza del dataFrame usando Statistics es : % s " % (statistics.variance(dataFrame['valores'])))
print("Varianza del dataFrame útilizando mode() es : {} ".format(dataFrame['valores'].var()))