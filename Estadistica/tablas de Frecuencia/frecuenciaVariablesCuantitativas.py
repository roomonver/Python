# -*- coding: utf-8 -*-

import pandas as pd
iris = pd.read_csv("https://raw.githubusercontent.com/toneloy/data/master/iris.csv")



'''
Al contar las frecuencias del df, tenemos un listado enorme que hace poco practica
la lectura y comprension de la tabla.
'''

print((iris
  .groupby("sepal_length")
  .agg(frequency=("sepal_length", "count"))))

'''
Para ellos es conveniente generar intervalos que den mayor sentido a la comprension
'''


'''
* * * * * * * * * * * * * * * * * * * * * 
Agrupacion con pd.cut y bins
* * * * * * * * * * * * * * * * * * * * * 
'''

iris["sepal_length_group"] = pd.cut(iris["sepal_length"], bins=5)

#Frecuencia agrupada y contada.
#Los valores superiores del intervalo no se consideran, ya que ese valor
#es el primer valor del intervalo siguiente
frecuenciapdCut =  (iris.groupby("sepal_length_group")
                        .agg(frequency=("sepal_length", "count"))
                        .reset_index()) 
print(frecuenciapdCut)

from plotnine import ggplot, aes,geom_bar, geom_histogram, ggtitle, labs
graficofrecuenciapdCut = (ggplot(frecuenciapdCut, aes(x = "sepal_length_group", y = "frequency")) +
                          geom_bar(stat = 'identity'))
graficofrecuenciapdCut.draw()


'''
* * * * * * * * * * * * * * * * * * * * * 
Agrupacion creando los intervalos
* * * * * * * * * * * * * * * * * * * * * 
'''

#Para ello debemos establecer los intervalos manualmente a traves del metodo Range
#podemos hacerlo como enteros
print( list(range(4, 8+1, 1)) )

# O podemos hacerlo con decimales utilizando numpy
import numpy as np
print( np.arange(4, 8+0.5, 0.5) )

bins = list(range(4, 8+1, 1))
iris["sepal_length_group_range"] = pd.cut(iris["sepal_length"], bins=bins)

frecuenciaRange=  (iris.groupby("sepal_length_group_range")
                        .agg(frequency=("sepal_length", "count"))
                        .reset_index()) 

graficoFrecuenciaRange = (ggplot(frecuenciaRange, aes(x = "sepal_length_group_range", y = "frequency")) +
                          geom_bar(stat = 'identity'))
graficoFrecuenciaRange.draw()


'''
* * * * * * * * * * * * * * * * * * * * * 
Frecuencia Acumulada
* * * * * * * * * * * * * * * * * * * * * 
'''

# Para llevar la frecuencia acumulada tenemos que definir los bins de alguna forma
# ya sea con range o pd.cut().
# Se utilizara frecuencia definida en frecuenciaRange

frecuenciaRange["cum_frequency"] = frecuenciaRange["frequency"].cumsum()



'''
* * * * * * * * * * * * * * * * * * * * * 
Histograma
* * * * * * * * * * * * * * * * * * * * *
'''

# con binwidth se define el itervalo
histograma = (ggplot(iris) +
              geom_histogram(aes(x = "sepal_length"), binwidth=0.1, boundary=4, colour='lightblue', fill='green')+
              ggtitle('Largo Sepalo: Distribución de frecuencia') +
              labs(x='Largo Sepalo', y='frecuencia'))
histograma.draw()


