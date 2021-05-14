# -*- coding: utf-8 -*-
import statistics 
import numpy 

dataList = [1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10]
print(type(dataList))
print("Media de la lista es : % s " % (statistics.mean(dataList)))
print("Media de la lista con numpy es : % s " % (numpy.mean(dataList)))

dataTuple = (1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10)
print(type(dataTuple))
print("Media de la tupla es : % s " % (statistics.mean(dataTuple)))
print("Media de la tupla con numpy es : % s " % (numpy.mean(dataTuple)))

dataSet = set([1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10])
print(type(dataSet))
print("Media de la un conjunto es : % s " % (statistics.mean(dataSet)))


dic = {'Juan': 50, 'Mariela':40, 'Pedro': 30}
print(type(dic))
print("Media de la dic es : % s " % (statistics.mean(dic.values())))

import pandas as pd
dataFrame = pd.DataFrame(dataList, columns =['valores'])
print(type(dataFrame))
print("Media del dataFrame usando Statistics es : % s " % (statistics.mean(dataFrame['valores'])))
print("Media del dataFrame útilizando mean() es : % s " % dataFrame['valores'].mean())