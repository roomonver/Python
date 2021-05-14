# -*- coding: utf-8 -*-


#Para acceder a las funciones estadisticas se debe importar el paquete statistics
import statistics 
import numpy 

dataList = [1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10]
print(type(dataList))
print("Mediana de la lista es : % s " % (statistics.median(dataList)))
print("Mediana de la lista con numpy es : % s " % (numpy.median(dataList)))

dataTuple = (1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10)
print(type(dataTuple))
print("Mediana de la tupla es : % s " % (statistics.median(dataTuple)))

dataSet = set([1, 2, 3, 4, 5, 3, 6, 4, 9, 2, 4, 1, 7, 7, 8, 9, 10])
print(type(dataSet))
print("Mediana de la un conjunto es : % s " % (statistics.median(dataSet)))

import pandas as pd
dataFrame = pd.DataFrame(dataList, columns =['valores'])
print(type(dataFrame))
print("Mediana del dataFrame usando Statistics es : % s " % (statistics.median(dataFrame['valores'])))

print("Mediana del dataFrame útilizando median() es : % s " % dataFrame['valores'].median())


  