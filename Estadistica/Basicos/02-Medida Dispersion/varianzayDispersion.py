# -*- coding: utf-8 -*-

import pandas as pd

iris = pd.read_csv("https://raw.githubusercontent.com/toneloy/data/master/iris.csv")


'''
* * * * * * * * * * * * * * * * 
Promedio de las desviaciones
* * * * * * * * * * * * * * * * 
'''

iris["sepal_length_deviations"] = iris["sepal_length"] - iris["sepal_length"].mean()
print("Media: ",  iris["sepal_length"].mean() )
print("Media de las desviaciones: ", iris["sepal_length_deviations"].mean() )


'''
* * * * * * * * * * * * * * * * 
Desviacion Media
* * * * * * * * * * * * * * * * 
'''

md = iris["sepal_length"].mad()
print("Desviacion Media: ", md)

'''
* * * * * * * * * * * * * * * * 
Desviacion Media
* * * * * * * * * * * * * * * * 
'''
print("Cuasi Varianza: ", iris["sepal_length"].var() )
print("Varianza: ", iris["sepal_length"].var(ddof=0) )


iris["petal_length_plus_one"] = iris["petal_length"] + 1
iris["petal_length_double"] = iris["petal_length"] * 2

print("Varianza: ",iris["petal_length"].var())
print("Varianza + 1: ",iris["petal_length_plus_one"].var())
print("Varianza * 2: ",iris["petal_length_double"].var())

#Al muliutuplicar por una constante, para obtener
print("Varianza * 2: ",(iris["petal_length_plus_one"].var()*2**2))


'''
* * * * * * * * * * * * * * * * 
Menor suma de desvios
* * * * * * * * * * * * * * * * 
'''
import numpy as np

mean_petal_length = iris["petal_length"].mean()
min_petal_length = mean_petal_length - 3
max_petal_length = mean_petal_length + 3

alpha_n_steps = 100
alpha_step = (max_petal_length - min_petal_length) / (alpha_n_steps + 1)
alpha_values = np.arange(min_petal_length, max_petal_length+alpha_step, alpha_step)
alpha_values = np.append(alpha_values, iris["petal_length"].mean())

def sum_of_squares(alpha, df, column):
  square_deviations = (df[column] - alpha).pow(2)
  df = pd.DataFrame({"ss": [square_deviations.sum()], "alpha": [alpha]})
  
  return df

ss = pd.concat([sum_of_squares(alpha, iris, "petal_length") for alpha in alpha_values])

from plotnine import ggplot, aes, ggtitle, labs, geom_line,geom_vline
(ggplot(ss, aes(x="alpha", y="ss")) +
  geom_line() +
  geom_vline(aes(xintercept=mean_petal_length), linetype="dashed", colour="red") +
  ggtitle("Suma de desvíos al cuadrado con respecto a distintos valores") +
  labs(y="Suma de desvíos al cuadrado")
).draw()