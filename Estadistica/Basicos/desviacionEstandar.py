# -*- coding: utf-8 -*-
import statistics 
import numpy 

dataList = [1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10]
print(type(dataList))
print("Deviación Estandar Poblacion de la lista es : % s " % (statistics.pstdev(dataList)))
print("Deviación Estandar Poblacion Numpy de la lista es : % s " % (numpy.std(dataList)))
print("Deviación Estandar Muestra de la lista es : % s " % (statistics.stdev(dataList)))
print("Deviación Estandar Muestra Numpy de la lista es : % s " % (numpy.std(dataList, ddof =1)))

dic = {'Juan': 50, 'Mariela':40, 'Pedro': 30}
print(type(dic))
print("Deviación Estandar Poblacion de diccionario es : % s " % (statistics.pstdev(dic.values())))
print("Deviación Estandar Poblacion Numpy de diccionario es : % s " % (numpy.std(list(dic.values()))))


dataTuple = (1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10)
print(type(dataList))
print("Deviación Estandar Poblacion de la tupla es : % s " % (statistics.pstdev(dataTuple)))
print("Deviación Estandar Poblacion tupla de la lista es : % s " % (numpy.std(dataTuple)))

dataSet = set([1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10])
print(type(dataSet))
print("Deviación Estandar Poblacion de la dataSet es : % s " % (statistics.pstdev(dataSet)))
print("Deviación Estandar Poblacion tupla de la dataSet es : % s " % (numpy.std(list(dataSet))))

import pandas as pd
dataFrame = pd.DataFrame(dataList, columns =['valores'])
print(type(dataFrame))
print("Deviación Estandar Poblacion de la dataFrame es : % s " % (statistics.pstdev(dataFrame['valores'])))
print("Deviación Estandar Poblacion de la dataFrame es : % s " % (dataFrame['valores'].std(ddof=0)))
print("Deviación Estandar Muestra de la dataFrame es : % s " % (dataFrame['valores'].std(ddof=1)))
print("Deviación Estandar Muestra de la dataFrame es : % s " % (dataFrame['valores'].std()))